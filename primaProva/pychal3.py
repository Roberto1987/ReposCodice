import re

with open("/home/roberto/Downloads/pychal3.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
    i=0
    j=0
    for j in range(5,len(data)-3):
        if data[j].istitle()==False:
            if data[j-1].istitle() & data[j-2].istitle() & data[j-3].istitle() & (data[j-4].istitle()==False)& data[j+1].istitle() & data[j+2].istitle() & data[j+3].istitle() & (data[j+4].istitle() == False):
                print(data[j-4],data[j-3],data[j-2], data[j-1], data[j], data[j+1] , data[j+2],  data[j+3], data[j+4] )

    print(j)





