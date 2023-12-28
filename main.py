import os

def getExtension(file):
    pass

def sort(file, directory):
    if '.' in file:
        pass
    else:
        return
    extension = file.split('.', -1)[-1]
    
    listOfFiles = os.listdir(directory)
    
    if extension in listOfFiles:
        pass
    else:
        print(extension)
        os.mkdir(directory + '/' + extension)
        print("hehe")
        
    os.rename(directory + '/' + file, directory + '/' + extension + '/' + file)
    
# access download folder
directory = 'C:/Users/ramsh/Downloads'
files = os.listdir(directory)

# iterate through each file in folder
for i in files:
    sort(i, directory)

