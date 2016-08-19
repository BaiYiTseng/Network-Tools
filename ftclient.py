# ========== ftclient.py ==========

import socket, sys

MAX_BYTE = 512

serverIP = input("Please enter the server IP you are downloading a file from: ")
port = int(input("Please enter the port number of the file transfer application: "))
filename = input("Please enter the file name you want to download from the server: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serverIP, port))
sock.send(filename.encode('ascii'))

count = 0
f = open("filedownloaded.py", 'w')

while True:
    print("%d ========= Receiving data from" % (count+1), (serverIP, port), "==========")
    data = sock.recv(MAX_BYTE).decode('ascii')
    sys.stdout.flush()
    print("received data size: ", len(data))
    sys.stdout.flush()
    print(data)
    if not data:
        break
    f.write(data)
    sys.stdout.flush()
    count = count + 1

f.close()
print("Successfully get the file,", filename)
sock.close()
print("Connection closed")