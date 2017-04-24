
import zipfile
import time
import re
from string import ascii_uppercase

maketrans = str.maketrans

folderAdd = '/home/roberto/Downloads/'
zipAdd =folderAdd+'channel.zip'

extractDir = 'channelDir'
extractPath =  folderAdd+extractDir

myZip = zipfile.ZipFile(zipAdd,mode='r') #open the file
fileList = myZip.filelist

for i in range(0,len(fileList)):
    myZip.extract(member=fileList[i],path=extractPath)

istruzioni = open(extractPath+'/readme.txt',mode='r')
# istruzioniStr = istruzioni.read()
# print(istruzioniStr)
# time.sleep(0.5)

start = open(extractPath+'/90052.txt')
startView = start.read()
stringArray = startView.split()
print(startView)
time.sleep(0.5)
nextFile = stringArray[-1]

print(myZip.comment)
list =[];
while(True):
    thisFileName = extractPath+'/'+nextFile+'.txt'
    try:
        thisFile = open(thisFileName,mode='r')
        # print('Opening file '+nextFile)
        thisFileView = thisFile.read()
        stringArray = thisFileView.split()
        print(thisFileView)
        time.sleep(0.0)
        nextFile = stringArray[-1]
        list.append(nextFile)
    except FileNotFoundError:
        break

myZip.close()
print(list)


#a = b''
comments =''
for i in list:
       name = i+".txt"
       for j in fileList:
           if j.filename == name:
               comments = comments + str(j.comment,'utf-8')




print(comments)

#
# f = open('/home/roberto/Downloads/output', 'wb')
# f.write(a)
# f.close()
#
# print(comments)
# print('\n\n\n')
# cipher_map = maketrans(ascii_uppercase, ascii_uppercase[1:] + ascii_uppercase[:1])
# encrypted = comments.translate(cipher_map)
# for i in range(0,25):
#     encrypted = encrypted.translate(cipher_map)
# print(encrypted)