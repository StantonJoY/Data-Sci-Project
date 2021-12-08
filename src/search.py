import os
import re
import ast
import sys
import astpretty
import shutil

def search(filepath):
    code = open(filepath, "r", encoding='utf-8').read()
    if (re.search("cloud", code) != None):
    # if (re.search(".py$", filepath) != None):
        print(filepath)

def getAllFile(filepath):
    # global filecnt
    pathDir = os.listdir(filepath)
    pathDir.sort()
    for file in pathDir: # 对于.py文件 在对应ast_目录中创建ast文件
        if (os.path.isfile(filepath + "/" + file) and re.match("ast_", file) != None):
                search(filepath + "/" + file)
        else:
            if (os.path.isdir(filepath + '/' + file)): # 递归遍历目录
                getAllFile(filepath + "/" + file)


if __name__ == '__main__':
    current_filepath = os.getcwd()
    ast_filepath = current_filepath + "/" + "ast_odoo-15.0"
    getAllFile(ast_filepath)
