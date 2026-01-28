#!/usr/bin/env python3

import os
import sys

def check_environment():
    if sys.version_info < (3, 6):
        print("Python 3.6+ required")
        sys.exit(1)

def install_pyshield():
    print("Installing PyShield...")
    
    os.system("chmod +x pyshield.py")
    
    home_dir = os.path.expanduser("~")
    bin_dir = os.path.join(home_dir, ".local", "bin")
    
    os.makedirs(bin_dir, exist_ok=True)
    
    current_path = os.path.abspath("pyshield.py")
    link_path = os.path.join(bin_dir, "pyshield")
    
    if os.path.exists(link_path):
        os.remove(link_path)
    
    os.symlink(current_path, link_path)
    
    print(f"Symlink created: {link_path}")
    print("Installation complete.")
    print("\nUsage: pyshield")

if __name__ == "__main__":
    check_environment()
    install_pyshield()
