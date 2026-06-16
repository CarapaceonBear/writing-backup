import os
import shutil
import json
import argparse

'''
restores a specified backup, from given date (string format 2000-12-30)
eg .\RestoreBackups.py --date='2026-06-16'

'''

def run(backupDate):
    with open(os.path.dirname(__file__) + "\\config.json", "r") as configFile:
        configData = json.load(configFile)
    backupFolderPath = configData.get("backup_folder")

    restoreFolderPath = backupFolderPath + "\\" + backupDate
    parentFolderPath = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    for file in os.listdir(restoreFolderPath):
        if checkIsAFolder(file) and file != "Encrypter":
            if os.path.exists(parentFolderPath + "\\" + file):
                shutil.rmtree(parentFolderPath + "\\" + file)
            shutil.copytree(restoreFolderPath + "\\" + file, parentFolderPath + "\\" + file)


def checkIsAFolder(input):
    return len(input.split(".")) == 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", required=True, type=str)
    args = parser.parse_args()

    run(args.date)
