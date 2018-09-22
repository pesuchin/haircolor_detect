from pathlib import Path


def get_file_path(path):
    path_dir = Path(path)
    file_paths = path_dir.glob('**/*.jpg')
    return file_paths


def sys_exit():
    import sys
    sys.exit()
