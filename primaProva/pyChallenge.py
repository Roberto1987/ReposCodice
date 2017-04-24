from string import ascii_lowercase
try:
    # Python 2
    from string import maketrans
except ImportError:
    # Python 3 made maketrans a static method
    maketrans = str.maketrans
bigString ='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr' \
           'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
#bigString ='map.html'

cipher_map = maketrans(ascii_lowercase, ascii_lowercase[1:] + ascii_lowercase[:1])
encrypted = bigString.translate(cipher_map)
encrypted = encrypted.translate(cipher_map)
print(encrypted)

encText = ''