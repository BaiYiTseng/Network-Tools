# Testing connections across a IP range on a specified port by attempting TCP three-way handshake
# Output: printing on the screen, consecutive successful connections will be shown with only one line and only the latest successful connection will be shown
# Program requirement: Python 2.7

import socket
from ipaddress import ip_network



def TCP_connect(IP, port_number, delay, x, count):
    
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    
    try:
        TCPsock.connect((IP, port_number))
        print("\rSuccessfully connect to %s" % (IP+":"+str(port_number))),
        x = -1
        count = count + 1
    except:
        if x:
            print "\nUnable to connect to " + IP + ":" + str(port_number)
            x = 0
        else:
            print "Unable to connect to " + IP + ":" + str(port_number)
    return (x, count)



def test_TCP_connection(network_range, port_number, delay):
     
    network = ip_network(network_range)
    x = 0       # To control the printing output so that consecutive successful connections only show on one line
    count = 0   # Count the number of successful connections

    if network.network_address == network.broadcast_address:
        x, count = TCP_connect(str(network.network_address), port_number, delay, x, count)
    else:
        x, count = TCP_connect(str(network.network_address), port_number, delay, x, count)
        for host in network.hosts():
            x, count = TCP_connect(str(host), port_number, delay, x, count)
        x, count = TCP_connect(str(network.broadcast_address), port_number, delay, x, count)
        
        if count == 0:
            print "\n\nUnable to communicate to %s on port %s" % (network_range, port_number)
        else:
            print "\n\nTotal successful connection: %d" % count    


 
def main():
    network_range = raw_input("Please enter network range in CIDR: ")
    port_number = int(raw_input("Please enter TCP port number: "))
    delay = int(raw_input("Please enter how many seconds the socket is going to wait until times out: "))
    test_TCP_connection(network_range, port_number, delay)
    


if __name__ == "__main__":
    main()
