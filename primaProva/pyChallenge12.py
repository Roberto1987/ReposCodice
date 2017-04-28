from PIL import Image
from pylab import *
imAdd = "/home/roberto/Downloads/"
imName ="evil1.jpg"

print("Opening" , imAdd+imName)
im = Image.open(imAdd+imName).convert("L")
print(im.format, im.size, im.mode)
imMatrix = im.load()
im.show()

imHeight = 480
imWidth = 640


k=0
while(k<1):
    test = np.zeros((imHeight, imWidth, 3), dtype=np.uint8)
    for i in range(0,imHeight):
         #print('\n')
         for j in range(0,imWidth):
             if (i+j)%5 == 0:
                 test[i, j] = imMatrix[j, i]
                 pass
             else:
                 # (255, 255, 255)
                 #test[i, j] = imMatrix[j, i]
                 pass
    imTest = Image.fromarray(test, 'RGB')
    imTest.show()
    k += 10






box = (400, 200, 420, 220)
region = im.crop(box)
#region.show()

cropMatrix = region.load()

for i in range(0,20):
    print("\n")
    for j in range(0,20):
        if j%2==0:
            print(cropMatrix[i,j], " ", end="")
