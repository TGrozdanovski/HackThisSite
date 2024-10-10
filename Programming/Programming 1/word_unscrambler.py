# Author: #TGrozdanovski

from itertools import permutations
from colorama import init, Fore

init(autoreset=True)

def load_word_list(file_path):
    with open(file_path, 'r') as file:
        return set(word.strip() for word in file.readlines())

def unscramble(scrambled_words, word_list):
    unscrambled = []
    for scrambled in scrambled_words:
        found = False
        for p in permutations(scrambled):
            candidate = ''.join(p)
            if candidate in word_list:
                unscrambled.append(candidate)
                found = True
                break
        if not found:
            unscrambled.append(scrambled)
    return unscrambled

if __name__ == "__main__":
    word_list = load_word_list('wordlist.txt')
    
    print(Fore.BLUE + "Paste scrambled words (one per line). Press Enter after the last word:")
    scrambled_input = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            scrambled_input.append(line.strip())
        except EOFError:
            break
    
    unscrambled_words = unscramble(scrambled_input, word_list)
    answer = ','.join(unscrambled_words)
    print(Fore.GREEN + f"Answer: {answer}")
