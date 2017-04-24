# [1, 11, 21, 1211, 111221]

def count(x,r):
    #print('counting')
    if x == '1':
        r[int(x)] += 1
        print('count 1: ',  r[int(x)]  )
    elif x == '2':
        r[int(x)] += 1
        print('count 2: ', r[int(x)])
    elif x == '3':
        r[int(x)] += 1
        print('count 3: ', r[int(x)])
    return ''

def stamp(x,r):
    if r[int(x)]>0:
         s = str(r[int(x)])+x
         r[int(x)] = 0
         print("Stamp:", int(x))
         return s
    else:
         return ''


s='1'
it = 30
a=''
r = [0,0,0,0]
i=0;j=0
while i < it:
    print("\n iteratione: ",i)
    print(s)
    j=0
    a = ''

    while j < len(s):
        print(a)
        print(" Stringa residua",s[:j],"|",s[j:])

        if len(s)-j != 1:
            if (s[j] == s[j+1]) & (len(s)-j>1):
                 count(s[j],r)
                 print("a: ", a)
                 j += 1
            else:
                 count(s[j],r)
                 a = a + stamp(s[j],r)
                 print("a: ",a)
                 j += 1
        else:
            count(s[j], r)
            a = a + stamp(s[j], r)
            print("a: ", a)
            j += 1

    i += 1

    s = a
    print("Stampa prima della prox iter:",s)


print("\n\n Stringa finale:",s,":",a)
print("Lunghezza di a[",i,"]:",len(s))
#
# s = '1'
# it = 5
# a = ''
# r = [0, 0, 0, 0]
# i = 0;
# j = 0
# while i < it:
#     print("\n iteratione: ", i, "\n")
#     print(a)
#     j = 0
#     if (i != 0):
#         s = a
#     else:
#         pass
#     while j < len(s):
#         print(" Stringa residua", s[j:])
#         try:
#             if (s[j] == s[j + 1]) & (len(s) - j > 1):
#                 count(s[j], r)
#                 j += 2
#             else:
#                 count(s[j], r)
#                 a = a + stamp(s[j], r)
#                 j += 1
#         except IndexError:
#             count(s[j], r)
#             a = a + stamp(s[j], r)
#             j += 1
#
#     i += 1
