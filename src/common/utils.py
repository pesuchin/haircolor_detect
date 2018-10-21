from pathlib import Path
import cv2


def get_file_path(path):
    path_dir = Path(path)
    file_paths = path_dir.glob('**/*.jpg')
    return [str(file_path) for file_path in file_paths]

def sys_exit():
    import sys
    sys.exit()

def display_image(im_trim):
    cv2.imshow("Show Image", im_trim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()