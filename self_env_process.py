import re
count=0
self_env='C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\res_env.self[].txt'
res_self_env_process='C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\res_self_env_process.txt'
def line_process(line):
    searchObj=re.search(r'(.*)self.env\[(.*)].(.*)\(',line)
    if(searchObj==None):
        searchObj=re.search(r'(.*)self.env\[(.*)].(.*)',line)
    return searchObj.group(2)+'      '+searchObj.group(3)+'\n'

if __name__=='__main__':
    with open(res_self_env_process,'a+',encoding='utf-8') as f1:
        f1.truncate(0)
        with open(self_env,'r+',encoding='utf-8') as f2:
            lines=f2.readlines()
            for line in lines:
                count+=1
                res_line=line_process(line)
                f1.write(res_line)
                print(count)


