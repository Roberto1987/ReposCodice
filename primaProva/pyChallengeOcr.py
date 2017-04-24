import re

with open("/home/roberto/Downloads/pychallenge.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
    s = re.sub('[^0-9a-zA-Z]+', '*', data)
    print(s)