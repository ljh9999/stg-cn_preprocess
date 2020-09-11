# STEP3
# DATASET extension
import os

def batchRenameFile(srcDir, dst_file):
    '''
    Parameters
    ----------
    srcDir : the source file absolute path
    dstDir : the destination file absolute path
    Returns : None
    -------
    '''
    filename = dst_file
    with open(filename, 'a') as file_object:
        file_object.write('{\n')

    for item_index, item in enumerate(os.listdir(srcDir)):
        item_name = item.split('.')[0]
        print("item_name:",item_name)

        #TODO 需要对这个json文件进行扩充操作，1.json————>1_001.json ~ 1_300.json

        if item_index < len(os.listdir(srcDir))-1:

            with open(filename, 'a') as file_object:
                file_object.write('    "' + item_name + '":{ \n')
                file_object.write('        "has_skeleton": true, \n')
                file_object.write('        "label": "cover_the_cloth",   \n')
                file_object.write('        "label_index": ' + str(0)  +  '\n')
                file_object.write('    }, \n')
        # the last frame is not end up with a common
        else:
            print("get here!!")
            with open(filename, 'a') as file_object:
                file_object.write('    "' + item_name + '":{ \n')
                file_object.write('        "has_skeleton": true, \n')
                file_object.write('        "label": "cover_the_cloth",   \n')
                file_object.write('        "label_index": ' + str(0)  +  '\n')
                file_object.write('    } \n')


    with open(filename, 'a') as file_object:
        file_object.write('}')


if __name__ == '__main__':
    src_path = './kinetics_val'
    dst_file = 'kinetics_val_label.json'
    batchRenameFile(src_path, dst_file)

