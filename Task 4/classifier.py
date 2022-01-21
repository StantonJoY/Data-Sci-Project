import spacy
import os

"""
@:param filePath 路径
@:param dataBase 隐私信息库
@:return （list） 包含的隐私信息
"""


def proc(filePath, dataBase):
    res = []
    pathDir = os.listdir(filePath)
    file = open(filePath + os.sep + pathDir[0], mode='r').read()
    doc = nlp(file)

    # 基础操作：与数据库匹配
    for chunk in doc.noun_chunks:
        word1 = nlp(chunk.text)
        with open(dataBase)as db:
            line = db.readline()
            while line:
                word2 = nlp(line)
                similarity = word1.similarity(word2)
                if similarity > 0.85:
                    res.append(chunk.text)
                    break
                line = db.readline()
    return res


def data_Classify(data):
    basePath = os.sep.join(['.', 'classes'])
    similarity = []
    for i in range(1, 8):
        max = 0.0
        doc1 = nlp(data)
        filePath = basePath + os.sep + str(i) + '.txt'
        with open(filePath, encoding='utf-8') as f:
            line = f.readline()
            while line:
                doc2 = nlp(line)
                if not doc2 == None:
                    tmp = doc1.similarity(doc2)
                if tmp > max:
                    max = tmp
                line = f.readline()
        similarity.append(max)
    with open(os.getcwd() + os.sep + "classRes.txt", 'a')as w:
        w.write(data + '\n')
        w.write(str(similarity) + '\n\n')


def data_Classify_avg(data):
    nlp = spacy.load('en_core_web_lg')
    basePath = os.sep.join(['..', 'data', 'classes'])
    similarity = []
    for i in range(1, 8):
        sum = 0.0
        cnt = 1
        doc1 = nlp(data)
        filePath = basePath + os.sep + str(i) + '.txt'
        with open(filePath, encoding='utf-8') as f:
            line = f.readline()
            while line:
                doc2 = nlp(line)
                tmp = doc1.similarity(doc2)
                sum += tmp
                line = f.readline()
                cnt += 1
        similarity.append(sum / cnt)
    # with open("../test2.txt", 'a')as w:
    #     w.write(data + '\n')
    #     w.write(str(similarity) + '\n\n')
    return similarity


# with open("../odoo words.txt")as odoo:
#     line = odoo.readline()
#     while line:
#         data_Classify(line)
#         line = odoo.readline()
if __name__ == '__main__':
    nlp = spacy.load('en_core_web_lg')
    inputfilepath = os.getcwd() + os.sep + "input"
    list = proc(inputfilepath, "../dictionary.txt")
    data = []
    for x in list:
        if x not in data:
            data.append(x)
    for x in data:
        data_Classify(x)
