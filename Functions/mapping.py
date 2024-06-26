from PIL import Image
import random

def mapping(image_source, method):

    characters = ["A", "B", "C", "D", "E", 
                "F", "G", "H", "I", "J", 
                "K", "L", "M", "N", "O", 
                "P", "Q", "R", "S", "T", 
                "U", "V", "W", "X", "Y", 
                "Z", "a", "b", "c", "d", 
                "e", "f", "g", "h", "i", 
                "j", "k", "l", "m", "n", 
                "o", "p", "q", "r", "s", 
                "t", "u", "v", "w", "x", 
                "y", "z", "0", "1", "2", 
                "3", "4", "5", "6", "7", 
                "8", "9", "+", "/", "=", "|"]

    image = Image.open(image_source)

    width = image.width
    height = image.height

    colors = []

    while len(colors) != len(characters):

        x = random.randrange(width)
        y = random.randrange(height)
        value = image.getpixel([x, y])

        for i in value:
            if i not in colors:
                if len(colors) != len(characters):   
                    colors.append(i)
                else:
                    break

    image.close()

    for i in range(len(colors)):
        colors[i] = str(colors[i])
        if len(colors[i]) == 2:
            colors[i] = "0" + str(colors[i])
        elif len(colors[i]) == 1:
            colors[i] = "00" + str(colors[i])

    random.shuffle(characters)
    random.shuffle(colors)
    
    dictionary = {}

    if method == "encode":
        for j in range(len(characters)):
            dictionary[characters[j]] = colors[j]
    elif method == "decode":
        for j in range(len(colors)):
            dictionary[colors[j]] = characters[j]

    return dictionary