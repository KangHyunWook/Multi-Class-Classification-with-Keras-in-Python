#Programmer: HYUN WOOK KANG
#Date: 2021-Feb-5
#Description: This program predicts the given image.

import cv2
import os
import argparse
import matplotlib.pyplot as plt
from keras.models import load_model
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True)

labels = os.listdir("dataset") #a list of labels

args= vars(ap.parse_args())
print(args)
filename=args['image']
img = cv2.imread(filename)
orig = img.copy() #save original image

#normalize to the image that has been trained in the model
img=cv2.resize(img, (100,100))
img=img.reshape((1,)+img.shape)
img=img/255.0

print(img.shape)

#load the trained model
model = load_model('trained_model.h5')

#outputs the individual probability given by the trained model for the input image                 
predictions = model.predict(img)[0]

maxProb=predictions[0]
label=labels[0]

#finds out the label that has the highest probability
for i in range(1, len(predictions)):
    if predictions[i] > maxProb:
        maxProb = predictions[i]
        label=labels[i]


#labels with the correct name for the image detected by the model
label= "This is {} {:.2f}%".format(label, maxProb*100)
cv2.putText(orig, label, (20, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (128, 0, 0), 2)
     
cv2.imshow('image', orig)
cv2.waitKey(0)






