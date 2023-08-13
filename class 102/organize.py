import os
import shutil
from_path="C:/Users/jiten/Downloads"
to_path="C:/Users/jiten/Desktop/class 102"
list_of_files=os.listdir(from_path)
print (list_of_files)
for file_name in list_of_files:
    name,extension =os.path.splitext(file_name)
    if extension ==' ':
        continue
    if extension in ['.gif', '.jpg']:
        path1=from_path+'/'+file_name
        path2=to_path+'/'+"image_files"
        path3=to_path+'/'+'image_files'+'/'+file_name
        if os.path.exists(path2):
            shutil.move(path1,path3) 
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
            




