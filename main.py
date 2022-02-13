from preprocess import *
from sys import exit


labels=['cat', 'dog']
#[1 0]-cat
#[0 1]-dog

allfilepath=getAllFiles(rootdir)

#train(trainX, trainY, 'binary_crossentropy', 'adam')

model=load_model('C:\prog\saved-model.h5')

testImageFiles=getAllFiles(r'C:\prog\Multi-Class-Classification-with-Keras-in-Python-Lesson8\testset')

testX, testY=preprocess(testImageFiles, labels)

correct_count=0

for i in range(len(testX)):
    x=testX[i]
    x=np.expand_dims(x, axis=0)
    pred=model.predict(x)[0]
    pred_idx=pred.argmax()
    true_idx=testY[i].argmax()
    if pred_idx==true_idx:
        correct_count=correct_count+1
        
print('correct_count:',correct_count)        
print('acc:',correct_count/len(testX))

_, acc=model.evaluate(testX, testY)

print('acc: {:.2f}'.format(acc))