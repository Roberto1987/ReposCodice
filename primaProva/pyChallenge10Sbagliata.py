# [1, 11, 21, 1211, 111221]

# 2 -> 12
# 11 -> 21
# 1 -> 11


#Start
s = '1'
s = str(s)
i=0
a=[]
it = 25      # number of iteration
i=0;j=0       # iteration index
print(s)
print("Starting size of the string: ",len(s))
while i < it:
   print('\n \n')
   print('----------------------------')
   size=len(s)
   j=0
   print('STEP',i, 'Stringa: ',s)
   a.append(s)
   while j <= size-1:

      # print('CHAR', j,':' ,  s[j])
      # print('\t remaning string:' ,s[:j]+'|'+s[j:] )
       if  size-j == 1: #case when last only one character
       #    print("size -j:", size, "-" , j ,'=', size-j)
       #    print(size,j,size-j)
       #    print("\t \t Last char ",s[-1])
       #    print('1->11')
           tmp = s[-1].replace('1','11')
           s = s[:-1] + tmp
       #    print(s)
           j += 2
           size = len(s)
       else:
           if s[j:j + 1] == '2':
        #       print('2 -> 12')
               temp = s[j:j + 1].replace('2', '12')
               s = s[:j] + temp + s[j + 1:]
        #       print(s)
               j += 2
               size = len(s)
           else:
               if s[j:j+2] == '11':
         #          print('11 -> 21')
                   temp = s[j:j+2].replace('11','21')
                   s = s[:j]+temp +s[j+2:]
         #          print(s)
                   j += 2
                   size = len(s)
               else:

                       if s[j:j + 2] == '12':
          #                 print('1 -> 11')
                           temp = s[j:j + 2].replace('1', '11')
                           s = s[:j] + temp + s[j + 2:]
          #                 print(s)
                           j += 2
                           size = len(s)
                       else:
                           print('nothing')
                           print(size, j, size - j)
                           j=j+1
                           size = len(s)

   i += 1
   print('----------------------------')

print('STEP', i, 'S: ', s)

print(a)
#print(a)
for i in a:
    print(len(i))
print('lunghezza di a[',29,']:',len(a[29]))
print('lunghezza di a[',30,']:',len(a[30]))
print('lunghezza di a[',31,']:',len(a[31]))
#632152
#lunghezza di a[ 29 ]: 405512
#lunghezza di a[ 30 ]: 632152