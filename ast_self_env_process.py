import ast
import re
import os
res_ast_self_env_process='C:\\Users\\LostPromise\\Desktop\\Data-Sci-Project 1.1\\res_ast_self_env_process.txt'

def search(filepath):
    with open(res_ast_self_env_process,'a+',encoding='utf-8') as f1:#Warning! Please ensure that the file'res_ast_self_env_process.txt' is clear or doesn't exist before you run this program every time!. Otherwise,the program will write new content after the content already exists in the file'res_ast_self_env_process.txt'!
        with open(filepath,'r+',encoding='utf-8') as f:
            code=f.read()
            ast_root=ast.parse(code,mode='exec')
            for node in ast.walk(ast_root):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Subscript) and isinstance(node.func.value.value, ast.Attribute) and isinstance(node.func.value.value.value, ast.Name) and node.func.value.value.value.id== 'self' and node.func.value.value.attr== 'env':
                    if len(node.args)!=0:
                        f1.write(node.func.attr)
                        f1.write('\n')
                        f1.write(ast.unparse(node.args))
                        f1.write('\n')
                        f1.write('***************************************************************************************')
                        f1.write('\n')

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


if __name__=='__main__':
    targetFilepath = os.getcwd() + os.sep + "odoo-15.0"
    getAllFile(targetFilepath)
    print('finished!')

