if __name__=='__main__':
    filename="C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\ERP privacy words.txt"#file you want to sort
    filename1="C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\ERP privacy words1.txt"#result file you want to store
    with open(filename,'r+',encoding='utf-8') as f:
        result=f.readlines()
        result.sort()
        with open(filename1,'a+',encoding='utf-8') as f1:
            f1.truncate(0)
            for words in result:
                f1.write(words)
