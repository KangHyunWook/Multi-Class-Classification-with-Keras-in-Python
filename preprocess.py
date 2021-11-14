import os
import cv2
import numpy as np

rootdir='./trainset'
    
def getAllFiles(root):
    allFilePath=[]
    items=os.listdir(root)
    for item in items:
        path=os.path.join(root,item)
        if os.path.isdir(path):
            allFilePath.extend(getAllFiles(path))
        else:
            allFilePath.append(path)
    return allFilePath
    
def getTrainData(allfilepath): #press tab
    trainX=[]
    trainY=[]
    for filepath in allfilepath:
        splits=filepath.split('\\')
        label=splits[1]
        trainY.append(label)
        img=cv2.imread(filepath)
        img=cv2.resize(img, (50, 50))
        trainX.append(img)
    
    #normalization scale: 0-1
    # trainX=trainX/255.0
    
    trainX=np.array(trainX)
    trainY=np.array(trainY)
    
    return trainX, trainY
 
















 