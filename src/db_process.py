if __name__=='__main__':
    for i in range(1,76):
        filename="C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\db\\{}.txt".format(i)
        filename1 = "C:\\Users\\LostPromise\\Desktop\\privacy policy\\{}.txt".format(i)
        with open(filename,mode='r+',encoding='utf-8') as f:
            context=f.readlines()
            result=[]

            for j in range(len(context)):
                if(context[j]!='\n'):
                    result.append(context[j])

            for k in range(len(result)):
                result[k]=result[k].lower()#lower

            result.sort(reverse=False)#sort

            result=list(set(result))#list

            with open("C:\\Users\\LostPromise\\Desktop\\stopwords.txt",mode='r+',encoding='utf-8') as f_stopwords:
                stopwords=f_stopwords.readlines()
                for it in stopwords:
                    for it2 in result:
                        if(it in it2):
                            result.remove(it2)
                with open(filename1,mode='a',encoding='utf-8') as f1:
                    f1.truncate(0)
                    for t in range(len(result)):
                        f1.write(result[t])
