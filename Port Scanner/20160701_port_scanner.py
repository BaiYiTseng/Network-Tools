# Probing a server or host for open TCP ports
# Program requirement: Python 3.5

import socket, threading



def TCP_connect(ip, port_number, delay, output):
    
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''
    
    TCPsock.close()
        
        
        
def scan_ports(host_ip, port_bottom, port_ceiling, delay):
    
    threads = []        # To run TCP_connect concurrently
    output = {}         # For printing
    number_of_ports = port_ceiling - port_bottom + 1

    # Spawning threads to scan ports
    for i in range(port_bottom, port_ceiling+1):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    # Starting threads
    for i in range(number_of_ports):
        threads[i].start()

    # Locking the script until all threads complete
    for i in range(number_of_ports):
        threads[i].join()
    
    # Printing listening ports from small to large
    for i in range(number_of_ports):
        if output[i+port_bottom] == 'Listening':
            print(str(i+port_bottom) + ': ' + output[i+port_bottom])



def main():
    host_ip = input("Enter host IP: ")
    print("Enter port range to be scanned:")
    port_bottom = input("From port (default=0): ")
    if port_bottom == '':
        port_bottom = 0
    else:
        port_bottom = int(port_bottom)
    port_ceiling = int(input("To port: "))
    delay = int(input("Enter how many seconds the socket is going to wait until timeout: "))   
    scan_ports(host_ip, port_bottom, port_ceiling, delay)



if __name__ == "__main__":
    main()

