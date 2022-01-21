import ast
import re
import os

res_other_functions = os.getcwd() + os.sep + 'res_other_functions.txt'
res_acquire=os.getcwd() + os.sep +'res_other_functions'+ os.sep + 'res_acquire.txt'
res_delete=os.getcwd() + os.sep +'res_other_functions'+ os.sep + 'res_delete.txt'
res_process=os.getcwd()+os.sep+'res_other_functions'+ os.sep + 'res_process.txt'
res_public=os.getcwd()+os.sep+'res_other_functions'+ os.sep + 'res_public.txt'
res_save=os.getcwd()+os.sep+'res_other_functions'+ os.sep + 'res_save.txt'

method_classes_acquire = os.getcwd() + os.sep + 'method_classes' + os.sep + 'acquire.txt'
method_classes_delete = os.getcwd() + os.sep + 'method_classes' + os.sep + 'delete.txt'
method_classes_processing = os.getcwd() + os.sep + 'method_classes' + os.sep + 'processing.txt'
method_classes_public = os.getcwd() + os.sep + 'method_classes' + os.sep + 'public.txt'
method_classes_save = os.getcwd() + os.sep + 'method_classes' + os.sep + 'save.txt'


def search(filepath, word):
    if word=='get' or word=='read' or word=='exist' or word=='reverse' or word=='search' or word=='list' or word=='lookup' or word=='load':
        f0 = open(res_acquire, 'a+', encoding='utf-8')
    elif word=='clean' or word=='unlink' or word=='delete' or word=='remove' or word=='discard':
        f0=open(res_delete, 'a+', encoding='utf-8')
    elif word=='to' or word=='preprocess' or word=='process' or word=='compute' or word=='append' or word=='insert' or word=='check' or word=='generate' or word=='set':
        f0=open(res_process, 'a+', encoding='utf-8')
    elif word=='js' or word=='json' or word=='css' or word=='xml' or word=='html' or word=='report' or word=='post' or word=='render' or word=='submit':
        f0=open(res_public, 'a+', encoding='utf-8')
    elif word=='save' or word=='create' or word=='write' or word=='replace':
        f0=open(res_save, 'a+', encoding='utf-8')
    else:
        return 0
    f = open(filepath, 'r+', encoding='utf-8')
    code = f.read()
    ast_root = ast.parse(code, mode='exec')
    for node in ast.walk(ast_root):
        if isinstance(node, ast.FunctionDef):
            for def_node in ast.walk(node):
                if isinstance(def_node, ast.Call) and isinstance(def_node.func, ast.Attribute) and isinstance(def_node.func.value, ast.Subscript) and isinstance(def_node.func.value.value, ast.Attribute) and isinstance(def_node.func.value.value.value, ast.Name) and def_node.func.value.value.value.id == 'self' and def_node.func.value.value.attr == 'env' and len(def_node.args) != 0:
                    for def_node1 in ast.walk(node):
                        if isinstance(def_node1, ast.Call) and re.search(word, ast.unparse(def_node1)):
                            f0.write(ast.unparse(def_node1)+'\n')
def getAllFile(filepath, word):
    pathDir = os.listdir(filepath)
    pathDir.sort()
    for file in pathDir:  # 对于.py文件 在对应ast_目录中创建ast文件
        if os.path.isfile(filepath + os.sep + file):
            if (re.search(".py$", file) is not None) and (file != "__init__.py") and (file != "__manifest__.py"):
                search(filepath + os.sep + file, word)
        else:
            if os.path.isdir(filepath + os.sep + file):  # 递归遍历目录
                getAllFile(filepath + os.sep + file, word)


def get_words(filepath):
    f = open(filepath, 'r+', encoding='utf-8')
    words = f.readlines()
    for i in range(len(words)):
        words[i] = words[i][0:len(words[i]) - 1]
    return words


if __name__ == '__main__':
    acquire_words = get_words(method_classes_acquire)
    delete_words = get_words(method_classes_delete)
    processing_words = get_words(method_classes_processing)
    public_words = get_words(method_classes_public)
    save_words = get_words(method_classes_save)

    targetFilepath = os.getcwd() + os.sep + "odoo-15.0"
    for word in acquire_words:
        getAllFile(targetFilepath, word)
    for word in delete_words:
        getAllFile(targetFilepath, word)
    for word in processing_words:
        getAllFile(targetFilepath, word)
    for word in public_words:
        getAllFile(targetFilepath, word)
    for word in save_words:
        getAllFile(targetFilepath, word)
    print('finished!')
