import bz2
import re
import sys
import os
from colorama import init, Fore, Style

init()

f = open('corrupted.png.bz2', 'rb')
raw = f.read()
f.close()
split = re.split(b'\x0d\x0a', raw)
total = len(split)

def magic(stuff, honnan, mennyit):
    enyem = bytearray(stuff)
    if mennyit == 0:
        for i in range(honnan, total - 1):
            enyem += split[i]
            enyem.append(10)
        enyem += split[total - 1]
        f = open('fixed.png', 'wb')
        try:
            f.write(bz2.decompress(enyem))
            f.close()
            print(Fore.GREEN + "File uncorrupted: fixed.png" + Style.RESET_ALL)
            os.startfile('fixed.png')  
            sys.exit()
        except OSError:
            f.close()
    else:
        for i in range(honnan, total - mennyit):
            enyem += split[i]
            enyem.append(13)
            enyem.append(10)
            magic(enyem, i + 1, mennyit - 1)
            enyem.pop()
            enyem.pop()
            enyem.append(10)

for i in range(total + 1):
    magic(bytearray(), 0, i)

# Author: #TGrozdanovski
