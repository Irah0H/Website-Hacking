# Website Vulnerability Scanner and Exploitation Lab

An educational project designed to teach website security by simulating common vulnerabilities like SQL injection, XSS, and weak password management. This project provides tools to scan, exploit, and understand these vulnerabilities in a safe, controlled environment.

---

##  **Disclaimer**

This project is for **educational purposes only**. Do not use the tools provided here to target unauthorized websites or systems. Misuse of this software may violate laws and ethical guidelines.

---

##  **Project Features**

1. **Vulnerable Website**:
   - A Flask-based web application intentionally designed with vulnerabilities for testing purposes.
   - Includes pages to demonstrate SQL injection, XSS, and insecure login mechanisms.

2. **Hacking Tools**:
   - **SQL Injection Tool**: Exploits vulnerable database queries.
   - **XSS Tester**: Identifies cross-site scripting vulnerabilities.
   - **Password Brute-Forcer**: Demonstrates cracking weak passwords using wordlists.
   - **Vulnerability Scanner**: Scans websites for common security flaws, such as insecure cookies.

3. **Educational Reports**:
   - Sample reports that explain discovered vulnerabilities and suggest mitigation techniques.

4. **Security Tutorials**:
   - Step-by-step guides on how to fix the demonstrated vulnerabilities.

---

## 🏗 **Project Structure**

```plaintext
website-hacking-lab/
│
├── tools/                     # Hacking tools for testing vulnerabilities
│   ├── vulnerability_scanner.py
│   ├── sql_injection_tool.py
│   ├── xss_tester.py
│   ├── password_bruteforcer.py
│
├── vulnerable-site/            # Flask app for the vulnerable website
│   ├── app.py
│   ├── templates/              # HTML templates for the web pages
│   ├── static/                 # Static files (CSS, JS)
│   └── database.db             # SQLite database
│
├── reports/                    # Example vulnerability reports
│   ├── vulnerability_report.txt
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── LICENSE                     # License file
└── .gitignore                  # Ignored files and folders



🛠️ Features and Usage
1. Vulnerable Website
Simulates:
SQL Injection: Exploit vulnerabilities in login forms or search bars.
XSS: Inject malicious scripts into comment sections.
Weak Passwords: Test the login page with brute-forcing.

## SQL Injection tool
python tools/sql_injection_tool.py

## XSS Tester
python tools/xss_tester.py

##Password Brute Forcer
python tools/password_bruteforcer.py

## Vulnerability Scanner
python tools/vulnerability_scanner.py


