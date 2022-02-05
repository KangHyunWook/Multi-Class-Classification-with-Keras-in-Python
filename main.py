from preprocess import *

allfilepath=getAllFiles(rootdir)

trainX, trainY=getTrainData(allfilepath)

print(trainX.shape)
print(trainY.shape)