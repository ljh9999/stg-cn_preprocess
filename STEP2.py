# STEP3
# DATASET extension
import os
import pdb

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

        item_class = item.split('.')[0][6:8]
        print("class:", item_class)

        item_name = item.split('.')[0]
        if item_index < len(os.listdir(srcDir))-1:
            with open(filename, 'a') as file_object:
                file_object.write('    "' + item_name + '":{ \n')
                file_object.write('        "has_skeleton": true, \n')

                if item_class == '01':
                    print("class_name: mopping")
                    file_object.write('        "label": "mopping",   \n')
                    file_object.write('        "label_index": ' + str(1) + '\n')

                if item_class == '00':
                    print("class_name: cover_the_cloth")
                    file_object.write('        "label": "cover_the_cloth",   \n')
                    file_object.write('        "label_index": ' + str(0) + '\n')

                file_object.write('    }, \n')
        # the last frame is not end up with a common
        else:
            print("get here!!")
            with open(filename, 'a') as file_object:
                file_object.write('    "' + item_name + '":{ \n')
                file_object.write('        "has_skeleton": true, \n')

                if item_class == '01':
                    print("class_name: mopping")
                    file_object.write('        "label": "mopping",   \n')
                    file_object.write('        "label_index": ' + str(1) + '\n')

                if item_class == '00':
                    print("class_name: cover_the_cloth")
                    file_object.write('        "label": "cover_the_cloth",   \n')
                    file_object.write('        "label_index": ' + str(0) + '\n')

                file_object.write('    } \n')


    with open(filename, 'a') as file_object:
        file_object.write('}')


if __name__ == '__main__':
    src_path = './kinetics_train'
    dst_file = 'kinetics_train_label.json'
    batchRenameFile(src_path, dst_file)
