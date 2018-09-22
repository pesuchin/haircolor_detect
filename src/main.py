import cv2
import shutil
from utils import get_file_path, sys_exit
from image_processing import crip_image
from predict_white_hair import predict_white_color


def face_detect(filepath):
    print('open:', filepath)
    # 画像の読み込み
    im = cv2.imread(filepath)
    # 顔探索用の機械学習ファイルを取得
    cascade = cv2.CascadeClassifier("../lbpcascade_animeface.xml")
    # 顔探索(画像, 縮小スケール, 最低矩形数)
    faces = cascade.detectMultiScale(im, 1.1, 3)
    return faces


def move_dir(filepath):
    faces = face_detect(filepath)
    pre = []
    for (x, y, w, h) in faces:
        im_trim, width, height = crip_image(x, y, w, h, filepath)
        pre.append(predict_white_color(im_trim, width, height))
    print(pre)
    sys_exit()
    if len(pre) > 2 or len(pre) == 0:
        shutil.move(filepath, "./output/gomi/")
    elif True in pre:
        shutil.move(filepath, "./output/sirokami/")
    else:
        shutil.move(filepath, "./output/gomi/")


def main():
    filepaths = get_file_path('../images/')
    for filepath in filepaths:
        move_dir(str(filepath))


if __name__ == '__main__':
    main()
