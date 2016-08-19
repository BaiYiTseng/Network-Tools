# Looking up host names across an IP range
# Program requirement: Python 2.7

import ipaddress, socket, threading


def reverse_DNS(ip, output):
    try:
        output[ip] = socket.gethostbyaddr(ip)[0]
    except:
        output[ip] = ""
        
        
        
def get_host_name(network_cidr):
    
    network = ipaddress.ip_network(network_cidr)
    threads = []                # To run TCP_connect concurrently
    output = {}                 # For printing purposes
    max_thread_size = 800       # How many threads to run at a time. Python 2 is more limited than Python 3

    # Constructing the IP range
    network_range = []
    network_range.append(str(network.network_address))
    for host in network.hosts():
        network_range.append(str(host))
    network_range.append(str(network.broadcast_address))

    # Spawning threads to run reverse DNS lookup concurrently
    for i in range(len(network_range)):
        t = threading.Thread(target=reverse_DNS, args=(network_range[i], output))
        threads.append(t)

    # Starting threads
    for i in range(len(network_range)//max_thread_size+1):
        j = 0
        while j < max_thread_size and i*max_thread_size+j < len(network_range):
            threads[i*max_thread_size+j].start()
            j += 1
        # Locking the script until all threads complete
        j = 0
        while j < max_thread_size and i*max_thread_size+j < len(network_range):
            threads[i*max_thread_size+j].join()
            j += 1
    
    # Printing host names in the IP range from small to large
    for i in range(len(network_range)):
        ip = network_range[i]
        print network_range[i] + ': ' + output[ip]



def main():
    network_cidr = raw_input("Please enter network range in CIDR: ")
    delay = int(raw_input("Please enter how many seconds the socket is going to wait until time's out: "))   
    get_host_name(network_cidr)



if __name__ == "__main__":
    main()

