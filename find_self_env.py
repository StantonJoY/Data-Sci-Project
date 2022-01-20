from src.search import search
import re
res='C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\res.txt'
res_update = 'C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\res_update.txt'
address_self_env='C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\address_self_env.txt'
res_env_self='C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project\\res_env.self[].txt'
temp=[]
def update_res():
    with open(res,"r+",encoding='utf-8') as f:
        with open(res_update,'a+',encoding='utf-8') as f1:
            f1.truncate(0)
            privacy_words=f.readlines()
            for words in privacy_words:
                new_word=''
                for i in range(len(words)):
                    if(words[i]!=' '):
                        new_word+=words[i]
                    else:
                        new_word+='_'
                f1.write(new_word)

def search_self_env():
    with open(res_env_self,'a+',encoding='utf-8') as f2:
        f2.truncate(0)
        with open(address_self_env,'r+',encoding='utf-8') as f:
        # with open(res_update,'r+',encoding='utf-8') as f1:
            # privacy_words=f1.readlines()
            addresses=f.readlines()
        for address in addresses:
            with open(address[0:len(address)-1],'r+',encoding='utf-8') as f3:
                contentOfAddress=f3.readlines()
                # for i in range(len(contentOfAddress)):
                #     if (re.search("def ", contentOfAddress[i])):
                #         temp.append(i + 1)
                # temp.append(10000000)
                for j in range(len(contentOfAddress)):
                    if(re.search(r"self.env\[(.*)].", contentOfAddress[j]) == None):
                        continue
                    else:
                        f2.write(contentOfAddress[j])
                #         for k in range(len(temp)):
                #             if(j>temp[k] and j<temp[k+1]):
                #                 for m in range(temp[k],min(temp[k+1],len(contentOfAddress)-1)):
                #                     for word in privacy_words:
                #                         if(re.search(word[0:len(word)-1],contentOfAddress[m])):
                #                             f2.write(address[0:len(address)-1])
                #                             f2.write(" ")
                #                             f2.write(str(m+1))
                #                             f2.write(" ")
                #                             f2.write(word)
                #                             f2.write("\n")
                # temp.clear()

if __name__=='__main__':
    search_self_env()




