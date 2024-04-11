from PIL import Image
import numpy as np

# Flipped around so I can get the alphabet characer based on the morse symbol
morse_dict = {".-"    : 'A',   "-..."  : 'B',   "-.-."  : 'C',   "-.."   : 'D',
    "."     : 'E',   "..-."  : 'F',   "--."   : 'G',   "...."  : 'H',
    ".."    : 'I',   ".---"  : 'J',   "-.-"   : 'K',   ".-.."  : 'L',
    "--"    : 'M',   "-."    : 'N',   "---"   : 'O',   ".--."  : 'P',
    "--.-"  : 'Q',   ".-."   : 'R',   "..."   : 'S',   "-"     : 'T',
    "..-"   : 'U',   "...-"  : 'V',   ".--"   : 'W',   "-..-"  : 'X',
    "-.--"  : 'Y',   "--.."  : 'Z',   ".----" : '1',   "..---" : '2',
    "...--" : '3',   "....-" : '4',   "....." : '5',   "-...." : '6',
    "--..." : '7',   "---.." : '8',   "----." : '9',   "-----" : '0',
    '/': ' '}

# Convert an image to ascii characters based on specifications:
# pixels are numbered based on distance from top right pixel, e.g.
# 
# 1, 2, 3, 4, 5
# 6, 7, 8, 9, 10
# etc.
# 
# Characterers are discerned based on distance between "white" pixels, e.g.
# the first white pixel at location 65 would be ascii ('A'), the next at 
# location 131 would represent ascii code (131 - 65) = 66 ('B') etc.
# 
# This Cypher is taken from hackthissite
def image_to_ascii(image_file):
    try:
        im = Image.open(image_file)
    except FileExistsError:
        print("No image! Aborting.")
        exit()

    im = np.array(im).flatten()
    
    gap = 0
    text = ""

    for pixel in im:
        if pixel > 0:
            text += chr(gap)
            gap = 0
        gap += 1
            
    
    return text

# Convert ascii representation of morse code to english
# "." = dit
# "-" = dah
# " " = character separator
# "/" = word separator
def morse_code_to_text(morse):
    symbols = morse.split(" ")
    message = []

    for symbol in symbols:
        try:
            message.append(morse_dict[symbol])
        except KeyError:
            print(f"symbol {symbol} not in dictionary, skipping")
    
    return "".join(message)

# Based on an image file that is hiding morse code in an image, convert the image
# into text, then convert the text (in morse code) to alphabet characters 
if __name__ == "__main__":
    in_file = input("Select an image to decode: ")

    morse_code = image_to_ascii(in_file)
    print(f"Recovered morse code: {morse_code}")

    text = morse_code_to_text(morse_code)
    print(f"Recovered text: {text.lower()}")
