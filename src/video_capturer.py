import cv2
import os
import copy
from PIL import Image
from torchvision import transforms
from torchvision.transforms import Compose


def check_dir(path):
    isExit = os.path.exists(path)
    if not isExit:
        os.mkdir(path)


def img_aug(img):
    pipeline = Compose([transforms.RandomHorizontalFlip(p=0.5),
                        transforms.ColorJitter(brightness=(0.6,1.0),)])
    orig_img = copy.deepcopy(img)
    aug_img = pipeline(img)
    return orig_img, aug_img


def vid_capture(path):
    vid_path = path
    cap = cv2.VideoCapture(vid_path)
    if (cap.isOpened() == False):
        print('Error while trying to read video. Please check path again')
    outputs_path = f"../outputs/{vid_path.split('/')[-1].split('.')[0]}"
    check_dir(outputs_path)
    frame_count = 0
    total_frame_count = int(cap.get(7))
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frame_count += 1
            print(frame_count, ' / ', total_frame_count)
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            # pil_image = pil_image.resize((270,270))
            org_img, aug_img = img_aug(pil_image)
            save_path = f"../outputs/{vid_path.split('/')[-1].split('.')[0]}/{vid_path.split('/')[-1].split('.')[0]}_{str(frame_count)}.jpg"
            aug_save_path = f"../outputs/{vid_path.split('/')[-1].split('.')[0]}/{vid_path.split('/')[-1].split('.')[0]}_aug_{str(frame_count)}.jpg"
            org_img.save(save_path)
            aug_img.save(aug_save_path)
        else:
            break

    cap.release()
    return True