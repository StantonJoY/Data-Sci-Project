if __name__=='__main__':
    filename=""#file you want to sort
    filename1=""#result file you want to store
    with open(filename,'r+',encoding='utf-8') as f:
        result=f.readlines()
        result.sort()
        with open(filename1,'a+',encoding='utf-8') as f1:
            f1.truncate(0)
            for words in result:
                f1.write(words)
