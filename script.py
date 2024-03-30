import os
import cv2
import shutil
import imutils
import numpy as np
from people_count import main

protopath = "MobileNetSSD_deploy.prototxt"
modelpath = "MobileNetSSD_deploy.caffemodel"
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]



startPath = 'START'


new_file = "NEW FILE"

res = os.path.exists(new_file)
if(not res) :
    os.mkdir(new_file)

exclude_folders = ["$RECYCLE.BIN"] #Folders you want to exclude

def checkPath(path,new_file,exclude_folders) : 
    try:
        dir_list = os.listdir(path)
    except PermissionError as e:
        print(f"Permission error accessing {path}: {e}")
        return
    for i in dir_list : 
        filename = os.path.join(path,i)
        if(os.path.isdir(filename)):
            if i not in exclude_folders:
                checkPath(filename,new_file,exclude_folders)
        if(os.path.isfile(filename)):
            split_up = os.path.splitext(i)
            file_name = split_up[0]
            file_ext = split_up[1]

            # You can segregate other file extension too....

            if(file_ext == ".JPEG" or file_ext ==".png" or file_ext == ".JPG"):
                print(filename)
                try : 
                    count = main(filename)
                    new_dir = os.path.join(new_file,str(count))
                    if(not os.path.exists(new_dir)):
                        os.mkdir(new_dir)
                    shutil.copy(filename,new_dir)
                except Exception as e:
                    print(f"Permission error accessing {filename}: {e}")
            
            if(file_ext == ".pdf"):
                new_dir = os.path.join(new_file,"pdfs")
                if(not os.path.exists(new_dir)):
                        os.mkdir(new_dir)
                shutil.copy(filename,new_dir)
                

checkPath(startPath,new_file,exclude_folders)


