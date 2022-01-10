if __name__=='__main__':
    with open("C:\\Users\\LostPromise\\Desktop\\test1.txt",mode="r+",encoding="utf-8") as f1:
        context_simple=f1.readlines()
        with open("C:\\Users\\LostPromise\\Desktop\\test.txt",mode="r+",encoding="utf-8") as f2:
            context=f2.readlines()
            for i in context_simple:
                for j in context:
                    if(i == j):
                        context.remove(j)
            with open("C:\\Users\\LostPromise\\Desktop\\result.txt",mode="r+",encoding="utf-8") as f3:
                f3.truncate(0)
                for i in range(0, len(context)):
                    f3.write(context[i])
