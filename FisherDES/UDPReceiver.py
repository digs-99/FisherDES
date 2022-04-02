import UDPHelper
import sys

inputArray = []
keyArray = []
outputArray = []
if (len(sys.argv) < 4):
    print("Invalid use of arguments. \nProper Use case for encrypt is \"python3 UDPSender.py input.txt source-ip destination-ip source-port output.txt 0\"\n")
    sys.exit(-1)
sourceIP = UDPHelper.ipSplit(sys.argv[1])
destIP = UDPHelper.ipSplit(sys.argv[2])
dgFilename = sys.argv[3]

#read DG file
try:
    inFile = open(dgFilename, "rb")
    inData = list(inFile.read())
    inFile.close()
except FileNotFoundError:
    print("Input File does not exist")

#calculate the checksum
checksum = 0x0000
inDataCheckSum = 0x0000

if checksum != inDataCheckSum:
    print("Checksum does not match up")
else:
    print("Datagram from source-address {} source-port {} to to dest-address {} dest-port {}; Length {} bytes.".format(inData[0]))


#write the contents to output file in BINARY
#try:
    #write the decrypted data here
#except:
    #print("An Error writing to the dg file occured")
    #sys.exit(-1)
