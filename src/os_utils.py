import os
import numpy as np
from PIL import Image


def get_paths(base):
    paths = []
    with os.scandir(base) as entries:
        for entry in entries:
            paths.append(base + '/' + entry.name)
            pass
    return paths


def get_img_paths(img_dir_paths):
    img_paths = []
    for p in img_dir_paths:
        paths = get_paths(p)
        img_paths.append(paths)
    return img_paths


def img_to_array(img_paths):
    all_imgs = []
    all_labels = []
    for i in range(len(img_paths)):
        for j in range(len(img_paths[i])):
            img = np.asarray(Image.open(img_paths[i][j]))
            all_imgs.append(img)
            all_labels.append(i)
    all_imgs = np.array(all_imgs)
    all_labels = np.array(all_labels)
    return all_imgs, all_labels


