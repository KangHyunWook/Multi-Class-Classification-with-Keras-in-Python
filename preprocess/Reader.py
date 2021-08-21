import os

class Reader:      
    def __init__(self):
        pass
    def getAllFiles(self, rootDir):
        allFilePath=[]
        items=os.listdir(rootDir)
        for item in items:
            path=os.path.join(rootDir, item)
            if os.path.isdir(path):
                allFilePath.extend(self.getAllFiles(path))
            else:
                allFilePath.append(path)
        return allFilePath
