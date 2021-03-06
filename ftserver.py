# ========== ftserver.py ==========

import socket

MAX_BYTES = 10

serverIP = input("Please enter server IP or name: ")
port = int(input("Please enter application port number: "))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((serverIP, port))
sock.listen(1)
print("Server listening at", sock.getsockname())

while True:
    clientConnSock, clientIPnPort = sock.accept()
    print("Got connection from", clientIPnPort)
    filename = clientConnSock.recv(1024).decode('ascii')
    print("Sending %s file to the client," % filename, clientIPnPort)
    f = open(filename, 'rb')
    l = f.read(MAX_BYTES)
    count = 0
    while(l):
        clientConnSock.send(l)
        print("==========Sent %d==========\n" % count, l.decode('ascii'))
        l = f.read(MAX_BYTES)
        count = count + 1
    f.close()
    
    print("\n\n\nDone sending the file,", filename)
    clientConnSock.send('Thank you for connecting'.encode('ascii'))
    clientConnSock.close()