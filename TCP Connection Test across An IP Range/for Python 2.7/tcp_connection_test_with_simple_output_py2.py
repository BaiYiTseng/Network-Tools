# Testing connections across a IP range on a specified port by attempting TCP three-way handshake
# Normal output on the screen
# Program requirement: Python 2.7

import socket, threading
from ipaddress import ip_network



def TCP_connect(IP, port_number, delay, count):
    
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    
    try:
        TCPsock.connect((IP, port_number))
        print "Successfully connect to %s" % (IP+":"+str(port_number))
        return count + 1
    except:
        print "Unable to connect to " + IP + ":" + str(port_number)
        return count



def test_TCP_connection(network_range, port_number, delay):
     
    network = ip_network(network_range)
    count = 0       # Counting number of successful connections
    
    count = TCP_connect(str(network.network_address), port_number, delay, count)    
    for host in network.hosts():
        count = TCP_connect(str(host), port_number, delay, count)
    count = TCP_connect(str(network.broadcast_address), port_number, delay, count)
    
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
