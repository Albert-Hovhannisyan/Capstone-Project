from PIL import Image
import random
import os

def mapping(image_source, seed):

    random.seed(seed)

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z", " ", ".", ",", "/"]

    image = Image.open(image_source)

    width = image.width
    height = image.height

    colors = []
    count = 0

    while len(colors) != len(alphabet):

        x = random.randrange(width)
        y = random.randrange(height)
        value = image.getpixel([x, y])

        for i in value:
            if i not in colors:
                if count != len(alphabet):   
                    colors.append(i)
                    count = count + 1
                else:
                    break

    image.close()

    os.remove(image_source)

    for i in range(len(colors)):
        colors[i] = str(colors[i])
        if len(colors[i]) == 2:
            colors[i] = "0" + str(colors[i])
        elif len(colors[i]) == 1:
            colors[i] = "00" + str(colors[i])

    random.shuffle(alphabet)
    random.shuffle(colors)

    return alphabet, colors