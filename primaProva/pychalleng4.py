import urllib.request
from urllib.parse import urlparse
import re

s='12345'
for i in range(1,450):
    with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+s) as url:
        s = url.read()
        print(s)
    s = str(s)

    s = ''.join(c for c in s if c.isdigit())
    if i==85:
        a = int(s)
        a = a/2
        s=str(a)
    if s == '82682':
        s = '63579'

    print(s,"iterazione numero:"+str(i))
