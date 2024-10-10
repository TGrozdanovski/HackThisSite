from colorama import init, Fore, Style
import pyperclip

init(autoreset=True)

def classify_numbers(input_string):
    sum_primes = 0
    sum_composites = 0
    
    for char in input_string:
        if char.isdigit():
            num = int(char)
            if num in {2, 3, 5, 7}:
                sum_primes += num
            elif num in {4, 6, 8, 9}:
                sum_composites += num

    product = sum_primes * sum_composites
    non_numeric_chars = []
    
    for char in input_string:
        if not char.isdigit() and len(non_numeric_chars) < 25:
            non_numeric_chars.append(chr(ord(char) + 1))

    answer = ''.join(non_numeric_chars) + str(product)
    return answer

input_string = input(Fore.GREEN + "Paste string: ")

result = classify_numbers(input_string)
print(Fore.RED + "======" * 5)
print(Fore.BLUE + "Answer: " + Fore.YELLOW + result)
print(Fore.RED + "======" * 5)

pyperclip.copy(result)
print(Fore.RED + "Your answer has been copied to clipboard. Go and paste it!")

# Author: #TGrozdanovski
