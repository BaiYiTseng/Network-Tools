import socket, threading
from ipaddress import ip_network



def TCP_connect(IP, port_number, delay, recording):
    
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    
    try:
        TCPsock.connect((IP, port_number))
        recording[IP] = 1
    except:
        recording[IP] = 0



def test_TCP_connection(network_range, port_number, delay, file_name):
     
    network = ip_network(network_range)
    count = 0       # Counting successful connections
    recording = {}     # Recording if connection is successful
    threads = []    # To run TCP_connect concurrently

    # Constructing the IP range
    scan_range = []
    scan_range.append(str(network.network_address))
    for host in network.hosts():
        scan_range.append(str(host))
    scan_range.append(str(network.broadcast_address))

    # Spawning threads to run TCP_connect concurrently
    for i in range(len(scan_range)):
        t = threading.Thread(target=TCP_connect, args=(scan_range[i], port_number, delay, recording))
        threads.append(t)

    # Starting threads and recording whether each connection is successful (1) or not (0)
    for i in range(len(scan_range)):
        recording[scan_range[i]] = threads[i].start()

    # Locking the script until all threads complete
    for i in range(len(scan_range)):
        threads[i].join()

    # Outputing the result
    if file_name != '':
        file_name += '.txt'
        f = open(file_name, 'w')
    for i in range(len(scan_range)):
        if recording[scan_range[i]] == 1:
            if file_name == '':
                print "Successfully connecting to %s" % (scan_range[i]+":"+str(port_number))
            else:
                f.write("Successfully connecting to %s\n" % (scan_range[i]+":"+str(port_number)))
        else:
            if file_name == '':
                print "Unable to connect to " + scan_range[i] + ":" + str(port_number)
            else:
                f.write("Unable to connect to " + scan_range[i] + ":" + str(port_number) + '\n')

    # Counting the number of successful connections
    for IP in recording:
        count += recording[IP]
    
    if count == 0:
        if file_name == '':
            print "\n\nUnable to communicate to %s on port %s" % (network_range, port_number)
        else:
            f.write("\nUnable to communicate to %s on port %s" % (network_range, port_number))
    else:
        if file_name == '':
            print "\n\nTotal successful connections: %d" % count
        else:
            f.write("\nTotal successful connections: %d" % count)

    if file_name != '':
        f.close()


 
def main():
    network_range = raw_input("Please enter network range in CIDR: ")
    port_number = int(raw_input("Please enter TCP port number: "))
    delay = int(raw_input("Please enter how many seconds the socket is going to wait until times out: "))
    file_name = raw_input("As what file name would you like to save the output?\nClick on \"Enter\" to print it directly on the screen: ")
    test_TCP_connection(network_range, port_number, delay, file_name)
    


if __name__ == "__main__":
    main()
