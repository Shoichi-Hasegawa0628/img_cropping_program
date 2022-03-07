#!/usr/bin/env python
# -*- coding: utf-8 -*-
# パワポで透過した画像を読み込んで、マスク画像を生成するプログラム

import os
import cv2
import numpy as np
from __init__ import *


class MaskImageGenerator():
    def __init__(self):
        pass

    def image_server(self):
        tmp_folder = os.listdir(RAW_IMAGE_DATA)
        self.folders = [f for f in tmp_folder if os.path.isdir(os.path.join(RAW_IMAGE_DATA, f))]

        for i in range(len(self.folders)):
            files = os.listdir(RAW_IMAGE_DATA + "/" + self.folders[i])
            for j in range(len(files)):
                raw_img = cv2.imread(RAW_IMAGE_DATA + "/" +
                                     self.folders[i] + "/" +
                                     "rgb_{}.png".format(j))

                mask = self.mask_generator(raw_img)
                self.save_data(self.folders[i], j, raw_img, mask)

    def mask_generator(self, img):
        # グレースケール
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # 二値化
        # bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)[1] # 黒色以外の物体
        retval, bin_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY) # 黒色を含む物体
        ## 輪郭抽出
        contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ## 面積が最大の輪郭を取得
        contour = max(contours, key=lambda x: cv2.contourArea(x))

        ## マスク画像を作成
        mask = np.zeros_like(bin_img)
        cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
        # cv2.imshow("mask", mask)
        # cv2.waitKey(0)

        return mask

    def save_data(self, folder_name, file_idx, rgb, mask):
        if not os.path.exists(PROCESSED_IMAGE_DATA + "/" + folder_name):
            os.makedirs(PROCESSED_IMAGE_DATA + "/" + folder_name)

        cv2.imwrite(PROCESSED_IMAGE_DATA + "/" + folder_name + "/rgb_{}.png".format(file_idx), rgb)
        cv2.imwrite(PROCESSED_IMAGE_DATA + "/" + folder_name + "/mask_{}.png".format(file_idx), mask)
        return


if __name__ == "__main__":
    mask_generator = MaskImageGenerator()
    mask_generator.image_server()
    pass
