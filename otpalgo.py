# implementaation of One-time pad algorithm method 1

def stringEncryption (text, key):
    #initialize
    cipherText = ""
    
    #cyper array of any length for text and key pairing
    cipher = []
    for i in range(len(key)):
        cipher.append(ord(text[i]) - ord('A') + ord(key[i])- ord('A'))
        
    #convert the no.s into integers corressponding to the characters
    for i in range(len(key)):
        x = cipher[i] + ord('A')
        cipherText += chr(x)
        
    return cipherText


#method 2
#returning plain text 
def stringDecryption (s, key):
    
    plainText = ""
    
    #intialize an array for storin gdifference of correspondance
    plain = []
    
    for i in range(len(key)):
        plain.append(ord(s[i])- ord('A') - (ord(key[i])- ord('A')))
        
        
    # if difference is less than 0 add 26 then store in an array
    
    for i in range(len(key)):
        
        if (plain[i] < 0 ):
            plain[i] = plain[i] + 26
            
    #convert to corresponding char 
    
    for i in range (len(key)):
        x = plain[i] + ord('A')
        plainText += chr(x)
        
    return plainText

plainText = "Great"

key = "MONEY"

encryptedText =stringEncryption(plainText.upper(), key.upper()) 

print("Cipher Text -" + encryptedText)

print("Message - "+ stringDecryption(encryptedText, key.upper()))     