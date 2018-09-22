import cv2
import sys
import os
sys.path.append(os.path.abspath("./"))
from src.haircolor import pixel_count


def test_top_pixel_count():
    filename = './data/hoshimiya.jpg'
    # 画像取得
    im = cv2.imread(filename)
    # 顔探索用の機械学習ファイルを取得
    cascade = cv2.CascadeClassifier("./lbpcascade_animeface.xml")
    # 顔探索(画像,縮小スケール,最低矩形数)
    face = cascade.detectMultiScale(im, 1.1, 3)
    for (x, y, w, h) in face:
        

    # 画像の切り抜き
    im_trim = im[y:y+h, x:x+w]
    height = len(im_trim[0])

    # 辞書を初期化
    color_freq = {}

    # 端っこを切り取るための変数を定義
    waru6height = int(height / 6)

    # 頻度を数えるための辞書を準備
    for color in im_trim.tolist():
        for c in color:
            cat = ''
            for rgb in c:
                cat += str(rgb)+":"
            color_freq[cat[0:-1]] = 0

    test = pixel_count(im_trim, color_freq, None, waru6height, None, None)
    for colors in im_trim[:waru6height].tolist():
        for color in colors:
            cat = ''
            for rgb in c:
                cat += str(rgb)+":"
            color_freq[cat[0:-1]] += 1
    assert(color_freq == test)

def test_left_pixel_count():
    # 頻度を数える(left)
    for color in im_trim[waru6height:, :waru10width].tolist():
        for c in color:
            cat = ''
            for rgb in c:
                cat += str(rgb)+":"
            color_freq[cat[0:-1]] += 1

def test_right_pixel_count():
    # 頻度を数える(right)
    for color in im_trim[waru6height:, -waru10width:].tolist():
      for c in color[0:waru15width]:
        cat = ''
        for rgb in c:
          cat += str(rgb)+":"
        color_freq[cat[0:-1]] += 1