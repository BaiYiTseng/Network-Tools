# Monitoring TCP Telnet connection, server

import socket, sys

serverIP = "APL8177"    # input("Please enter server IP or name: ")
serverPort = int(input("Please enter server application port: "))
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSock.bind((serverIP, serverPort))
serverSock.listen(1)
print("Listening at", serverSock.getsockname())
while True:
    forClientSock, clientIPnPort = serverSock.accept()
    n = 0
    # while True:
    #     data = forClientSock.recv(bytecount)
    #     output += data
    #     if not data:
    #         break      
    #     n += len(data)
    #     print("\r %d bytes processed so far" % (n,), end=" ")
    #     sys.stdout.flush()
    # print()
    # while True:
    #     output = output.decode('ascii').upper().encode('ascii')
    #     forClientSock.sendall(output)
    #     print("\r %d bytes sent" % (n,), end=" ")
    # sc.close()
    # print("  Socket closed")
