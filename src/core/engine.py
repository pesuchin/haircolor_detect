from src.common.utils import get_file_path
from src.io.image_reader import FacesInImageIterator
from src.image.predict_white_hair import PredictResultManager
from src.io.files import FileProcessor


class Engine(object):
    def __init__(self, args):
        filepaths = get_file_path(args.folder_path)
        self.debug = args.debug
        self.fiter = FacesInImageIterator(filepaths)

    def run(self):
        for faces, image, path in self.fiter:
            prm = self.predict(faces, image, self.debug)
            self.file_move(prm, path)

    @staticmethod
    def predict(faces, image, debug):
        prm = PredictResultManager(faces, image, debug)
        prm.send_face_to_predictor()
        return prm

    @staticmethod
    def file_move(prm, path):
        fp = FileProcessor(prm.get_final_result(), path)
        fp.move_directory()
