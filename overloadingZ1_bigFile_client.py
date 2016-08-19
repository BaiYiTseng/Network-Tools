# p.049 TCP Server and Client That can Deadlock
# TCP client and server that leave too much data waiting

import socket, sys

serverIP = "APL8177"     # input("Please enter server IP you would like to connect to: ")
serverPort = int(input("Please enter application port number: "))
bytecount = 2**16     # int(input("Please enter up to how many bytes you will send to the server: "))
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Sending", bytecount, "bytes of data")
clientSock.connect((serverIP, serverPort))
f = open('overloadingZ1_Big_File_1.txt', 'r', encoding='utf-8')
count = 0
sent = 0

for line in f:
    clientSock.sendall(line.encode('utf-8', errors='ignore'))
    sent += len(line)
    count += 1
    if count%1000 == 0:
        print("\r %d bytes sent" % (sent,), end=" ")
    sys.stdout.flush()
print()
clientSock.shutdown(socket.SHUT_WR)

print("Receiving all the data the server sends back")
