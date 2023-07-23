#!/usr/bin/env python3
"""
Author: Jazmin Morales
Purpose: Resolver el ejercicio 1.1(b)
"""
# program can find the python3 in the machine on which its running
# Purpose: generative art

# `>>>` Advanced Python Mastery  

# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("Usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))
    
