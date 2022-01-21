import os
import re
import ast


# 修改re.search中的内容搜索execute中的sql
def check(node):
    if (isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name)):
        if (node.func.value.id == 'hashlib' or node.func.value.id == 'hmac'):
            return True


def search(filepath):
    file = open(filepath, encoding='utf-8')
    code = file.read()
    file.close()
    ast_root = ast.parse(code, mode="exec")
    for node in ast.walk(ast_root):
        if (isinstance(node, ast.Call)):
            if (check(node) == True):
                res.write(ast.unparse(node) + os.linesep)
                res.write(filepath + os.linesep)
                res.write('lineno = ' + str(node.lineno) + os.linesep)
                res.write(os.linesep)
                break


def getAllFile(filepath):
    pathDir = os.listdir(filepath)
    pathDir.sort()

    for file in pathDir:
        if (os.path.isfile(filepath + os.sep + file)):
            if (re.search(".py$", file) != None) and (file != "__init__.py") and (file != "__manifest__.py"):
                # (filepath == "/Users/hare/Documents/GitHub/Data-Sci-Project/odoo-15.0/odoo/addons/base/models")
                search(filepath + os.sep + file)
        else:
            if (os.path.isdir(filepath + os.sep + file)):  # 递归遍历目录
                getAllFile(filepath + os.sep + file)


if __name__ == '__main__':
    targetFilepath = "../odoo-15.0"
    resFilepath = os.getcwd() + os.sep + "res.txt"

    res = open(resFilepath, encoding='utf-8', mode="w+")

    getAllFile(targetFilepath)
    res.close()
