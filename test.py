import ast
import os
import sys

import astpretty

if __name__ == '__main__':
    filePath = os.getcwd()
    f = open(filePath + "/ast_test.py")
    original_code = f.read()
    f.close()
    ast_node = ast.parse(original_code, mode="exec")
    print(ast.dump(ast_node))
    astpretty.pprint(ast_node, show_offsets=False)

# standard_output = sys.stdout # 输出重定向到file中
# if os.path.exists(outputpath + "/" + "ast_" + file):
#     os.remove(outputpath + "/" + "ast_" + file)
# sys.stdout = open(outputpath + "/" + "ast_" + file, "w+")
# astpretty.pprint(ast_node)
# sys.stdout.close()
# sys.stdout = standard_output