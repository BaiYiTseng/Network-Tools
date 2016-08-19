import socket



delay = 5
TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPsock.settimeout(delay)

for i in range(10):
    try:
        TCPsock.connect(("64.62.142.2", 443))
        print("\r Successfully connect to 64.64.142.2:443", i)
    except:
        print("Unable to connect to 64.62.142.2:443")