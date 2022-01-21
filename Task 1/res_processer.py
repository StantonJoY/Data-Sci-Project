import os

def processs():
    resFilepath = os.getcwd() + os.sep + "res.txt"
    res = open(resFilepath, encoding='utf-8', mode="r")
    result = res.read()
    res.close()
    resupd = open(os.getcwd() + os.sep + "res.txt", mode="w+")
    lst = result.split(os.linesep)
    for i in range(len(lst)): lst[i] = lst[i].lower()
    lst = list(set(lst))
    lst.sort()
    for word in lst:
        if word == "": continue
        resupd.write(word + os.linesep)
    resupd.close()