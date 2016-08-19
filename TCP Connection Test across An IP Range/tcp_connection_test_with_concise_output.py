# Testing connections across a IP range on a specified port by attempting TCP three-way handshake
# Output: printing on the screen, consecutive successful connections will be shown with only one line and only the latest successful connection will be shown
# Program requirement: Python 3.5

python import argparse, socket, ipaddress



def TCP_connect(IP, port_number, delay, x):
    
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    
    try:
        TCPsock.connect((IP, port_number))
        print("\rSuccessfully connect to %s" % (IP+":"+str(port_number)), end=' ')
        x = -1
    except:
        if x:
            print("\nUnable to connect to " + IP + ":" + str(port_number))
            x = 0
        else:
            print("Unable to connect to " + IP + ":" + str(port_number))
    return x



def test_TCP_connection(network_range, port_number, delay):
     
    network = ipaddress.ip_network(network_range)
    x = 0   # To control the printing output
    
    x = TCP_connect(str(network.network_address), port_number, delay, x)    
    for host in network.hosts():
        x = TCP_connect(str(host), port_number, delay, x)
    x = TCP_connect(str(network.broadcast_address), port_number, delay, x)



def main():
    network_range = input("Please enter network in CIDR: ")
    port_number = int(input("Please enter TCP port number: "))
    delay = int(input("Please enter how many seconds the socket is going to wait until times out: "))
    test_TCP_connection(network_range, port_number, delay)



if __name__ == "__main__":
    main()