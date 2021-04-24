from PIL import Image
from random import randint
import numpy as np
import json

high = (2**8) - 1
low = 0
#print(high, low)

myImage = Image.open("D:\\semester 6\\security in computing(64)\\image-encryption\\Image-Encryption-Based-on-Rubiks-Cube\\flower.jpg");
width, height = myImage.size
pixels = myImage.load()
print(pixels[0,0])
has_opac = len(pixels[0,0]) == 4

value = 1
image = [[value for x in range(width)] for y in range(height)]

for y in range(height):
    for x in range(width):
        if has_opac:
            r, g, b, a = pixels[x,y]
        else:
            r, g, b = pixels[x,y]
        #lum = 255-r # Reversed luminosity
        image[y][x] = r # Map values from range 0-255 to 0-1

Key_Row = []
Key_Col = []

for i in range(height):
    Key_Row.insert(i, randint(low, high))

for i in range(width):
    Key_Col.insert(i, randint(low, high))

for i in range(height):
    alpha = 0
    for j in range(width):
        alpha = ((alpha%2) + (image[i][j] % 2)) % 2
    if(alpha == 0):
        for k in range(Key_Row[i]):
            temp2 = image[i][width-1]
            for l in range(width-1, -1, -1):
                image[i][l] = image[i][l-1];
            image[i][0] = temp2;
    else:
        for k in range(Key_Row[i]):
            temp2 = image[i][0]
            for l in range(width-1):
                image[i][l] = image[i][l+1];
            image[i][width-1] = temp2;

for j in range(width):
    beta = 0
    for i in range(height):
        beta = ((beta%2) + (image[i][j] % 2)) % 2
    if(beta == 0):
        for k in range(Key_Col[j]):
            temp2 = image[height - 1][j]
            for l in range(height-1, -1, -1):
                image[l][j] = image[l-1][j];
            image[0][j] = temp2;
    else:
        for k in range(Key_Col[j]):
            temp2 = image[0][j]
            for l in range(height-1):
                image[l][j] = image[l+1][j];
            image[height-1][j] = temp2;            



for j in range(width):
    for i in range(height):
        if((i%2) !=0 ):
            image[i][j] = image[i][j]^Key_Col[j]
        else:
            image[i][j] = image[i][j]^Key_Col[width-1-j]


for i in range(height):
    for j in range(width):
        if((j%2) !=0 ):
            image[i][j] = image[i][j]^Key_Row[i]
        else:
            image[i][j] = image[i][j]^Key_Row[height-1-i]

image1 = np.image(image, dtype=np.uint8)
final_image = Image.fromimage(image1)
final_image.save('D:\\semester 6\\security in computing(64)\image-encryption\\Image-Encryption-Based-on-Rubiks-Cube\\flower-encrypted.png')


with open("Key_Row.txt", "w") as outfile:
    json.dump(Key_Row, outfile)

with open("Key_Col.txt", "w") as outfile:
    json.dump(Key_Col, outfile)    
