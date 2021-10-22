
import os.path

def check_file_exist(file):
    if os.path.isfile(file):
        return True
    else:
        return False

def check_dir_exist(dir):
    if os.path.isdir(dir):
        return True
    else:
        return False

