directory = 'path/to/download/folder'

import os

# Method to sort an individual file into its respective folder
def sort(file):
    if '.' in file:
        pass
    else:
        return
    extension = file.split('.', -1)[-1]
    
    listOfFiles = os.listdir(directory)
    
    if extension in listOfFiles:
        pass
    else:
        os.mkdir(directory + '/' + extension)
        
    os.rename(directory + '/' + file, directory + '/' + extension + '/' + file)
    
# Put files in download folder into an array
files = os.listdir(directory)

# Iterate through each file and sort it
for i in files:
    sort(i)