import socket, ipaddress

delay = 1
network_ID = "8.8.8.0"
netmask = "24"
port_number = 53

cidr = network_ID + "/" + netmask   
network = ipaddress.ip_network(cidr)

for host in network.hosts():
    
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    
    
    host = str(host)
    # print("host", host, ":", "port number", port_number)
    try:
        TCPsock.connect((host, port_number))
        print("\r Successfully connect to %s" % (str(host)+":"+str(port_number)), end=' ')
    except:
        print("Unable to connect to " + str(host) + ":" + str(port_number))
        TCPsock.close()