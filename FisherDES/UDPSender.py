import UDPHelper
import sys

inputArray = []
keyArray = []
outputArray = []
if (len(sys.argv) < 7):
    print("Invalid use of arguments. \nProper Use case for encrypt is \"python3 UDPSender.py input.txt source-ip destination-ip source-port output.txt 0\"\n")
    sys.exit(-1)
iFilename = sys.argv[1]
sourceIP = UDPHelper.ipSplit(sys.argv[2])
destIP = UDPHelper.ipSplit(sys.argv[3])
sourcePort = [sys.argv[4]]
destPort = [sys.argv[5]]
dgFilename = sys.argv[6]


#convert IP address
sourceIPHeader = UDPHelper.ToBits(sourceIP)
destIPHeader = UDPHelper.ToBits(destIP)

#convert port numbers
sourceHeader = UDPHelper.ToBits(sourcePort)
destHeader = UDPHelper.ToBits(destPort)

#convert data to binary format
try:
    inFile = open(iFilename, "rb")
    inData = list(inFile.read())
    inFile.close()
except FileNotFoundError:
    print("Input File does not exist")

#calculate the length of the header plus the data
UDPLength = 8 + len(inData)

#calculate the checksum
checksum = 0x0000


#write the contents to output file in BINARY
try:
    oFile = open(dgFilename, "wb")
    oFile.write(bytes(str(sourceHeader[0]), "utf-8"))
    oFile.write(bytes(str(destHeader[0]), "utf-8"))
    oFile.write(bytes(str(UDPLength), "utf-8"))
    oFile.write(checksum)
    oFile.write(inData)
except:
    print("An Error writing to the dg file occured")
    sys.exit(-1)
