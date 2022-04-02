#this swaps the values of the 16 bit block
def swapChar(twoBytes):
    string1 = twoBytes[0]
    string2 = twoBytes[1]
    newString = string2 + string1
    return newString

#function to encrypt the 16 bit block with the provided key
def des(twoBytes, key):
    return twoBytes[0] + chr(ord(twoBytes[1])^ord(key))

#itertator for swapping and encrypting
def encrypt(iArray, kArray):
    for i in range(8):
        for j in range(len(iArray)):
            iArray[j] = des(swapChar(iArray[j]), kArray[i])
    return iArray

#iterator for decrypting THEN swapping
def decrypt(iArray, kArray):
    for i in range(8):
        for j in range(len(iArray)):
            iArray[j] = swapChar(des(iArray[j], kArray[7-i]))
    return iArray

#writes to an output file.
def write(oArray, filename):
    f = open(filename, 'w+')
    for val in oArray:
        f.write(val)
    f.close()

