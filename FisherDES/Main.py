import HelperDES
import sys

inputArray = []
keyArray = []
outputArray = []
if (len(sys.argv) < 5):
    print("Invalid use of arguments. \nProper Use case for encrypt is \"python3 main.py input.txt keys.txt output.txt 0\"\nProper Use case for decypt is \"python3 main.py input.txt keys.txt output.txt 1\"\n")
    sys.exit(-1)

#handle Input file data handling
try:
    f = open(sys.argv[1])
    EoF = False
    while not EoF:
        bitBlock = f.read(2)
        if len(bitBlock) == 0:
            #We have reached the EOF
            EoF = True
        elif (len(bitBlock) == 1):
            #if file size is not divizible by 2 pad the last 8 bit with ASCII BACKSPACE VALUE
            bitBlock = bitBlock + '\n'
            inputArray.append(bitBlock)
        else:
            inputArray.append(bitBlock)
except FileNotFoundError:
    print("Input File does not exist")
finally:
    f.close()

#Handle key file input
try:
    f = open(sys.argv[2])
    EoF = False
    while not EoF:
        bitBlock = f.read(1)
        if len(bitBlock) == 0:
            #We have reached the EOF
            EoF = True
        else:
            keyArray.append(bitBlock)
except FileNotFoundError:
    print("Input File does not exist")
finally:
    f.close()

#Handle Key File error handling
if(len(keyArray) < 8):
    print(keyArray)
    print("Invalid Keyfile")
    sys.exit(-1)


if(sys.argv[4] == '0'):
    OutputArray = HelperDES.encrypt(inputArray, keyArray)
    #assertArray = HelperDES.decrypt(inputArray, keyArray)
    #assert (inputArray == assertArray), "Encryption Failed"
elif(sys.argv[4] == '1'):
    OutputArray = HelperDES.decrypt(inputArray, keyArray)
    #assertArray = HelperDES.encrypt(inputArray, keyArray)
    #ssert (inputArray == assertArray), "Encryption Failed"
else:
    print(sys.argv[4])
    print("Error: Values for Encrypt is 0. Values for Decrypt is 1. No other values allowed.")

HelperDES.write(OutputArray, sys.argv[3])

