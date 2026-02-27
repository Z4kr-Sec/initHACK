#!/usr/bin/python3
import sys
import subprocess
import re
import signal
import ipaddress
from art import text2art
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
import questionary

# Initialize Rich Console
console = Console()

# --- Configuration & Styling ---
def print_banner():
    ascii_art = text2art("Init-Hack", font='tarty1')
    console.print(f"[green]{ascii_art}[/green]")
    console.print("[bold cyan]By: W1nz4c4r[/bold cyan] | [dim]https://github.com/W1nz4c4r/initHACK[/dim]\n")

# --- Logic Functions ---

def signal_handler(sig, frame):
    console.print("\n[bold red][-] Exiting program... Happy Hacking :)[/bold red]")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def is_valid_ip(ip):
    try:
        if ip == "0.0.0.0": return False
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def check_os(ip):
    console.print(f"[yellow][*][/yellow] Checking OS for [bold]{ip}[/bold]...")
    try:
        # Run ping command
        process = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True)
        if process.returncode != 0:
            console.print("[red][!] Target is unreachable.[/red]")
            return
        
        # Extract TTL
        ttl_match = re.search(r"ttl=(\d+)", process.stdout, re.IGNORECASE)
        if ttl_match:
            ttl = int(ttl_match.group(1))
            os_name = "LINUX" if ttl <= 64 else "WINDOWS" if ttl <= 128 else "UNKNOWN"
            
            table = Table(title="Target Information", style="cyan")
            table.add_column("Property", style="bold")
            table.add_column("Value")
            table.add_row("IP Address", ip)
            table.add_row("TTL", str(ttl))
            table.add_row("Estimated OS", f"[bold green]{os_name}[/bold green]")
            console.print(table)
        else:
            console.print("[red][!] Could not determine TTL.[/red]")
    except Exception as e:
        console.print(f"[red][!] Error: {e}[/red]")

def create_directories():
    extra = Prompt.ask("[white]Creating nmap, content and explots diretories[/white]\n[magenta][*][/magenta] Extra directories? (comma separated)", default="")
    dirs = ["nmap", "content", "exploits"]
    if extra:
        dirs.extend([d.strip() for d in extra.split(",") if d.strip()])
    
    for d in dirs:
        subprocess.run(["mkdir", "-p", d])
    console.print(f"[green][+] Created:[/green] {', '.join(dirs)}")

def scan_ports(ip):
    console.print(f"[blue][*][/blue] Starting fast port scan on {ip}...")
    cmd = f"sudo nmap -p- --open -sS -vvv -n -Pn {ip} -oN nmap/OP_ports"
    subprocess.run(cmd, shell=True)
    console.print("[bold green][+] Initial scan complete. Results saved to nmap/OP_ports[/bold green]")

def full_scan(ip):
    console.print("[blue][*][/blue] Extracting ports and starting deep scan...")
    try:
        with open("nmap/OP_ports", "r") as f:
            content = f.read()
        
        # Pure Python regex to find open ports (cleaner than awk/sed)
        ports = re.findall(r"(\d+)/tcp\s+open", content)
        
        if not ports:
            console.print("[red][!] No open ports found in nmap/OP_ports. Run option 3 first?[/red]")
            return

        ports_str = ",".join(ports)
        console.print(f"[green][+] Found ports:[/green] [bold]{ports_str}[/bold]")
        
        cmd = f"sudo nmap -sS -sV -sC -p{ports_str} -Pn -n -vvv {ip} -oA nmap/allPorts"
        subprocess.run(cmd, shell=True)
    except FileNotFoundError:
        console.print("[red][!] nmap/OP_ports not found. Run a scan first![/red]")

# --- Main App ---

def main():
    print_banner()
    target_ip = None

    while True:
        # Using questionary for a professional interactive menu
        choice = questionary.select(
            "What would you like to do?",
            choices=[
                "1. Check Machine OS",
                "2. Create Project Directories",
                "3. Scan Open Ports (Nmap Fast)",
                "4. Perform Full Service Scan (Nmap Deep)",
                "5. Set/Change Target IP",
                "Exit"
            ]
        ).ask()

        if choice == "Exit":
            console.print("[red]Happy Hacking! Bye.[/red]")
            break

        # IP management
        if choice in ["1. Check Machine OS", "3. Scan Open Ports (Nmap Fast)", "4. Perform Full Service Scan (Nmap Deep)"]:
            if not target_ip:
                target_ip = Prompt.ask("[yellow][?][/yellow] Enter Target IP")
                while not is_valid_ip(target_ip):
                    target_ip = Prompt.ask("[red][!] Invalid IP. Enter again[/red]")

        if "1." in choice:
            check_os(target_ip)
        elif "2." in choice:
            create_directories()
        elif "3." in choice:
            scan_ports(target_ip)
        elif "4." in choice:
            full_scan(target_ip)
        elif "5." in choice:
            target_ip = Prompt.ask("[yellow][?][/yellow] Enter New Target IP")
            if is_valid_ip(target_ip):
                console.print(f"[green][+] Target updated to: {target_ip}[/green]")

if __name__ == "__main__":
    main()