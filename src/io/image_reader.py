import cv2


class FacesInImageIterator(object):
    def __init__(self, paths):
        self.paths = paths
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.paths):
            raise StopIteration()
        path = self.paths[self.i]
        self.i += 1
        # 画像内の顔を全て検出
        faces, image = self.face_detect(path)
        return faces, image, path

    def face_detect(self, filepath):
        # 画像の読み込み
        im = cv2.imread(filepath)
        # 顔探索用の機械学習ファイルを取得
        cascade = cv2.CascadeClassifier("./lbpcascade_animeface.xml")
        # 顔探索(画像, 縮小スケール, 最低矩形数)
        faces = cascade.detectMultiScale(im, 1.1, 3)
        return faces, im
