
---

# 🚀 initHACK

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Tool Category](https://img.shields.io/badge/Category-Pentesting-red.svg)

**initHACK** is a modern, interactive automation tool designed to streamline the initial enumeration phase of a penetration test. Written in Python, it replaces clunky manual commands with a beautiful CLI that handles directory creation, OS fingerprinting, and multi-stage Nmap scanning.

---

## ✨ Features

*   **Interactive UI:** Powered by `Questionary` and `Rich`. No more typing numbers—use your arrow keys to navigate menus.
*   **Smart OS Detection:** Automatically estimates the target OS (Linux/Windows) by analyzing ICMP TTL values from a ping request.
*   **Automated Workflow:**
    *   **Phase 1:** Creates a standardized project structure (`nmap/`, `content/`, `exploits/`).
    *   **Phase 2:** Performs a fast "All Ports" stealth scan to find open gates.
    *   **Phase 3:** Automatically parses results to launch a targeted "Deep Scan" (Service Versions/Default Scripts).
*   **Persistent Target IP:** Remembers your Target IP throughout the session so you only have to enter it once.
*   **Clean Exits:** Handles `Ctrl+C` gracefully without messy Python error traces.

---

## 🛠️ Installation

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

## 🚀 Usage

Since Nmap requires root privileges for stealth scans (`-sS`), run the script with `sudo`:

```bash
sudo python3 init-hack.py
```

### The Standard Workflow:
1.  **Select Option 2:** Automatically set up your `nmap`, `content`, and `exploits` folders.
2.  **Select Option 1:** Identify if the target is Linux or Windows.
3.  **Select Option 3:** Launch the fast port discovery scan.
4.  **Select Option 4:** The script will automatically read the found ports and start a deep service/script scan.

---

## 📂 Project Structure Created
When you use the directory creation feature, the tool generates:
```text
.
├── content/      # For web files, notes, or raw data
├── exploits/     # For Proof of Concepts and downloaded scripts
└── nmap/         # For all Nmap scan results
```

---

## ⚖️ License & Disclaimer
This tool is for **educational and ethical testing purposes only**. Usage of initHACK against targets without prior mutual consent is illegal. The author is not responsible for any misuse or damage caused by this tool.

Distributed under the MIT License. 

---
**Developed by [Z4kr](https://github.com/Z4kr-Sec)**