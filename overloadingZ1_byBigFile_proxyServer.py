# p.049 TCP Server and Client That can Deadlock - My Version, Server
# TCP client and server that leave too much data waiting

import socket, sys

serverIP = "APL8177"    # input("Please enter server IP or name: ")
serverPort = int(input("Please enter server application port: "))
bytecount = 2**16       # int(input("Please enter up to how many bytes the server would accept at a time: "))
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSock.bind((serverIP, serverPort))
serverSock.listen(1)
print("Listening at", serverSock.getsockname())
while True:
    f_01 = open('overloadingZ1_receivingBigFile.txt', 'a', encoding='utf-8')
    forClientSock, clientIPnPort = serverSock.accept()
    print("Processing up to %d bytes at a time from" % bytecount, clientIPnPort)
    n = 0
    while True:
        data = forClientSock.recv(bytecount)
        if not data:
            break      
        n += len(data)
        print("\r %d bytes processed so far" % (n,), end=" ")
        sys.stdout.flush()
    print()