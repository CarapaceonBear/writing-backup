import os

'''
returns a list of paths for all files in the parent folder (and subfolders) which have valid file extensions

'''

validFileExtensions = ["nwx", "nwd", "txt"]

def run():
    return(listTxtFilesInAllProjects(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))))


def printOutput():
    print(listTxtFilesInAllProjects(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))))
   

def listTxtFilesInAllProjects(mainFolder):
    fullFileList = []
    for fileName in os.listdir(mainFolder):
        if checkIsAFolder(fileName):
            intermediaryList = listTxtFilePathsInProjectFolder(mainFolder + "\\" + fileName)
            for txtFile in intermediaryList:
                fullFileList.append(txtFile)
    return fullFileList


def listTxtFilePathsInProjectFolder(folder):
    #STRUCTURE
    #-project folder
    #--content folder
    #---files.nwd
    #--meta folder
    #---files.json (these can be left alone)
    #--nwProject.nwx
    #--ToC.txt
    fileList = []
    for fileName in os.listdir(folder):
        if checkIsAFolder(fileName):
            subFolder = folder + "\\" + fileName
            for subFileName in os.listdir(subFolder):
                if checkIsTargetFiletype(subFileName):
                    fileList.append(subFolder + "\\" + subFileName)
        elif checkIsTargetFiletype(fileName):
            fileList.append(folder + "\\" + fileName)
    return fileList


def checkIsAFolder(input):
    return len(input.split(".")) == 1


def checkIsTargetFiletype(input):
    fileExtension = input.split(".")[-1]
    return fileExtension in validFileExtensions


run()