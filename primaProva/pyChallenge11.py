from PIL import Image
from pylab import *
imAdd = "/home/roberto/Downloads/"
imName ="cave.jpg"

print("Opening" , imAdd+imName)
im = Image.open(imAdd+imName)#.convert("L")
print(im.format, im.size, im.mode)
imMatrix = im.load()

imHeight = 480
imWidth = 640


test = np.zeros((imHeight, imWidth, 3), dtype=np.uint8)
for i in range(0,imHeight):
    #print('\n')
    for j in range(0,imWidth):
        if (j+i)%2 == 0:
            test[i,j] = imMatrix[j,i]
        else:
            pass

imTest = Image.fromarray(test, 'RGB')
imTest.show()
