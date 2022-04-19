import os
from glob import glob
import cv2 as cv
import numpy as np


def crop_width(img):
    # wider than higher
    aspect = wh_aspect
    new_width = int(img.shape[0] * aspect)
    crop_pad = int((img.shape[1] - new_width) // 2)
    if crop_pad < 0:
        return crop_height(img)
    img = img[:, crop_pad:new_width+crop_pad]
    return img

def crop_height(img):
    aspect = 1 / wh_aspect
    new_height = int(img.shape[1] * aspect)
    crop_pad = int((img.shape[0] - new_height) // 2)
    if crop_pad < 0:
        return crop_width(img)
    img = img[crop_pad:new_height+crop_pad, :]
    return img


if __name__ == '__main__':

    root_folders = glob('./outcast/timelapse/cae*')
    
    for root in root_folders:
        
        paths = glob(os.path.join(root, 'frames', '*'))

        for path in paths:

            img = cv.imread(path)

            wh_aspect = 1.6
            max_height = 640
            max_width = int(max_height * wh_aspect)

            max_length = np.max(img.shape[:2])
            max_dim = np.argmax(img.shape[:2])

            if max_dim == 1:
                img = crop_width(img)
            else:
                img = crop_height(img)

            img = cv.resize(img, (max_width, max_height))

            # cv.imwrite(path, img)