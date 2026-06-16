
'''
overwrites files with encrypted or decrypted text, using a Vigenere cypher

'''

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def encrypt(filePath, key):
    code(filePath, key, True)


def decrypt(filePath, key):
    code(filePath, key, False)


def code(filePath, key, encryptTrue):
    key = key.replace(" ", "")
    key = key.lower()
    if not key.isalpha():
        raise ValueError("key input contains non-alphabetic character(s)")
    
    keyIndexLimit = len(key) -1
    keyCurrentIndex = 0

    with open(filePath, "r", encoding="utf-8-sig", errors="ignore") as file:
        originalLines = file.readlines()
    
    translatedLines = []
    for line in originalLines:
        cursor = ""
        for char in line:
            if char.isalpha() and char.lower() in alphabet:
                alphabetIndex = alphabet.index(char.lower())  
                shiftAmount = alphabet.index(key[keyCurrentIndex])

                if not encryptTrue:
                    shiftAmount = 26 - shiftAmount

                targetIndex = (alphabetIndex + shiftAmount) % 26
                if char == char.lower():
                    cursor = cursor + alphabet[targetIndex]
                else:
                    cursor = cursor + alphabet[targetIndex].upper()
                keyCurrentIndex = keyCurrentIndex + 1 if keyCurrentIndex < keyIndexLimit else 0
            else:
                cursor = cursor + char
        translatedLines.append(cursor)  

    if len(originalLines) == len(translatedLines):
        with open(filePath, "w", encoding="utf-8-sig") as file:
            for line in translatedLines:
                file.write(line)
