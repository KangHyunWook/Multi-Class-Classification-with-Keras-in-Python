import os

class Reader:      
    def __init__(self):
        pass
    def getAllFiles(self, rootDir):
        allFilePath=[]
        items=os.listdir(root)
        for item in items:
            path=os.path.join(root, item)
            if os.path.isdir(path):
                allFilePath.extend(self.getAllFiles(path))
            else:
                allFilePath.append(path)
        return allFilePath
