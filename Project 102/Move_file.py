import os
import shutil

from_dir='/Users/ahaana/Downloads'
to_dir='/Users/ahaana/Desktop/Document_files'
list_of_files=os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,ext = os.path.splitext(file)
    if (ext==""):
        continue
    if(ext=='.txt', '.dox', '.docx', '.pdf'):
        path1=from_dir+"/"+file
        path2=to_dir+"/"+"Document_files"
        path3=to_dir+"/"+"Document_files"+"/"+file
        if(os.path.exists(path2)):
            print("moving"+file+".....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file+".....")
            shutil.move(path1,path3)