import pickle
from operator import itemgetter, attrgetter, methodcaller
fileName = '/home/roberto/Downloads/banner.p'

with open(fileName, 'rb') as f:
    x = pickle.load(f)

print(type(x))

i=0
h=0
for item in x:
    print('\t')
    #print(item)
    for j in item:
          #print(j[1],end="")
          for k in range(0,j[1]):
              print(j[0],end="")






