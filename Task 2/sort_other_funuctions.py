import os

filepath_acquire = os.getcwd() + os.sep + 'res_other_functions' + os.sep + 'res_acquire.txt'
filepath_delete = os.getcwd() + os.sep + 'res_other_functions' + os.sep + 'res_delete.txt'
filepath_process = os.getcwd() + os.sep + 'res_other_functions' + os.sep + 'res_process.txt'
filepath_public = os.getcwd() + os.sep + 'res_other_functions' + os.sep + 'res_public.txt'
filepath_save = os.getcwd() + os.sep + 'res_other_functions' + os.sep + 'res_save.txt'

filepath_acquire_sorted = os.getcwd() + os.sep + 'res_other_functions_sorted' + os.sep + 'res_acquire_sorted.txt'
filepath_delete_sorted = os.getcwd() + os.sep + 'res_other_functions_sorted' + os.sep + 'res_delete_sorted.txt'
filepath_process_sorted = os.getcwd() + os.sep + 'res_other_functions_sorted' + os.sep + 'res_process_sorted.txt'
filepath_public_sorted = os.getcwd() + os.sep + 'res_other_functions_sorted' + os.sep + 'res_public_sorted.txt'
filepath_save_sorted = os.getcwd() + os.sep + 'res_other_functions_sorted' + os.sep + 'res_save_sorted.txt'


def sort(filepath, targetfilepath):
    f1 = open(targetfilepath, 'a+', encoding='utf-8')
    f1.truncate(0)
    f = open(filepath, 'r+', encoding='utf-8')
    content = f.readlines()
    result = list(set(content))
    result.sort()
    for words in result:
        f1.write(words + '\n')


if __name__ == '__main__':
    sort(filepath_acquire, filepath_acquire_sorted)
    sort(filepath_delete, filepath_delete_sorted)
    sort(filepath_process, filepath_process_sorted)
    sort(filepath_public, filepath_public_sorted)
    sort(filepath_save, filepath_save_sorted)
