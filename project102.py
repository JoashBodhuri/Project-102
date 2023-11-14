import os
import shutil

from_dir = "C:/Users/maymo/Downloads"

to_dir = "C:/Users/maymo/Downloads/Storage"

listoffiles = os.listdir(from_dir)
print(listoffiles)

for filename in listoffiles:
    name,ext = os.path.splitext(filename)
    #print(name)
    #print(ext)
    if ext == "":
        continue
    if ext in[ ".txt", ".pdf", ".doc", ".docx"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "imagefiles"
        path3 = to_dir + "/" + "imagefiles" + "/" + filename
        if os.path.exists(path2):
            print("moving " , filename)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving " , filename)
            shutil.move(path1, path3)