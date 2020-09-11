# STEP3
# DATASET extension
import os
import shutil
import random
import string

def batchRenameFile(srcDir, dstDir):
    '''
    Parameters
    ----------
    srcDir : the source file absolute path
    dstDir : the destination file absolute path
    Returns : None
    -------
    '''
    filename = "kinetics_val_label.json"
    with open(filename, 'a') as file_object:
        file_object.write('{\n')
    # for loop the entire train dataset for 300 times.
    for i in range(300):

        # ran_str = ''.join(random.sample(string.ascii_letters + string.digits,11))
        # src_name = os.path.join(srcDir,'test.json')
        # dst_name = os.path.join(dstDir,ran_str + '.json')
        # shutil.copy(src_name,dst_name)

    #     if i <= 299:
    #         with open(filename, 'a') as file_object:
    #             file_object.write('    "' + ran_str + '":{ \n')
    #             file_object.write('        "has_skeleton": true, \n')
    #             file_object.write('        "label": "mopping",   \n')
    #             file_object.write('        "label_index": ' + str(0)  +  '\n')
    #             file_object.write('    }, \n')
    #     # the last video is not end up with a common
    #     else:
    #         with open(filename, 'a') as file_object:
    #             file_object.write('    "' + ran_str + '":{ \n')
    #             file_object.write('        "has_skeleton": true, \n')
    #             file_object.write('        "label": "mopping",   \n')
    #             file_object.write('        "label_index": ' + str(0)  +  '\n')
    #             file_object.write('    } \n')
    # with open(filename, 'a') as file_object:
    #     file_object.write('}')

if __name__ == '__main__':
    src_path = '.'
    dst_path = 'kinetics_val'
    batchRenameFile(src_path, dst_path)

