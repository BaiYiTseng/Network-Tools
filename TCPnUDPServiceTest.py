import argparse, socket, ipaddress



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



def UDP_connect(IP, port_number, delay, x):
    
    UDPsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    UDPsock.settimeout(delay)
    
    try:
        UDPsock.connect((IP, port_number))
        UDPsock.recv(65536)
        print("\rSuccessfully connect to %s" % (IP+":"+str(port_number)), end=' ')
        x = -1
    except:
        if x:
            print("\nUnable to connect to " + IP + ":" + str(port_number))
            x = 0
        else:
            print("Unable to connect to " + IP + ":" + str(port_number))
    UDPsock.close()
    return x



def testTCP(port_number, network_ID, netmask, delay):
    
    cidr = network_ID + "/" + netmask   
    network = ipaddress.ip_network(cidr)
    x = 0   # To control the printing output
    
    x = TCP_connect(network_ID, port_number, delay, x)    
    for host in network.hosts():
        x = TCP_connect(str(host), port_number, delay, x)
    x = TCP_connect(str(network.broadcast_address), port_number, delay, x)
                   


def testUDP(port_number, network_ID, netmask, delay):
    
    cidr = network_ID + "/" + netmask   
    network = ipaddress.ip_network(cidr)
    x = 0
    
    x = UDP_connect(network_ID, port_number, delay, x)    
    for host in network.hosts():
        x = UDP_connect(str(host), port_number, delay, x)   
    x = UDP_connect(str(network.broadcast_address), port_number, delay, x)



def main():
    protocol = {'TCP':testTCP, 'UDP':testUDP}
    parser = argparse.ArgumentParser(description='Test TCP and UDP connection with a specific port')
    parser.add_argument('protocol', choices=protocol, help='which protocol, TCP or UDP?')
    parser.add_argument('port_number', help='which port number?', type=int)
    parser.add_argument('network_ID', help='network ID service resides', type=str, default="108.161.147.0")
    parser.add_argument('netmask', help='subnet mask of the network', type=str, default=24)
    parser.add_argument('delay', help='how long to wait before connection times out?', type=int, default=2)
    args = parser.parse_args()
    function = protocol[args.protocol]
    function(args.port_number, args.network_ID, args.netmask, args.delay)



if __name__ == "__main__":
    main()