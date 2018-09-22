import cv2
import sys
import os
sys.path.append(os.path.abspath("../"))
from src.image_processing import crip_pixel_count, crip_image, face_detect


def test_top_pixel_count():
    filepath = './data/hoshimiya.jpg'
    faces = face_detect(filepath)

    # 辞書を初期化
    color_freq = {}

    for (x, y, w, h) in faces:
        im_trim, width, height = crip_image(x, y, w, h, filepath)

        # 端っこを切り取るための変数を定義
        waru6height = int(height / 6)

        # 頻度を数えるための辞書を準備
        for color in im_trim.tolist():
            for c in color:
                cat = ''
                for rgb in c:
                    cat += str(rgb)+":"
                color_freq[cat[0:-1]] = 0

        test = crip_pixel_count(im_trim, color_freq, 
                                None, waru6height, None, None)

        for colors in im_trim[:waru6height].tolist():
            for color in colors:
                cat = ''
                for rgb in c:
                    cat += str(rgb)+":"
                color_freq[cat[0:-1]] += 1

    assert(color_freq == test)


def test_left_pixel_count():
    filepath = './data/hoshimiya.jpg'
    faces = face_detect(filepath)

    # 辞書を初期化
    color_freq = {}

    for (x, y, w, h) in faces:
        im_trim, width, height = crip_image(x, y, w, h, filepath)

        # 頻度を数えるための辞書を準備
        for color in im_trim.tolist():
            for c in color:
                cat = ''
                for rgb in c:
                    cat += str(rgb)+":"
                color_freq[cat[0:-1]] = 0

        # 端っこを切り取るための変数を定義
        waru6height = int(height / 6)
        waru10width = int(width / 10)

        # 頻度を数える(left)
        test = crip_pixel_count(im_trim, color_freq, 
                                None, waru10width, waru6height, None)
        for color in im_trim[waru6height:, :waru10width].tolist():
            for c in color:
                cat = ''
                for rgb in c:
                    cat += str(rgb)+":"
                color_freq[cat[0:-1]] += 1
    assert(color_freq == test)


def test_right_pixel_count():
    filepath = './data/hoshimiya.jpg'
    faces = face_detect(filepath)

    # 辞書を初期化
    color_freq = {}

    for (x, y, w, h) in faces:
        im_trim, width, height = crip_image(x, y, w, h, filepath)

        # 頻度を数えるための辞書を準備
        for color in im_trim.tolist():
            for c in color:
                cat = ''
                for rgb in c:
                    cat += str(rgb)+":"
                color_freq[cat[0:-1]] = 0

        # 端っこを切り取るための変数を定義
        waru6height = int(height / 6)
        waru10width = int(width / 10)

        # 頻度を数える(left)
        test = crip_pixel_count(im_trim, color_freq, 
                                None, waru10width, waru6height, None)
        # 頻度を数える(right)
        for color in im_trim[waru6height:, -waru10width:].tolist():
            for c in color:
                cat = ''
                for rgb in c:
                    cat += str(rgb)+":"
                color_freq[cat[0:-1]] += 1
    assert(color_freq == test)