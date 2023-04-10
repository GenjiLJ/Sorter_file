import os
import shutil
# Path
path = "D:\Tugas Akhir\Sorter\\facerecog_dataset_test"
parent = 'D:\Tugas Akhir\Sorter\\dataset'
dir_list = os.listdir(path)


#Make folder
def make_folder():
    for i in dir_list:
        if i.find('_1.jpg') != -1:
            name=i.replace('_1.jpg','')
            path_2 = os.path.join(parent,name)
            os.mkdir(path_2)

#Move file to folder
def move_folder():
    for i in dir_list:
        if i.find('_1.jpg') != -1:
            name=i.replace('_1.jpg','')
            src_folder = path + '\\' + i
            dest_folder = parent +'\\'+ name
            shutil.copy(src_folder,dest_folder)
            print('1')
        else :
            src_folder = path + '\\' + i
            dest_folder = parent +'\\'+ name
            shutil.copy(src_folder,dest_folder)
            print('2')
    
move_folder()
