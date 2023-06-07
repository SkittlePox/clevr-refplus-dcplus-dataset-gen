import json
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def str_to_biimg(imgstr):
    img=[]
    cur = 0
    for num in imgstr.strip().split(','):
        num = int(num)
        img += [cur] * num
        cur = 1 - cur
    return np.array(img)


with open('output/scenes/clevr_ref+_cogent_valA_scenes.json') as f:
    data = json.load(f)
    scenes = data['scenes']
    scenes = scenes[:1]

    for scene in scenes:
        # print(scene['obj_mask'])
        print(scene['image_filename'])
        # open the associated image and display it
        img = Image.open('output/images/valA/' + scene['image_filename'])
        # img.show()
        img = np.array(img.convert('RGB'))
        plt.imshow(img)
        plt.show()

        mask_pixel_num = 480*320
        gt_mask  = np.array([0]*mask_pixel_num)
        obj_mask = scene['obj_mask']

        one_obj = obj_mask['1']
        gt_mask |= str_to_biimg(one_obj)
        gt_mask = gt_mask.reshape((320,480)).astype(np.uint8)

        im_seg = img / 2 
        c2 = im_seg[:, :, 2]
        for ci in range(c2.shape[0]):
            for cj in range(c2.shape[1]):
                if gt_mask[ci][cj] :
                    im_seg[ci, cj, :] = (0, 0, 180)

        # Display as an image
        plt.imshow(im_seg)
        plt.show()

    