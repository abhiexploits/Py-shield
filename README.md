# PyShield 🔒

### Advanced Python Code Obfuscation & Protection Tool

## 📌 Overview

PyShield is a powerful Python code protection system designed to obfuscate and secure your Python scripts against reverse engineering and unauthorized modification. Built with multiple layers of protection, it transforms readable code into a highly secured format that's extremely difficult to decompile.

## ✨ Features

#### ·  Multi-layer obfuscation - Multiple protection layers
#### · Identifier transformation - Randomizes variable/function names
#### · Code compression - Compresses and encodes entire code
#### · Anti-decompilation - Makes decompiling extremely difficult
#### · Integrity verification - Self-checking mechanism
#### · Dead code injection - Adds confusing junk code
#### · Clean interface - Professional hacker-style UI
#### · Termux compatible - Works perfectly on Android/Termux
#### · No external dependencies - Uses only Python standard library

## 🛠️ Installation

### For Termux (Android):

```bash
pkg update && pkg upgrade
pkg install python git
git clone https://github.com/abhiexploits/Py-shield.git
cd Py-shield
python pyshield.py
```

### For Linux:

```bash
sudo apt update
sudo apt install python3 git
git clone https://github.com/abhiexploits/Py-shield.git
cd Py-shield
python3 pyshield.py
```

# 🚀 Quick Start

1. Clone the repository:

```bash
git clone https://github.com/abhiexploits/Py-shield.git
```

1. Run PyShield:

```bash
cd Py-shield
python3 pyshield.py
```

1. Follow the interactive prompts:
   · Enter your Python file path
   · Choose output filename (optional)
   · Let PyShield do the magic! ✨

## 📝 Usage Example

```bash
# Basic usage
python3 pyshield.py

# After running, you'll see:
# 1. Cool ASCII banner
# 2. File path prompt
# 3. Automatic obfuscation process
# 4. Protected file saved as: filename_protected.py
```

## 🔧 How It Works

Protection Layers:

1. Identifier Obfuscation - Renames all variables/functions
2. String Encryption - Encodes strings within code
3. Dead Code Injection - Adds useless confusing code
4. Compression Layer - Compresses entire code
5. Base64 Encoding - Final encoding layer
6. Integrity Check - Adds self-verification

## Input:

```python
# Original code
def calculate(x, y):
    return x + y
```

## Output:

```python
# Obfuscated code (simplified example)
import base64, zlib, marshal
exec(marshal.loads(zlib.decompress(base64.b64decode("eJwL..."))))
```

# 📁 Project Structure

```
Py-shield/
├── pyshield.py          # Main obfuscation tool
├── README.md            # This documentation
├── requirements.txt     # Dependencies (none required)
├── test.py             # Example test file
└── install.sh          # Installation script
```

## ⚙️ Technical Details

Supported Python Versions:

· Python 3.6+
· Python 3.7+
· Python 3.8+
· Python 3.9+
· Python 3.10+
· Python 3.11+

### Dependencies:

· No external packages required
· Uses only Python standard library
· Works offline

### Security Features:

· SHA256 integrity checking
· Anti-debugging techniques
· Code flow obfuscation
· Random seed generation
· Timestamp verification

## 🎯 Use Cases

· Protect proprietary code - Secure your commercial scripts
· License management - Add license verification to your software
· Educational purposes - Learn about code protection techniques
· Security testing - Test your obfuscation methods
· Software distribution - Distribute protected Python applications

## ⚠️ Important Notes

· 100% protection is impossible - Any code can eventually be reverse engineered
· Always keep backups - Keep original code safe before obfuscation
· Test thoroughly - Always test obfuscated code before deployment
· Use responsibly - Only protect code you own or have permission to protect

# 🔍 Testing

Test the obfuscation with provided example:

```bash
# Test with example file
python3 test.py
python3 pyshield.py
# Choose test.py when prompted
# Run the protected version
python3 test_protected.py
```

# 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request
4. Report issues or suggest features

## 📞 Support

· Author: Abhishek
· GitHub: @abhiexploits
· Repository: https://github.com/abhiexploits/Py-shield
· Issues: GitHub Issues page

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⭐ Show Your Support

If you find this tool useful, please:

· ⭐ Star the repository
· 🍴 Fork it
· 🔄 Share with others
· 📢 Spread the word

---

### Made with ❤️ by Abhishek (@abhiexploits)

"Protecting your code, one layer at a time" 🛡️

---

Quick Command Reference:

```bash
# Clone & Run
git clone https://github.com/abhiexploits/Py-shield.git
cd Py-shield
python3 pyshield.py

# Update
cd Py-shield
git pull

# View help
python3 pyshield.py --help
```

### Happy Coding & Stay Protected! 🔐
