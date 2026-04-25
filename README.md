# 🛡️ Aegis-Gen v1.2
> **AI-Powered Vulnerability Orchestrator & Strategic Analyst**

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Engine](https://img.shields.io/badge/AI-Gemini%203%20Flash-orange.svg)](https://ai.google.dev/)

---

## 📖 Overview
**Aegis-Gen** is a professional-grade security tool designed for **Kali Linux**. It automates the transition from passive reconnaissance to active strategic planning. By merging **Nmap's** precision with the reasoning power of **Gemini 3 Flash**, it transforms raw port data into a high-level tactical roadmap for penetration testers.

---

## 🛠️ The Architecture
Aegis-Gen follows a modular "Scout-Brain" architecture:

* **🛰️ Scout Module (`scout.py`):** Performs deep-service fingerprinting, identifying open ports, service versions, and OS details.
* **🧠 Brain Module (`brain.py`):** Ingests raw XML/text data and uses the **2026 Gemini SDK** to map findings to known CVEs and misconfigurations.
* **📋 Controller (`main.py`):** Orchestrates the data flow and generates the final **Strategic Attack Plan**.

---

## 🚀 Features
- [x] **Autonomous Analysis:** No manual CVE searching required.
- [x] **Live SDK Integration:** Built on the latest `google-genai` library.
- [x] **Secret Management:** Securely handles API keys via `.env` files.
- [x] **Tactical Output:** Provides exact Metasploit modules and Kali commands for validation.

---

## ⚙️ Installation & Setup

### 1. Clone the Arsenal
```bash
git clone [https://github.com/NuttyHack/AegisGen.git](https://github.com/NuttyHack/AegisGen.git)
cd AegisGen
2. Prepare the Environment
Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Deploy API Secrets
Create a .env file in the root folder:

Bash
echo "GEMINI_API_KEY=your_key_here" > .env
4. Execute Scan
Bash
python3 main.py
📊 Sample Output
When pointed at a target, the AI provides:

Risk Assessment: Criticality rating for each open service.

Attack Vector: Specific commands (e.g., nmap --script, msfconsole).

Remediation: Step-by-step instructions for sysadmins to patch the holes.

⚠️ Legal Disclaimer
FOR EDUCATIONAL PURPOSES ONLY. This tool was developed by NuttyHack to demonstrate the integration of AI in cybersecurity. Use of this tool for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state, and federal laws.
