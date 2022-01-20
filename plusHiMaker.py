import os
import shutil

def getListOfFiles(dir):
    listOfFiles = os.listdir(dir)
    allFiles = list()

    for file in listOfFiles:
        pathName = os.path.join(dir, file)
        if os.path.isdir(pathName):
            allFiles = allFiles + getListOfFiles(pathName)
        else:
            allFiles.append(pathName)
        
    return allFiles

def addPlusHi():
    currentPath = os.path.dirname(os.path.realpath(__file__))
    files = getListOfFiles(currentPath)
    i = 0

    for file in files:
        if file.endswith('+hi.ytd'): continue
        if file.endswith('.ytd'):
            filePath = file.rsplit(".ytd", 1)
            if os.path.exists(filePath[0] + '+hi.ytd'): 
                print(f"{filePath[0]}+hi.ytd exists -- skipping\n")
                continue
            else:
                newFile = filePath[0] + '+hi.ytd'
                shutil.copy(file, newFile)
                i = i + 1
    
    return i


def main():
    _addPlusHi = addPlusHi()
    print(f'Created {_addPlusHi} new files')

if __name__ == '__main__':
    main()
