from keras.models import Sequential, load_model
from keras.layers import Conv2D, Dense, Activation, MaxPooling2D, Flatten
from sys import exit

import os
import cv2
import numpy as np

rootdir='./trainset'

def CNN():
    model=Sequential()
    model.add(Conv2D(32, 5,5, input_shape=(50,50,3)))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (5,5)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D((2,2)))
    
    #fully connected layers
    model.add(Flatten())
    model.add(Dense(1000))
    model.add(Dense(2))
    model.add(Activation('softmax'))
    
    return model

def train(trainX, trainY, loss, opt):
    model=CNN()
    model.compile(loss=loss, optimizer=opt, metrics=['accuracy'])
    model.fit(trainX, trainY, epochs=15, batch_size=10)
    model.save('C:\prog\saved-model.h5')
    
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
    
def preprocess(allfilepath, labels): #press tab
    trainX=[]
    trainY=[]
    n_classes=len(labels)
    for filepath in allfilepath:
        splits=filepath.split('\\')
      
        label=splits[-2]
       
        ind=labels.index(label)
       
        y=np.zeros(n_classes)
        y[ind]=1
    
        trainY.append(y)
        img=cv2.imread(filepath)
        img=cv2.resize(img, (50, 50))
        trainX.append(img)
    
    #normalization scale: 0-1
    # trainX=trainX/255.0
    
    trainX=np.array(trainX)/255.
    trainY=np.array(trainY)
    
    return trainX, trainY
 
















 