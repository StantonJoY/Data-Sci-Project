import os
import re
import ast
import sys
import astpretty
import shutil

def search(filepath):
    code = open(filepath, "r", encoding='utf-8').read()
    if (re.search("def execute", code) != None):
        print(filepath)

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

if __name__ == '__main__':
    current_filepath = os.getcwd()
    filepath = "/Users/hare/Documents/GitHub/Data-Sci-Project/" + "odoo-15.0"
    getAllFile(filepath)
