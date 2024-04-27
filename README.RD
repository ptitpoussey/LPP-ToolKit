# Comprehensive Penetration Testing Suite

## Features
- **Network Discovery and Mapping**: Utilizes Nmap for in-depth network scanning.
- **Vulnerability Scanning**: Integrates with OpenVAS and Nessus to identify vulnerabilities.
- **Real-Time Reporting and Visualization**: Employs the ELK Stack (Elasticsearch, Logstash, Kibana) for dynamic data logging and visualization.
- **Social Engineering Toolkit (SET)**: Includes tools for testing human-related security vulnerabilities.
- **Automated Exploitation**: Leverages Metasploit for executing known exploits based on scan results.
- **Comprehensive Reporting**: Generates detailed reports suitable for both technical analysis and executive summaries.

## Prerequisites
- **Operating System**: Linux (Ubuntu, Kali Linux recommended) or Windows 10/11 with Windows Subsystem for Linux (WSL).
- **Python 3.8 or higher**
- **pip3 (Python Package Installer)**

## Installation

### Linux Users
#### Install Python and pip
```bash
sudo apt update
sudo apt install python3 python3-pip

### Required Tools
sudo apt-get install elasticsearch logstash kibana
sudo apt-get install metasploit-framework openvas set


### Usage
python3 pentest_suite.py


Contributing
Contributions are welcome. Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Support
For support and queries, contact lppousset@protonmail.com.