# p.049 TCP Server and Client That can Deadlock
# TCP client and server that leave too much data waiting

import socket, sys

serverIP = input("Please enter server IP you would like to connect to: ")
serverPort = int(input("Please enter application port number: "))
bytecount = int(input("Please enter up to how many bytes you will send to the server: "))
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bytecount = (bytecount + 15) // 16 * 16     # round up to a multiple of 16
message = b"capitalize this!"       # 16-byte message to repeat over and over

print("Sending", bytecount, "bytes of data, in chunks of 16 bytes")
clientSock.connect((serverIP, serverPort))
sent = 0
while sent < bytecount:
    clientSock.sendall(message)
    sent += len(message)
    print("\r %d bytes sent" % (sent,), end=" ")
    sys.stdout.flush()

print()
clientSock.shutdown(socket.SHUT_WR)

print("Receiving all the data the server sends back")

received = 0
while True:
    data = clientSock.recv(42)
    if not received:
        print(" The first data received says", repr(data))
    if not data:
        break
    received += len(data)
    print("\r %d bytes received" % (received,), end=" ")

print()
clientSock.close()
