from preprocess import *
from keras.layers import Conv2D, Dense, Activation, MaxPooling2D, Flatten
from keras.models import Sequential

labels=['cat', 'dog']

allfilepath=getAllFiles(rootdir)

trainX, trainY=getTrainData(allfilepath, labels)

print(trainX.shape)
print(trainY.shape)

#convolutional layers
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

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(trainX, trainY, epochs=15, batch_size=10)
model.save('C:\prog\saved-model.h5')