# initHACK

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Tool Category](https://img.shields.io/badge/Category-Pentesting-red.svg)

**initHACK** is a modern, interactive automation tool designed to streamline the initial enumeration phase of a penetration test. Written in Python, it replaces clunky manual commands with a beautiful CLI that handles directory creation, OS fingerprinting, and multi-stage Nmap scanning.

---

## Features

*   **Interactive UI:** Powered by `Questionary` and `Rich`. No more typing numbers—use your arrow keys to navigate menus.
*   **Smart OS Detection:** Automatically estimates the target OS (Linux/Windows) by analyzing ICMP TTL values from a ping request.
*   **Automated Workflow:**
    *   **Phase 1:** Creates a standardized project structure (`nmap/`, `content/`, `exploits/`).
    *   **Phase 2:** Performs a fast "All Ports" stealth scan to find open gates.
    *   **Phase 3:** Automatically parses results to launch a targeted "Deep Scan" (Service Versions/Default Scripts).
*   **Persistent Target IP:** Remembers your Target IP throughout the session so you only have to enter it once.
*   **Clean Exits:** Handles `Ctrl+C` gracefully without messy Python error traces.

---

##  Installation

### 1. Prerequisites
You must have `nmap` installed on your system:
```bash
sudo apt update && sudo apt install nmap -y
```

### 2. Clone the Repository
```bash
git clone https://github.com/Z4kr-Sec/initHACK.git
cd initHACK
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

---

(Or manually: pip3 install rich questionary art termcolor)

## Usage

Run the script with sudo privileges (required for Nmap stealth scans *-sS*):

```bash
sudo python3 init-hack.py
```
![alt text](/img/init.png)

### Typical Workflow:
- **Option 2**: Setup your working folders.
- **Option 1**: Identify if the target is Linux or Windows.
- **Option 3**: Run the fast port discovery.
- **Option 4**: Let the script automatically parse those ports and run a deep service scan.

---


| Feature | Description |
|---|---|
| Menu | Interactive arrow-key selection |
| OS Detection | Clean table showing IP, TTL, and Guest OS |
| Nmap Logic | Automated port extraction and chain scanning |


## 📂 Project Structure Created
When you use the directory creation feature, the tool generates:
```text
.
├── content/      # For web files, notes, or raw data
├── exploits/     # For Proof of Concepts and downloaded scripts
└── nmap/         # For all Nmap scan results
```

---

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.


## ⚖️ License & Disclaimer
This tool is for **educational and ethical testing purposes only**. Usage of initHACK against targets without prior mutual consent is illegal. The author is not responsible for any misuse or damage caused by this tool.

Distributed under the MIT License. 

---
**Developed by [Z4kr](https://github.com/Z4kr-Sec)**