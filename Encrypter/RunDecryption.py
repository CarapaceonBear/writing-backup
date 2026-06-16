import FilePathFinder
import EncryptDecryptFile
import json
import os

with open(os.path.dirname(__file__) + "\\config.json", "r") as configFile:
    configData = json.load(configFile)

encryptionKey = configData.get("encryption_key")

filePathsList = FilePathFinder.run()

for filePath in filePathsList:
    try:
        EncryptDecryptFile.decrypt(filePath, encryptionKey)
    except:
        print("Decryption failed for filePath: " + filePath)

print("Decryption complete")