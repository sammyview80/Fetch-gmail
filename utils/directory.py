import os
import shutil


def make_dir(dir, base_folder="testingFolder"):
        """This will make a directory here base_dir= Documents. dir= /home/sammyview80/Documents/collage/project/testingFolder.
        Make Director for all path after the base_dir. /collage/project/testingFolder
        Make director for: /collage
        Make director for: /collage/project
        Make director for: /collage/project/testingFolder
        """
        my_list = dir.split('/')
        try:
            index_of_base_dir = my_list.index(base_folder)
        except ValueError:
            print(base_folder, 'not in the list')
        folders = my_list[index_of_base_dir+1:]
        root_dir = '/'.join(my_list[:index_of_base_dir+1])
        new_folders_array = []
        for index, folder in enumerate(folders):
            if folder == '':
                continue
            a = '/'.join(folders[:index+1])
            check_dir(os.path.join(root_dir, a))

def check_dir(dir):
    """This will check if the directory is present or not. If not then it will create it."""
    try:
        os.listdir(dir)
    except FileNotFoundError as e:
        os.mkdir(dir)

def copy_file(source_file, destination_folder):
    """This will copy the file to the destination folder."""
    try:
        shutil.copy(source_file, destination_folder)
    except shutil.Error as e:
        print('File Already Exists in the destination folder.')

def move_file(source_file, destination_folder):
    """This will move the file to the destination folder."""
    try:
        shutil.move(source_file, destination_folder)
    except shutil.Error as e:
        print('File Already Exists in the destination folder.')