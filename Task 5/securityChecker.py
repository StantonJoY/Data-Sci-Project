import os
import re
import ast


def check(line):
    if ("hashlib" in line) or ("hmac" in line) or ("b64encode" in line):
        return True
    return False


def search(filepath, file):
    global resFilepath
    f = open(filepath + os.sep + file, encoding='utf-8')
    code = f.read().split(os.linesep)
    f.close()

    res = open(resFilepath + os.sep + file, mode='w+', encoding='utf-8')
    for line in code:
        if (check(line)):
            res.write(line + os.linesep)
    # ast_root = ast.parse(code, mode="exec")
    # for node in ast.walk(ast_root):
    #     if (isinstance(node, ast.Call)):
    #         if (check(node) == True):
    #             res.write(ast.unparse(node) + os.linesep)
    #             res.write(filepath + os.linesep)
    #             res.write('lineno = ' + str(node.lineno) + os.linesep)
    #             res.write(os.linesep)
    #             break
    res.close()


def getAllFile(filepath):
    pathDir = os.listdir(filepath)
    pathDir.sort()

    for file in pathDir:
        if (os.path.isfile(filepath + os.sep + file)):
            search(filepath, file)
        else:
            if (os.path.isdir(filepath + os.sep + file)):  # 递归遍历目录
                getAllFile(filepath + os.sep + file)


if __name__ == '__main__':
    targetFilepath = os.getcwd() + os.sep + "res_other_functions_sorted"
    resFilepath = os.getcwd() + os.sep + "res"

    getAllFile(targetFilepath)
