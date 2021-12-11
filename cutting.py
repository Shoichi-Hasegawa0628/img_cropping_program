from pathlib import Path
import cv2

import numpy as np
from PIL import Image
from tqdm import tqdm
from natsort import natsorted
if __name__ == '__main__':

    objects_dir = Path("./objects")
    for object_dir in tqdm(natsorted(objects_dir.iterdir())):
        rgb_dir = object_dir.joinpath("rgb")
        mask_dir = object_dir.joinpath("mask")
        rgbs = natsorted(rgb_dir.iterdir())
        masks = natsorted(mask_dir.iterdir())

        for rgb_path, mask_path in zip(rgbs, masks):
            rgb_image = Image.open(rgb_path)
            mask_image = Image.open(mask_path)
            composit_img = Image.new("RGBA", rgb_image.size, (0, 0, 0, 0))
            composit_img.paste(rgb_image, (0, 0), mask_image.split()[0])

            rgb_image = np.array(composit_img)
            mask_image = np.array(mask_image.convert("L"))

            bool_mask = mask_image > 0
            axis_0 = np.any(bool_mask, axis=0)
            axis_1 = np.any(bool_mask, axis=1)

            axis_0 = np.where(axis_0)[0][[0, -1]]
            axis_1 = np.where(axis_1)[0]

            min_x, max_x = axis_1[0], axis_1[-1]
            min_y, max_y = axis_0[0], axis_0[-1]


            Image.fromarray(rgb_image[min_x:max_x, min_y:max_y]).save(rgb_path)
            Image.fromarray(mask_image[min_x:max_x, min_y:max_y]).save(mask_path)
