from PIL import Image
import random

def mapping(source, seed):

    random.seed(seed)

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z", " ", ".", ",", "/"]

    image = Image.open(source)

    width = image.width
    height = image.height

    colors = []

    while len(colors) != len(alphabet):

        x = random.randrange(width)
        y = random.randrange(height)
        value = image.getpixel([x, y])

        if value[0] != value[1] and value[0] != value[2] and value[1] != value[2]:
            if value[0] not in colors and value[1] not in colors and value[2] not in colors:
                for i in range(0, 3):
                    colors.append(value[i])

    image.close()

    for i in range(len(colors)):
        colors[i] = str(colors[i])
        if len(colors[i]) == 2:
            colors[i] = "0" + str(colors[i])
        elif len(colors[i]) == 1:
            colors[i] = "00" + str(colors[i])

    # random.shuffle(alphabet)
    random.shuffle(colors)

    return alphabet, colors