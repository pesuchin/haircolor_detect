import shutil


class FileProcessor(object):
    def __init__(self, result, filepath):
        self.result = result
        self.filepath = filepath

    def move_directory(self):
        if self.result:
            shutil.move(self.filepath, './output/white_hair/')
        else:
            shutil.move(self.filepath, './output/gomi/')
