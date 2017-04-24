def count(x,r):
    #print('counting')
    if x == '1':
        r[int(x)] += 1
    elif x == '2':
        r[int(x)] += 1
    elif x == '3':
        r[int(x)] += 1
    return ''

def stamp(x,r):
   # print('printing')
    if r[int(x)]>0:
        s = str(r[int(x)])+x
        r[int(x)] = 0
        return s
    else:
        return ''


s='1'
it = 3
a=''
r = [0,0,0,0]
i=0;j=0
while i < it:
    print("iteratione: ",i)
    print(a)
    j=0
    if(i!=0):
        s = a
    else:
        pass
    while j < len(s):
        print("Stringa residua",s[j:])
        try:
            if (s[j] == s[j+1]) & (len(s)-j>1):
                 count(s[j],r)
                 j += 1
            else:
                 count(s[j],r)
                 a = a + stamp(s[j],r)
                 j += 1
        except IndexError:
            count(s[j], r)
            a = a + stamp(s[j], r)
            j += 1

    i += 1



print(a)
