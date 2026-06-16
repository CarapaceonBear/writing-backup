import FilePathFinder
import EncryptDecryptFile
import MakeBackups
import json
import os

with open(os.path.dirname(__file__) + "\\config.json", "r") as configFile:
    configData = json.load(configFile)

encryptionKey = configData.get("encryption_key")
backupFolderPath = configData.get("backup_folder")

#MakeBackups.run(backupFolderPath)

#filePathsList = FilePathFinder.run()
filePathsList = ["F:\\Actual Documents\\Writing\\novelWriter\\Indigo\\content\\8732746b7cbb4.nwd"]

for filePath in filePathsList:
    try:
        EncryptDecryptFile.encrypt(filePath, encryptionKey)
    except:
        print("Encryption failed for filePath: " + filePath)

print("Encryption complete")