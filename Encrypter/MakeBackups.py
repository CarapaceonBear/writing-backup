import os
import shutil
import datetime

'''
makes backups of project folders: current parent folder -> dated folder in specified backup location

'''

def run(backupFolderPath):
    currentDate = datetime.date.today()
    currentDateString = f"{currentDate.strftime("%Y")}-{currentDate.strftime("%m")}-{currentDate.strftime("%d")}"
    
    parentFolderPath = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    newBackupFolderPath = backupFolderPath + "\\" + currentDateString
    os.mkdir(newBackupFolderPath)

    for file in os.listdir(parentFolderPath):
        if checkIsAFolder(file) and file != "Encrypter":
            shutil.copytree(parentFolderPath + "\\" + file, newBackupFolderPath + "\\" + file)


def checkIsAFolder(input):
    return len(input.split(".")) == 1
