# ==========Multithread TCP File Transfer on Localhost==========

import socket, sys

MAX_BYTE = 1024

serverIP = input("Please enter the server IP you are downloading a file from: ")
serverPort = int(input("Please enter the port number of the file transfer application: "))
filename = input("Please enter the file name you want to download from the server: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((serverIP, serverPort))
sock.send(filename.encode('ascii'))

count = 0
f = open("mtftdownload.py", 'w')

while True:
    print("%d ========= Receiving data from" % (count+1), (serverIP, serverPort), "==========")
    data = sock.recv(MAX_BYTE).decode('ascii')
    print("received data size: ", len(data))
    print(data)
    if not data:
        f.close()
        print("file close()")
        break
    f.write(data)

print("Successfully get the file,", filename)
sock.close()
print("Connection closed")
