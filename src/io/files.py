import shutil


class FileProcessor(object):
    def __init__(self, result, filepath):
        self.result = result
        self.filepath = filepath

    def move_directory(self):
        if self.result:
            print(self.filepath, 'is white hair.')
            shutil.move(self.filepath, './output/white_hair/')
        else:
            print(self.filepath, 'is not white hair.')
            shutil.move(self.filepath, './output/gomi/')
