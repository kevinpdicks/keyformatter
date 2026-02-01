#!/usr/bin/env python3
# Created by KPD

import sys
import re

def format_pem_key(key_string):
    """
    Format a PEM key by removing \n escape sequences and ensuring proper line breaks.
    """
    # Remove literal \n sequences
    key_string = key_string.replace('\\n', '\n')
    
    # Remove any extra whitespace
    key_string = key_string.strip()
    
    # Ensure proper line breaks (64 characters per line for base64 content)
    lines = key_string.split('\n')
    formatted_lines = []
    
    for line in lines:
        line = line.strip()
        if line:
            formatted_lines.append(line)
    
    return '\n'.join(formatted_lines)

def main():
    if len(sys.argv) > 1:
        # Read from file
        with open(sys.argv[1], 'r') as f:
            key_content = f.read()
    else:
        # Read from stdin
        print("Paste your key (press Ctrl+D when done):")
        key_content = sys.stdin.read()
    
    formatted_key = format_pem_key(key_content)
    print(formatted_key)

if __name__ == "__main__":
    main()