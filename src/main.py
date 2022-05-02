import csv

import video_capturer as vc
import os_utils as utils
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

vid_paths = utils.get_paths('../inputs')
print(vid_paths)
processed = []
with open('csv_record/processed.csv') as csv_file:
    rows = csv.reader(csv_file)
    for row in rows:
        if len(row) != 0:
            processed.append(row[0])
        else:
            continue
for vid_path in vid_paths:
    vid_name = vid_path.split('/')[-1].split('.')[0]
    if vid_path not in processed:
        success = vc.vid_capture(vid_path)
        if success:
            with open('csv_record/processed.csv', 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([vid_name])
    else:
        print(f'{vid_name} already processed!')


print('VC Finished !')

#----------------------------------------------------------------

# print('Start preparing datasets !')
#
# class_dir_paths = utils.get_paths('../train')
# all_img_paths = utils.get_img_paths(class_dir_paths)
# all_images, all_labels = utils.img_to_array(all_img_paths)
# print('Dataset Prepared !')
# print(all_images.shape)
# print(all_labels.shape)
#
# with open('x_train.npy', 'wb') as f:
#     np.save(f, all_images)
# with open('y_train.npy', 'wb') as f:
#     np.save(f, all_labels)
#
# with open('x_train.npy', 'rb') as f:
#     x_train = np.load(f)
# with open('y_train.npy', 'rb') as f:
#     y_train = np.load(f)
# print(x_train.shape, type(x_train))
# print(y_train.shape, type(y_train))
# img = Image.fromarray(np.uint8(x_train[-1])).convert('RGB')
# label = y_train[-1]
# print(label)
# plt.imshow(img)
# plt.show()








