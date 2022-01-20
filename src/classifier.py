import spacy
import os
import NLP_process as proc


def data_Classify(data):
    nlp = spacy.load('en_core_web_lg')
    basePath = os.sep.join(['..', 'data', 'classes'])
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
    with open("../classifier.txt", 'a')as w:
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

list = proc.proc("../odoo full.txt", "../words.txt")
data = []
for x in list:
    if x not in data:
        data.append(x)
for x in data:
    data_Classify(x)
