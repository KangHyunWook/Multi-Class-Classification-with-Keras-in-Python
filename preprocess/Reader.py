import os

class Reader:      
    def __init__(self):
        pass
    def getAllFiles(self, rootDir):
        entries = os.listdir(rootDir)
        allFiles=[]
        for entry in entries: 
            new_entry=os.path.join(rootDir, entry)
            if not os.path.isdir(new_entry):
                allFiles.append(new_entry)
            else:
                allFiles=allFiles+self.getAllFiles(os.path.join(new_entry))
        return allFiles  
