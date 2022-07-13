from PIL import Image, ImageOps
from regex import I 

image = Image.open('JohnLocke.jpg')
image = ImageOps.grayscale(image)
rgb = image.convert('RGB')

width, height = rgb.size

output = '' 

for i in range(height):
    output += '/n'
    for j in range(width):
        r, g, b = rgb.getpixel((j, i))
        if r in range(0,43) : output += '⚅'
        if r in range(43,86) : output += '⚄'
        if r in range(86,129) : output += '⚃'
        if r in range(129,172) : output += '⚂'
        if r in range(172,215) : output += '⚁'
        if r in range(215,258) : output += '⚀'


f = open("JohnLocke.txt", "w")
f.write(output)
f.close()