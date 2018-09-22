import cv2
import shutil
from utils import get_file_path, sys_exit
from image_processing import crip_image, face_detect
from predict_white_hair import predict_white_color


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
