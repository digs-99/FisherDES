import sys

def ipSplit(address):
    splitIP = address.split('.')
    if len(splitIP) > 4:
        print("IP address error incorrect formatting\n")
        sys.exit(-1)
    else:
        return splitIP

def ToBits(ipList):
    output = []
    for octet in ipList:
        output.append(hex(int(octet.zfill(3))))
    return output
