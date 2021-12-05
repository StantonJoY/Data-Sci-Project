import os
import re
import ast
import sys
import astpretty
import shutil

def check(filePath):
    fopen = open(filePath, 'r')
    for eachLine in fopen:

        if (re.search("bank", eachLine) != None): # need to change
            return True
    fopen.close()
    return False

def build(filePath, file, outputpath):
    f = open(filePath + "/" + file)
    original_code = f.read()
    f.close()
    ast_code = ast.parse(original_code, mode="exec")
    standard_output = sys.stdout # 输出重定向到file中
    if os.path.exists(outputpath + "/" + "ast_" + file):
        os.remove(outputpath + "/" + "ast_" + file)
    sys.stdout = open(outputpath + "/" + "ast_" + file, "w+")
    astpretty.pprint(ast_code)
    sys.stdout.close()
    sys.stdout = standard_output


def getAllFile(filepath, ast_filepath):
    # global filecnt
    flag = 0
    pathDir = os.listdir(filepath)
    pathDir.sort()
    for file in pathDir: # 对于.py文件 在对应ast_目录中创建ast文件
        if (os.path.isfile(filepath + "/" + file)):
            if (re.search(".py$", file) != None) and (file != "__init__.py") and (file != "__manifest__.py"):
                flag = 1
                build(filepath, file, ast_filepath)
        else:
            if (os.path.isdir(filepath + '/' + file)): # 递归遍历目录
                if os.path.exists(ast_filepath + "/" + "ast_" + file):
                    shutil.rmtree(ast_filepath + "/" + "ast_" + file)
                os.mkdir(ast_filepath + "/" + "ast_" + file)
                tmp = getAllFile(filepath + "/" + file, ast_filepath + '/' + "ast_" + file)
                if (tmp == 0):
                    os.rmdir(ast_filepath + "/" + "ast_" + file)
                else:
                    flag = 1

    return flag

if __name__ == '__main__':
    filepath = "/Users/hare/Desktop/odoo-15.0"
    current_filepath = os.getcwd()
    ast_filepath = current_filepath + "/" + "ast_odoo-15.0"
    if (os.path.exists(ast_filepath)):
        shutil.rmtree(ast_filepath)
    os.mkdir(ast_filepath)
    getAllFile(filepath, ast_filepath)
    # print(filecnt)
