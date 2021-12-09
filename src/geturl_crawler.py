from urllib import request
import bs4
import requests as requests

if __name__=='__main__':
    result=[]
    privacy_policy =input()#此处将百度搜索设置为显示50条搜索，并直接将网址输入即可
    req = request.Request(privacy_policy)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',)

    response = request.urlopen(req)
    content = response.read().decode('utf-8')


    soup = bs4.BeautifulSoup(content)
    linkElems = soup.select('h3 > a')
    for i in range(50):
        result.append(linkElems[i].get('href'))

    for i in range(50):
        target=result[i]
        req=requests.get(url=target)
        html=req.text
        bf= bs4.BeautifulSoup(html)
        texts=bf.find_all()
        filename="C:\\Users\\LostPromise\\Desktop\\privacy policy\\{}.txt".format(i)#此处将filename修改为想要存储结果的地址，i为txt文件名，多次爬取时为防止重复可以将i改为i+50*k,k为爬取次数

        with open(filename,mode='a',encoding='utf-8') as f:#格式化输出，去除所有html标记
            f.truncate(0)
            f.write(texts[0].text.replace('<p><span style=\"font-size: 14px; font-family: 宋体;\">','\n\n\t'))
