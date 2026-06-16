import EncryptDecryptFile
import os

def test_encrypt():
    testInput = "this is a test, boy howdy am I testing right now"
    testKey = "test"
    expectedOutput = "mlal bw s mxwl, uhc zhphq tf M lxlxagz vazax fhp"

    testFilePath = os.path.dirname(__file__) + "\\testFile.txt"
    if os.path.exists(testFilePath):
        os.remove(testFilePath)
    testFile = open(testFilePath, "x")
    testFile.write(testInput)
    testFile.close()

    EncryptDecryptFile.encrypt(testFilePath, testKey)

    with open(testFilePath, "r", encoding="utf-8-sig") as file:
        outputTest = file.readlines()
        if outputTest[0] == expectedOutput:
            print("test_encrypt -- PASSED")
        else:
            print("test_encrypt -- FAILED")
    
    if os.path.exists(testFilePath):
        os.remove(testFilePath)
    

def test_encrypt_key_with_whitespace():
    testInput = "this is a test, boy howdy am I testing right now"
    testKey = "t e    st  "
    expectedOutput = "mlal bw s mxwl, uhc zhphq tf M lxlxagz vazax fhp"

    testFilePath = os.path.dirname(__file__) + "\\testFile.txt"
    if os.path.exists(testFilePath):
        os.remove(testFilePath)
    testFile = open(testFilePath, "x")
    testFile.write(testInput)
    testFile.close()

    EncryptDecryptFile.encrypt(testFilePath, testKey)

    with open(testFilePath, "r", encoding="utf-8-sig") as file:
        outputTest = file.readlines()
        if outputTest[0] == expectedOutput:
            print("test_encrypt_key_with_whitespace -- PASSED")  
        else:
            print("test_encrypt_key_with_whitespace -- FAILED") 
    
    if os.path.exists(testFilePath):
        os.remove(testFilePath)


def test_encrypt_key_with_symbol():
    testInput = "this is a test, boy howdy am I testing right now"
    testKey = "1test"

    testFilePath = os.path.dirname(__file__) + "\\testFile.txt"
    if os.path.exists(testFilePath):
        os.remove(testFilePath)
    testFile = open(testFilePath, "x")
    testFile.write(testInput)
    testFile.close()

    try:
        EncryptDecryptFile.encrypt(testFilePath, testKey)
    except:
        print("test_encrypt_key_with_symbol -- PASSED")

    if os.path.exists(testFilePath):
        os.remove(testFilePath)


def test_encrypt_multiline():
    testInput = ["this is a test,\n", " boy howdy am I testing right now"]
    testKey = "test"
    expectedOutput = ["mlal bw s mxwl,\n", " uhc zhphq tf M lxlxagz vazax fhp"]

    testFilePath = os.path.dirname(__file__) + "\\testFile.txt"
    if os.path.exists(testFilePath):
        os.remove(testFilePath)
    testFile = open(testFilePath, "x")
    for line in testInput:
        testFile.write(line)
    testFile.close()

    EncryptDecryptFile.encrypt(testFilePath, testKey)

    with open(testFilePath, "r", encoding="utf-8-sig") as file:
        outputTest = file.readlines()
        if outputTest == expectedOutput:
            print("test_encrypt_multiline -- PASSED")
        else:
            print("test_encrypt_multiline -- FAILED")
    
    if os.path.exists(testFilePath):
        os.remove(testFilePath)


def test_decrypt():
    testInput = "mlal bw s mxwl, uhc zhphq tf M lxlxagz vazax fhp"
    testKey = "test"
    expectedOutput = "this is a test, boy howdy am I testing right now"

    testFilePath = os.path.dirname(__file__) + "\\testFile.txt"
    if os.path.exists(testFilePath):
        os.remove(testFilePath)
    testFile = open(testFilePath, "x")
    testFile.write(testInput)
    testFile.close()

    EncryptDecryptFile.decrypt(testFilePath, testKey)

    with open(testFilePath, "r", encoding="utf-8-sig") as file:
        outputTest = file.readlines()
        if outputTest[0] == expectedOutput:
            print("test_decrypt -- PASSED")  
        else:
            print("test_decrypt -- FAILED") 
    
    if os.path.exists(testFilePath):
        os.remove(testFilePath)


def test_decrypt_multiline():
    testInput = ["mlal bw s mxwl,\n", " uhc zhphq tf M lxlxagz vazax fhp"]
    testKey = "test"
    expectedOutput = ["this is a test,\n", " boy howdy am I testing right now"]

    testFilePath = os.path.dirname(__file__) + "\\testFile.txt"
    if os.path.exists(testFilePath):
        os.remove(testFilePath)
    testFile = open(testFilePath, "x")
    for line in testInput:
        testFile.write(line)
    testFile.close()

    EncryptDecryptFile.decrypt(testFilePath, testKey)

    with open(testFilePath, "r", encoding="utf-8-sig") as file:
        outputTest = file.readlines()
        if outputTest == expectedOutput:
            print("test_decrypt_multiline -- PASSED")
        else:
            print("test_decrypt_multiline -- FAILED")
    
    if os.path.exists(testFilePath):
        os.remove(testFilePath)


test_encrypt()
test_encrypt_key_with_whitespace()
test_encrypt_key_with_symbol()
test_encrypt_multiline()
test_decrypt()
test_decrypt_multiline()
