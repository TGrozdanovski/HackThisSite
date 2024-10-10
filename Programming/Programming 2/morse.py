from PIL import Image
from colorama import init, Fore, Style

init()

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '.': '.-.-', ',': '--..--', '?': '..--..'
}

def decode_image_to_morse(image):
    white_pixel_indices = []
    ascii_values = []

    for index, pixel in enumerate(image.getdata()):
        if pixel == (255, 255, 255):
            white_pixel_indices.append(index)

    last_white_pixel = None
    for current_index in white_pixel_indices:
        ascii_value = current_index if last_white_pixel is None else current_index - last_white_pixel
        ascii_values.append(ascii_value)
        last_white_pixel = current_index

    characters = ''.join(chr(value) for value in ascii_values if 0 <= value < 256)
    return characters

def translate_morse_to_text(morse_code):
    decoded_message = []
    words = morse_code.split(' / ')
    
    for word in words:
        letters = word.split()
        decoded_word = ''.join(k for letter in letters for k, v in morse_dict.items() if v == letter)
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)

image_path = 'download.png'
image = Image.open(image_path).convert('RGB')
decoded_characters = decode_image_to_morse(image)

print(Fore.GREEN + f"Decoded Characters: {decoded_characters}" + Style.RESET_ALL)
morse_code = decoded_characters.replace('.', '.').replace('-', '-')
decoded_message = translate_morse_to_text(morse_code)
print(Fore.BLUE + f"Answer: {decoded_message}" + Style.RESET_ALL)

# Author: #TGrozdanovski
