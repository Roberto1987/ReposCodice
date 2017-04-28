from PIL import Image

folderAdd = '/home/roberto/Downloads/'
name = 'oxygen.png'

im = Image.open(folderAdd+name)#conversione in greyscale
print(im.format, im.size, im.mode)
im.show()

# da 43 a 51
pngMatrix = im.load()

#striscia 608x9 pixel
list=[]
fix = 7

for j in range(0,89): #larghezza 6 pixel
    print('\n',j*fix,' \n')
    for i in range(44,45): #range pixel verticali 43-52
        list.append(pngMatrix[j*fix,i])
        print(pngMatrix[j*fix,i])




for i in list:
    print(chr(i[0]),end="")



im.close()