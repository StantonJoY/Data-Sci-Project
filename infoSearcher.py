import os
import re
import sys
import spacy
from spacy.matcher import Matcher
import ast
import shutil
import res_processer
min_similarity = 0.82
hashset = []


def check(varName):
    global doc1
    global res
    varname = " ".join(re.split("[^A-Za-z0-9]", varName))
    docVar = nlp(varname)
    for doc in doc1:
        if (doc.similarity(docVar) >= min_similarity):
            res.write(varname.strip() + os.linesep)
            break


def search(filepath):
    file = open(filepath, encoding='utf-8')
    code = file.read()
    file.close()
    ast_root = ast.parse(code, mode="exec")
    for node in ast.walk(ast_root):
        if (isinstance(node, ast.Name)):
            if (node.id in hashset): continue
            hashset.append(node.id)
            check(node.id)


def getAllFile(filepath):
    pathDir = os.listdir(filepath)
    pathDir.sort()

    for file in pathDir:  # 对于.py文件 在对应ast_目录中创建ast文件
        if (os.path.isfile(filepath + os.sep + file)):
            if (re.search(".py$", file) != None) and (file != "__init__.py") and (file != "__manifest__.py"):
                search(filepath + os.sep + file)
        else:
            if (os.path.isdir(filepath + os.sep + file)):  # 递归遍历目录
                getAllFile(filepath + os.sep + file)


# def process():
#     resFilepath = os.getcwd() + os.sep + "res.txt"
#     res = open(resFilepath, encoding='utf-8', mode="r")
#     result = res.read()
#     res.close()
#     resupd = open(os.getcwd() + os.sep + "res.txt", mode="w+")
#     lst = result.split(os.linesep)
#     for i in range(len(lst)): lst[i] = lst[i].lower()
#     lst = list(set(lst))
#     lst.sort()
#     for word in lst:
#         if word == "": continue
#         resupd.write(word + os.linesep)
#     resupd.close()
#



if __name__ == '__main__':
    nlp = spacy.load("en_core_web_lg")
    targetFilepath = os.getcwd() + os.sep + "odoo-15.0"
    resFilepath = os.getcwd() + os.sep + "res.txt"
    dictFilepath = os.getcwd() + os.sep + "dictionary.txt"

    # 获取词典
    dictionary = open(dictFilepath, encoding='utf-8')
    dictwords = dictionary.read()
    words = dictwords.split(os.linesep)
    doc1 = [nlp(word) for word in words]

    res = open(resFilepath, encoding='utf-8', mode="w+")

    # init matcher
    # matcher = Matcher(nlp.vocab)
    # pattern = [{'POS': 'ADJ', 'OP': '*'}, {'POS': 'NOUN', 'OP': '+'}]
    # matcher.add("var", [pattern])
    getAllFile(targetFilepath)
    res.close()
    res_processer.processs()
