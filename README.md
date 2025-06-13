# 🔒 Python DDoS Simulation Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Educational](https://img.shields.io/badge/purpose-educational-orange.svg)](https://github.com/Bilal-XQ/python-ddos-tool)

A comprehensive Python-based tool designed to simulate Distributed Denial-of-Service (DDoS) attacks in controlled environments for cybersecurity education and network stress testing research.

---

## 🚨 **IMPORTANT LEGAL DISCLAIMER**

> ⚠️ **FOR EDUCATIONAL PURPOSES ONLY** ⚠️
> 
> This tool is developed exclusively for:
> - **Educational research** and learning about network security
> - **Authorized penetration testing** on systems you own
> - **Academic studies** in cybersecurity programs
> 
> **🚫 ILLEGAL USES:**
> - Attacking systems without explicit written permission
> - Disrupting services you don't own
> - Any malicious activities
> 
> **By using this tool, you agree to use it responsibly and legally. The authors disclaim all responsibility for misuse.**

---

## 📋 Table of Contents

- [Features](#-features)
- [Technologies](#-technologies-used)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Examples](#-examples)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

- 🎯 **Multiple Attack Types**: TCP, UDP, HTTP flood simulations
- ⚙️ **Customizable Parameters**: Thread count, request rate, payload size
- 📊 **Real-time Monitoring**: Live statistics and performance metrics
- 🛡️ **Safety Controls**: Built-in rate limiting and target validation
- 📱 **Web Interface**: Optional HTML/CSS dashboard for monitoring
- 📈 **Detailed Logging**: Comprehensive attack logs and reports
- 🔧 **Easy Configuration**: YAML/JSON config file support

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core simulation engine | 3.8+ |
| **HTML/CSS** | Web dashboard interface | HTML5/CSS3 |
| **Threading** | Concurrent request handling | Built-in |
| **Requests** | HTTP operations | Latest |
| **Socket** | Low-level network operations | Built-in |

---

## 📋 Prerequisites

Before running this tool, ensure you have:

- ✅ **Python 3.8 or higher**
- ✅ **pip package manager**
- ✅ **Internet connection**
- ✅ **Administrative privileges** (for some network operations)
- ✅ **Written permission** for any target systems

**System Requirements:**
- RAM: 2GB minimum
- CPU: Multi-core recommended
- OS: Windows 10+, macOS 10.15+, Linux Ubuntu 18.04+

---

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Bilal-XQ/python-ddos-tool.git
cd python-ddos-tool
```

### 2. Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
python main.py --help
```

---

## ⚙️ Usage

### Basic Usage
```bash
# Run with default settings
python main.py

# Show help and available options
python main.py --help

# Quick stress test (safe mode)
python main.py --target localhost --port 8080 --threads 10 --duration 30
```

### Advanced Usage
```bash
# HTTP flood simulation
python main.py --type http --target example.com --threads 50 --rate 100

# UDP flood with custom payload
python main.py --type udp --target 192.168.1.100 --port 53 --payload-size 1024

# Using configuration file
python main.py --config config/test-config.json
```

### Web Interface
```bash
# Start with web dashboard
python main.py --web-interface --port 5000
# Open browser to http://localhost:5000
```

---

## 🔧 Configuration

### Command Line Options
```bash
Options:
  --target TARGET       Target IP or domain
  --port PORT          Target port (default: 80)
  --threads THREADS    Number of threads (default: 10)
  --duration DURATION  Attack duration in seconds
  --type TYPE          Attack type: http, tcp, udp
  --rate RATE          Requests per second
  --config CONFIG      Configuration file path
  --web-interface      Enable web dashboard
  --safe-mode          Enable safety restrictions
```

### Configuration File Example
```json
{
  "target": "localhost",
  "port": 8080,
  "attack_type": "http",
  "threads": 20,
  "duration": 60,
  "rate_limit": 100,
  "payload_size": 512,
  "user_agent": "DDoS-Simulation-Tool/1.0",
  "safety_checks": true
}
```

---

## 📊 Examples

### Example 1: Local Server Stress Test
```bash
# Test your own web server
python main.py --target localhost --port 3000 --threads 5 --duration 30
```

### Example 2: Network Research
```bash
# Controlled network analysis
python main.py --config examples/research-config.json --safe-mode
```

### Example 3: Educational Demonstration
```bash
# Classroom demonstration with monitoring
python main.py --target demo-server.local --web-interface --duration 60
```

---

## 📂 Project Structure

```
python-ddos-tool/
│
├── 📄 main.py                 # Main application entry point
├── 📄 requirements.txt        # Python dependencies
├── 📄 README.md              # Project documentation
├── 📄 LICENSE                # License information
│
├── 📁 src/                   # Source code modules
│   ├── 📄 __init__.py
│   ├── 📄 ddos_simulator.py   # Core DDoS simulation logic
│   ├── 📄 attack_types.py     # Different attack implementations
│   ├── 📄 web_interface.py    # Web dashboard backend
│   └── 📄 utils.py           # Utility functions
│
├── 📁 static/                # Web interface assets
│   ├── 📄 index.html         # Dashboard HTML
│   ├── 📄 style.css          # Dashboard styling
│   └── 📄 script.js          # Dashboard JavaScript
│
├── 📁 config/                # Configuration files
│   ├── 📄 default.json       # Default configuration
│   └── 📄 examples/          # Example configurations
│
├── 📁 logs/                  # Log files directory
├── 📁 docs/                  # Additional documentation
└── 📁 tests/                 # Unit tests
```

---

## 🤝 Contributing

We welcome contributions that enhance the educational value of this tool!

### How to Contribute:

1. **Fork the repository**
   ```bash
   git fork https://github.com/Bilal-XQ/python-ddos-tool.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/educational-enhancement
   ```

3. **Make your changes**
   - Add educational features
   - Improve documentation
   - Enhance safety measures

4. **Test your changes**
   ```bash
   python -m pytest tests/
   ```

5. **Commit and push**
   ```bash
   git commit -m "Add: Educational feature description"
   git push origin feature/educational-enhancement
   ```

6. **Open a Pull Request**

### Contribution Guidelines:
- ✅ Must maintain educational focus
- ✅ Include comprehensive documentation
- ✅ Add safety measures and warnings
- ✅ Follow Python PEP 8 standards
- ❌ No malicious or harmful features

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact & Support

### Developer
- **Name**: Bilal El Azzam
- **GitHub**: [@Bilal-XQ](https://github.com/Bilal-XQ)
- **Email**: bilalelazzam.dev@gmail.com

### Support
- 🐛 **Issues**: [GitHub Issues](https://github.com/Bilal-XQ/python-ddos-tool/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/Bilal-XQ/python-ddos-tool/discussions)
- 📧 **Security**: Report security issues via private email

---

## 🔗 Related Resources

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [Ethical Hacking Resources](https://www.cybrary.it/course/ethical-hacking/)
- [Network Security Fundamentals](https://www.sans.org/cyber-security-courses/)

---

<div align="center">

**⭐ Star this repository if it helped your cybersecurity education!**

[![GitHub stars](https://img.shields.io/github/stars/Bilal-XQ/python-ddos-tool?style=social)](https://github.com/Bilal-XQ/python-ddos-tool/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Bilal-XQ/python-ddos-tool?style=social)](https://github.com/Bilal-XQ/python-ddos-tool/network)

</div>

---

*Remember: With great power comes great responsibility. Use this tool ethically and legally.*
