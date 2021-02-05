from keras import Sequential
from keras import regularizers
from keras.layers import Conv2D, MaxPooling2D, Activation, Dense, Dropout, Flatten

class CNN:
    def __init__(self, size, numOfLabels):
        self.model=None
        self.size=size
        self.numOfLabels=numOfLabels
    def build(self):   
        size = self.size
        model=Sequential()
        model.add(Conv2D(6, (5, 5), input_shape=(size, size, 3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2,2)))
        model.add(Conv2D(16, (3,3)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D((2,2)))
        model.add(Flatten())
        model.add(Dense(120))
        model.add(Activation('relu'))
        model.add(Dense(84))
        model.add(Activation('relu'))
        model.add(Dense(self.numOfLabels))
        model.add(Activation('softmax'))
        
        return model
        
        
        
        
        
        
        
        
        