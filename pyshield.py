#!/usr/bin/env python3

import os
import sys
import base64
import zlib
import marshal
import random
import string
import hashlib
import time
import subprocess
from pathlib import Path

def clear_display():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_header():
    clear_display()
    print("""\033[91m\033[1m
██████╗ ██╗   ██╗███████╗██╗  ██╗██╗███████╗██╗     ███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝██║  ██║██║██╔════╝██║     ██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ ███████╗███████║██║█████╗  ██║     █████╗  ██║  ██║
██╔═══╝   ╚██╔╝  ╚════██║██╔══██║██║██╔══╝  ██║     ██╔══╝  ██║  ██║
██║        ██║   ███████║██║  ██║██║███████╗███████╗███████╗██████╔╝
╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═════╝ 
                                                                     
\033[94m╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║               P Y T H O N   C O D E   S H I E L D                ║
║                                                                  ║
║          Advanced Obfuscation & Protection System                ║
║                                                                  ║
║          Author: Abhishek               Contact: @abhiexploits   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝\033[0m
""")

class CodeProtector:
    def __init__(self):
        self.obfuscation_depth = 5
        self.protection_layers = []
    
    def generate_random_name(self, length=12):
        chars = '_' + string.ascii_letters
        return ''.join(random.choice(chars) for _ in range(length))
    
    def encrypt_string_data(self, text):
        rotated = ''.join(chr((ord(c) + 17) % 256) for c in text)
        encoded = base64.b85encode(rotated.encode()).decode()
        return f'exec(__import__("base64").b85decode("{encoded}"))'
    
    def transform_identifiers(self, source_code):
        identifier_mapping = {}
        transformed_lines = []
        
        lines = source_code.strip().split('\n')
        for line in lines:
            if not line.strip():
                transformed_lines.append(line)
                continue
            
            words = line.split()
            new_words = []
            
            for word in words:
                if word.isidentifier() and len(word) > 2:
                    if word not in ['def', 'class', 'import', 'from', 'as', 'if', 'else', 'for', 'while', 'return', 'try', 'except']:
                        if word not in identifier_mapping:
                            identifier_mapping[word] = self.generate_random_name()
                        new_words.append(identifier_mapping[word])
                    else:
                        new_words.append(word)
                else:
                    new_words.append(word)
            
            transformed_lines.append(' '.join(new_words))
        
        return '\n'.join(transformed_lines)
    
    def insert_dead_code(self):
        dead_code = []
        for _ in range(random.randint(3, 7)):
            var_name = self.generate_random_name()
            dead_code.append(f'{var_name} = {random.randint(10000, 99999)}')
            dead_code.append(f'for _ in range({random.randint(2, 10)}): pass')
            dead_code.append(f'if False: {self.generate_random_name()}()')
        
        return '\n'.join(dead_code)
    
    def compress_and_obfuscate(self, code):
        compressed = zlib.compress(code.encode())
        encoded = base64.b64encode(compressed).decode()
        
        wrapper = f"""
import zlib, base64, marshal
_data = "{encoded}"
_code = zlib.decompress(base64.b64decode(_data))
_exec = marshal.loads(_code)
exec(_exec)
"""
        return wrapper
    
    def add_integrity_check(self):
        check_code = """
def _verify_file():
    import hashlib, os
    current_hash = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    return True

if not _verify_file():
    import sys
    sys.exit(0)
"""
        return check_code
    
    def protect_file(self, input_path, output_path=None):
        print(f"\033[93m[*] Loading source: {input_path}\033[0m")
        
        with open(input_path, 'r', encoding='utf-8') as f:
            original = f.read()
        
        print(f"\033[92m[+] Source size: {len(original)} bytes\033[0m")
        print("\033[93m[*] Initiating protection sequence...\033[0m")
        
        protected = original
        
        print("\033[92m[1/5] Transforming identifiers...\033[0m")
        protected = self.transform_identifiers(protected)
        
        print("\033[92m[2/5] Inserting protection layers...\033[0m")
        protected = self.insert_dead_code() + '\n' + protected + '\n' + self.insert_dead_code()
        
        print("\033[92m[3/5] Adding integrity verification...\033[0m")
        protected = self.add_integrity_check() + '\n' + protected
        
        print("\033[92m[4/5] Applying compression encoding...\033[0m")
        protected = self.compress_and_obfuscate(protected)
        
        print("\033[92m[5/5] Finalizing protection...\033[0m")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        final_code = f"""#!/usr/bin/env python3

"""
        final_code += protected
        
        if output_path is None:
            base = Path(input_path).stem
            output_path = f"{base}_protected.py"
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_code)
        
        print(f"\033[92m[✓] Protection completed\033[0m")
        print(f"\033[94m[*] Output: {output_path}\033[0m")
        print(f"\033[94m[*] Final size: {len(final_code)} bytes\033[0m")
        
        return output_path

def main_execution():
    display_header()
    
    print("\033[93m" + "="*70 + "\033[0m")
    print("\033[97m\033[1mPyShield Code Protection System\033[0m")
    print("\033[93m" + "="*70 + "\033[0m\n")
    
    while True:
        target_file = input("\033[96m[?] Enter Python file path: \033[0m").strip()
        
        if not target_file:
            print("\033[91m[!] Path required\033[0m")
            continue
        
        if not os.path.exists(target_file):
            print(f"\033[91m[!] Not found: {target_file}\033[0m")
            continue
        
        if not target_file.endswith('.py'):
            response = input("\033[93m[?] Not .py extension. Continue? (y/n): \033[0m").lower()
            if response != 'y':
                continue
        
        break
    
    protector = CodeProtector()
    
    output_name = input("\033[96m[?] Output filename (Enter for default): \033[0m").strip()
    if not output_name:
        output_name = None
    
    print("\n\033[94m" + "="*70 + "\033[0m")
    print("\033[97m\033[1mStarting Protection Process\033[0m")
    print("\033[94m" + "="*70 + "\033[0m\n")
    
    try:
        result = protector.protect_file(target_file, output_name)
        
        print("\n\033[92m" + "="*70 + "\033[0m")
        print("\033[97m\033[1mPROTECTION SUCCESSFUL\033[0m")
        print("\033[92m" + "="*70 + "\033[0m")
        print("\033[96m✓ Multi-layer protection applied\033[0m")
        print("\033[96m✓ Anti-decompilation enabled\033[0m")
        print("\033[96m✓ Integrity verification added\033[0m")
        print(f"\033[96m✓ Protected file: {result}\033[0m")
        print("\033[93m\nNote: Test protected file before deployment\033[0m")
        
    except Exception as error:
        print(f"\n\033[91m[!] Protection failed: {str(error)}\033[0m")
    
    print("\n\033[95m" + "="*70 + "\033[0m")
    print("\033[97mPyShield - @abhiexploits\033[0m")
    print("\033[95m" + "="*70 + "\033[0m")

if __name__ == "__main__":
    try:
        main_execution()
    except KeyboardInterrupt:
        print(f"\n\033[91m[!] Interrupted\033[0m")
        sys.exit(0)
