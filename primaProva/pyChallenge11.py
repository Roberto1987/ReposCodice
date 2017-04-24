from PIL import Image

imAdd = "/home/roberto/Downloads/"
imName ="cave.jpg"

print("Opening" , imAdd+imName)

im = Image.open(imAdd+imName).convert("L")
print(im.format, im.size, im.mode)
imMatrix = im.load()
imHeight = 640
imWidth = 480

for i in range(0,imHeight-1):
    print('\n')
    for j in range(0,imWidth-1):
        print(imMatrix[i,j],end="")


im.close()