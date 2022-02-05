import numpy as np
labels=[0, 1, 2]

n_classes=len(labels)
print(n_classes)

oneHotLabels=[]
for label in labels:
    y=np.zeros(n_classes)
    y[labels.index(label)]=1
    oneHotLabels.append(y)
oneHotLabels=np.array(oneHotLabels)
print('labels ont hot encoded')
print(oneHotLabels)
    