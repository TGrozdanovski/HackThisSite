#Author TGrozdanovski

from colorama import init, Fore
import hashlib
import time

init(autoreset=True)  

encrypted = input('Enter Encrypted String: ')
print(Fore.YELLOW + "Please wait, decoding...\n")
time.sleep(1)  
elist = encrypted.split(' ')

characters = [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [str(i) for i in range(10)]
hex_chars = [chr(i) for i in range(ord('a'), ord('f') + 1)] + [str(i) for i in range(10)]

def Sum(hex_str):
    return sum(int(element, 16) for element in hex_str)

def MD5_Hash(string1):
    m = hashlib.md5()
    m.update(string1.encode('utf-8'))
    return m.hexdigest()

def SpecialChar(location):
    if location % 20 == 19:
        return "\n"
    elif location % 20 in {3, 7, 11, 15}:
        return "-"
    elif location % 20 == 8:
        return "O"
    elif location % 20 == 9:
        return "E"
    elif location % 20 == 10:
        return "M"
    elif location % 20 in {16, 18}:
        return "1"
    elif location % 20 == 17:
        return "."
    else:
        return "0"

def Total(str_guess, passhash_guess, previous, times_run):
    if times_run == 0:
        return ord(str_guess[0]) - int(elist[times_run]) + int(passhash_guess, 16)
    else:
        previous_hash = MD5_Hash(str(previous))
        return Sum(MD5_Hash(str_guess[:(times_run + 1)])[:16] + previous_hash[:16])

def Find_Possible():
    results = []
    for j in range(len(hex_chars)):
        for i in range(len(characters)):
            if (ord(characters[i]) + int(hex_chars[j], 16) - Total(characters[i], hex_chars[j], 0, 0)) == int(elist[0]):
                intTotal = Total(characters[i], hex_chars[j], Total(characters[i], hex_chars[j], 0, 0), 1)
                found = HashCalculate(characters[i], 1, str(hex_chars[j]), intTotal)
                if found != "0":
                    results.append(found)
    return results

def HashCalculate(char_guess, depth, hash_string, total):
    if depth > 99:
        return str(char_guess)
    elif depth > 31:
        if SpecialChar(depth) != "0":
            intTotal = Total(char_guess + SpecialChar(depth), hash_string[0:1], total, depth + 1)
            return HashCalculate(char_guess + SpecialChar(depth), depth + 1, hash_string, intTotal)
        else:
            for i in range(len(characters)):
                if (ord(characters[i]) + int(hash_string[(depth % 32):(depth % 32 + 1)], 16) - total) == int(elist[depth]):
                    intTotal = Total(char_guess + characters[i], hash_string[0:1], total, depth + 1)
                    found = HashCalculate(char_guess + characters[i], depth + 1, hash_string, intTotal)
                    if found != "0":
                        return found
        return "0"
    else:
        for j in range(len(hex_chars)):
            if SpecialChar(depth) != "0":
                if (ord(SpecialChar(depth)) + int(hex_chars[j], 16) - total) == int(elist[depth]):
                    intTotal = Total(char_guess + SpecialChar(depth), hash_string[0:1], total, depth + 1)
                    return HashCalculate(char_guess + SpecialChar(depth), depth + 1, hash_string + hex_chars[j], intTotal)
            else:
                for i in range(len(characters)):
                    if (ord(characters[i]) + int(hex_chars[j], 16) - total) == int(elist[depth]):
                        intTotal = Total(char_guess + characters[i], hash_string[0:1], total, depth + 1)
                        found = HashCalculate(char_guess + characters[i], depth + 1, hash_string + hex_chars[j], intTotal)
                        if found != "0":
                            return found
    return "0"

results = Find_Possible()

print("\n===================")
for result in results:
    print(Fore.YELLOW + "Found: ")
    print(Fore.GREEN + result)
print("===================")
