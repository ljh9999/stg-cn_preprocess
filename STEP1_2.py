# STEP 1
# acquire the kinetics_train folder which contains all the frames in each video, and there are 14 videos in total.
import json
import glob
import random
import string
from tqdm import tqdm

def thread1(process_folder, label_name):
    global confidence1
    global coor1
    global multi_frame_dict1
    # step1: go through all the video folder
    for video_index, input in enumerate(i for i in range(1,14)):
        # 对一个视频重复300遍，扩大数据集规模
        for i in range(15):
            # 定义一个空字典，每个视频一个字典
            file_dict = {}
            video_name = ''.join(random.sample(string.ascii_letters + string.digits, 8)) + str(input) + ''.join(
                random.sample(string.ascii_letters + string.digits, 2))
            print("video_name: ", video_name)
            # 遍历每一帧
            # 因为input是1~12的数字，而我重命名了生成了json文件，所以这儿的input不一样


            for frame_index, frame in enumerate(glob.glob(process_folder + str(input) + "/*")):
                print("input_file_name: ", frame)
                with open(frame, 'r') as f:
                    s1 = json.load(f)
                    # 这样做有问题，会丢帧的
                    if len(s1['people']) == 0:
                        continue
                    people = s1['people'][0]
                    pose_keypoints_2d = people['pose_keypoints_2d']
                    print(pose_keypoints_2d)

                    for indx, data in enumerate(pose_keypoints_2d):
                        if indx % 3 == 0:
                            coor1.append(float('%.3f' % data))
                        if (indx - 1) % 3 == 0:
                            coor1.append(float('%.3f' % data))
                        if (indx - 2) % 3 == 0:
                            confidence1.append(float('%.3f' % data))

                    print("coor:", coor1)
                    print("confidence: ", confidence1)

                info_dict = {"pose": coor1, "score": confidence1}
                single_frame_dict = {"frame_index": frame_index + 1, "skeleton": [info_dict]}
                print("single_frame_dict:", single_frame_dict)
                multi_frame_dict1.append(single_frame_dict)
                coor1 = []
                confidence1 = []

            file_dict = {"data": multi_frame_dict1, "label": label_name, "label_index": 0}
            output = open("./kinetics_train/" + video_name + ".json", "w")
            json.dump(file_dict, output)

def thread2(process_folder, label_name):
    # step1: go through all the video folder
    global confidence2
    global coor2
    global multi_frame_dict2
    for input in tqdm(range(15,28)):
        # 定义一个空字典，每个视频一个字典
        # 对一个视频重复300遍，扩大数据集规模
        for i in range(30):
            file_dict = {}
            video_name = ''.join(random.sample(string.ascii_letters + string.digits, 5)) + 'A01' + ''.join(
                random.sample(string.ascii_letters + string.digits, 2))
            print("video_name: ", video_name)
            # 遍历每一帧
            # 因为input是1~12的数字，而我重命名了生成了json文件，所以这儿的input不一样

            for frame_index, frame in enumerate(glob.glob(process_folder + str(input) + "/*")):
                print("input_file_name: ", frame)
                # print("frame_index: ",frame_index)
                with open(frame, 'r') as f:
                    s1 = json.load(f)
                    # 这样做有问题，会丢帧的
                    if len(s1['people']) == 0:
                        continue
                    people = s1['people'][0]
                    pose_keypoints_2d = people['pose_keypoints_2d']
                    print(pose_keypoints_2d)

                    for indx, data in enumerate(pose_keypoints_2d):
                        if indx % 3 == 0:
                            coor2.append(float('%.3f' % data))
                        if (indx - 1) % 3 == 0:
                            coor2.append(float('%.3f' % data))
                        if (indx - 2) % 3 == 0:
                            confidence2.append(float('%.3f' % data))

                    print("coor:", coor2)
                    print("confidence: ", confidence2)

                info_dict = {"pose": coor2, "score": confidence2}
                single_frame_dict = {"frame_index": frame_index + 1, "skeleton": [info_dict]}
                print("single_frame_dict:", single_frame_dict)
                multi_frame_dict2.append(single_frame_dict)
                coor2 = []
                confidence2 = []

            file_dict = {"data": multi_frame_dict2, "label": label_name, "label_index": 1}
            output = open("./kinetics_train/" + video_name + ".json", "w")
            json.dump(file_dict, output)


if __name__ == "__main__":
    coor1 = []
    coor2 = []
    confidence1 = []
    confidence2 = []
    multi_frame_dict1 = []
    multi_frame_dict2 = []

    process_folder = "./STEP1/"

    thread2(process_folder, label_name="mopping")

'''
single frame format
    {
     "frame_index": frame_index, 
     "skeleton":
    [
    {"pose":  [x1, y1, x2, y2, ......], 
     "score": [c1, ......],
    }
    ]
    }
'''

'''
multi frame format

{single frame info}
'''

'''
"data": 
"label": "customized action name",
"label_index:" num
'''
