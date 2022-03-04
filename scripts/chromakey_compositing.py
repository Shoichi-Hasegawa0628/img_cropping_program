#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

class ChromakeyCompositing():
    def __init__(self):
        pass
        self.compositing()

    def compositing(self):
        fg_img = cv2.imread('/root/HSR/catkin_ws/src/img_cropping_program/sample/sample1.png')
        # cv2.imshow('img', fg_img)
        # cv2.waitKey(0)

        # HSV に変換する。
        hsv = cv2.cvtColor(fg_img, cv2.COLOR_BGR2HSV)

        # 2値化する。
        bin_img = ~cv2.inRange(hsv, (62, 100, 0), (79, 255, 255))

        # 輪郭抽出する。
        contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 面積が最大の輪郭を取得する
        contour = max(contours, key=lambda x: cv2.contourArea(x))

        # マスク画像を作成する。
        mask = np.zeros_like(bin_img)
        cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
        cv2.imshow("mask", mask)
        cv2.waitKey(0)

if __name__ == "__main__":
    chromakey = ChromakeyCompositing()
    pass
