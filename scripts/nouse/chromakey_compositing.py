#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 画像を読み込んで、グリーンバックの背景を透過させるプログラム

import os
import cv2
import numpy as np
from __init__ import *


class ChromakeyCompositing():
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

                rgb, mask = self.background_transparency(raw_img)
                self.save_data(self.folders[i], j, rgb, mask)

    def background_transparency(self, img):
    #def background_transparency(self):
        # 画像のリサイズ
        # img = cv2.imread("/root/HSR/catkin_ws/src/img_cropping_program/scripts/rgb_0.png")
        # mask = cv2.imread("/root/HSR/catkin_ws/src/img_cropping_program/scripts/mask_0.png")
        # mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

        height = img.shape[0]
        width = img.shape[1]
        img = cv2.resize(img, (int(width * 1.25), int(height * 1.25)))

        # ガンマ補正 (色相対比で色味が変化した画像を補正, 緑を強くした)
        b, g, r = cv2.split(img)  # B(青),G(緑),R(赤)チャンネルごとに分割
        gamma = 2
        look_up_table = np.zeros((256, 1), dtype=np.uint8)
        for i in range(256):
            look_up_table[i][0] = (i / 255) ** (1.0 / gamma) * 255
        g_lut = cv2.LUT(g, look_up_table)  # Gに対してルックアップテーブル適用
        img_merge = cv2.merge([b, g_lut, r])  # B,G,変換後Rをマージ

        # rgb = cv2.bitwise_and(img_merge, img_merge, mask=mask)
        # cv2.imshow("mask", rgb)
        # cv2.waitKey(0)


        # マスク画像を生成 (ガンマ補正する前の画像の方が作りやすいのでそれにする)
        ## HSVに変換
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        ## 2値化
        #bin_img = cv2.inRange(hsv, (60, 0, 0), (75, 255, 255)) # 全体に適用
        bin_img = cv2.inRange(hsv, (60, 0, 0), (90, 255, 255)) # doll分 (ガンマ補正前)
        ## 色反転
        ch_bin_img = cv2.bitwise_not(bin_img)
        ## 輪郭抽出
        contours, _ = cv2.findContours(ch_bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ## 面積が最大の輪郭を取得
        contour = max(contours, key=lambda x: cv2.contourArea(x))
        ## マスク画像を作成
        mask = np.zeros_like(ch_bin_img)
        cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)

        # クロマキー合成のために前景画像(物体画像)の背景を黒色にする処理
        ## 前景画像の背景を黒色化
        rgb = cv2.bitwise_and(img_merge, img_merge, mask=mask)
        #
        # # cv2.imshow("mask", img_merge)
        # # cv2.waitKey(0)

        return rgb, mask

    def save_data(self, folder_name, file_idx, rgb, mask):
        if not os.path.exists(PROCESSED_IMAGE_DATA + "/" + folder_name):
            os.makedirs(PROCESSED_IMAGE_DATA + "/" + folder_name)

        cv2.imwrite(PROCESSED_IMAGE_DATA + "/" + folder_name + "/rgb_{}.png".format(file_idx), rgb)
        cv2.imwrite(PROCESSED_IMAGE_DATA + "/" + folder_name + "/mask_{}.png".format(file_idx), mask)
        return


if __name__ == "__main__":
    chromakey = ChromakeyCompositing()
    #chromakey.background_transparency()
    chromakey.image_server()
    pass
