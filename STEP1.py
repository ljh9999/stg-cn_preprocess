# STEP 1
# acquire the kinetics_train folder which contains all the frames in each video, and there are 14 videos in total.
import json
import os
import glob
import pdb
import random
import string

coor = []
confidence = []
multi_frame_dict = []

video_path = os.listdir("output_cover_the_cloth")

# step1: go through all the video folder
for video_index, input in enumerate(video_path):
    # 定义一个空字典，每个视频一个字典
    file_dict = {}
    video_name = input
    print("video_name: ", video_name)
    # 遍历每一帧

    # 这样写有问题！！修改为字符串

    for frame_index, frame in enumerate(glob.glob("./output_cover_the_cloth/" + str(video_name) + "/*")):
        # 使用随机名，而且
        frame_name = ''.join(random.sample(string.ascii_letters + string.digits, 8)) + str(frame_index) + ''.join(
            random.sample(string.ascii_letters + string.digits, 2))
        print("input_file_name: ", frame_name)
        with open(frame_name, 'r') as f:
            s1 = json.load(f)
            # 这样做有问题，会丢帧的
            if len(s1['people']) == 0:
                print("wrong frame:", frame_index)
                pdb.set_trace()
                continue
            people = s1['people'][0]
            pose_keypoints_2d = people['pose_keypoints_2d']
            print(pose_keypoints_2d)

            for indx, data in enumerate(pose_keypoints_2d):
                if indx % 3 == 0:
                    coor.append(float('%.3f' % data))
                if (indx - 1) % 3 == 0:
                    coor.append(float('%.3f' % data))
                if (indx - 2) % 3 == 0:
                    confidence.append(float('%.3f' % data))

        print("coor:", coor)
        print("confidence: ", confidence)

        info_dict = {"pose": coor, "score": confidence}
        single_frame_dict = {"frame_index": frame_index + 1, "skeleton": [info_dict]}

        multi_frame_dict.append(single_frame_dict)
        coor = []
        confidence = []

    file_dict = {"data": multi_frame_dict, "label": "cover_the_cloth", "label_index": 0}
    output = open("./kinetics_train/" + input + ".json", "w")
    json.dump(file_dict, output)

# for frame_index, input in enumerate(input_list):
#     input_file = os.path.join("output/",input)
#     with open(input_file,'r') as f:
#         s1 = json.load(f)
#         if len(s1['people']) == 0:
#             continue
#         people = s1['people'][0]
#         pose_keypoints_2d = people['pose_keypoints_2d']
#         print(pose_keypoints_2d)
#         pdb.set_trace()
#         # read out the coordination and confidence
#
#
#         for indx, data in enumerate(pose_keypoints_2d):
#             if indx % 3 == 0:
#                 coor.append(float('%.3f' % data))
#             if (indx-1) % 3 == 0:
#                 coor.append(float('%.3f' % data))
#             if (indx - 2) % 3 == 0:
#                 confidence.append(float('%.3f' % data))

# print("coor:", coor)
# print("confidence: ", confidence)

# info_dict = {"pose":coor, "score":confidence}
# single_frame_dict = {"frame_index":frame_index+1, "skeleton":[info_dict]}
#
# multi_frame_dict.append(single_frame_dict)
# coor = []
# confidence = []

# file_dict = {"data":multi_frame_dict, "label":"mopping", "label_index":1}


# one video fraction corresponds to one json file
# output = open("./test.json", "w")
#
# json.dump(file_dict,output)

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
