# This script continuously testing a web service connection
# by attempting a TCP handshake every given time (in seconds)
# Program Requirement: Python 2

from socket import *
from datetime import *
from time import *

host = raw_input('Please enter web sevice host name or IP: ')
port = input('Please enter port number of the service: ')
addr = (host, port)
period = input('Please enter the period of the connection attempt in seconds: ')
print 'Please enter the monitoring duration: '
hours = input('How many hours: ')
minutes = input('How many minutes: ')
file_name = raw_input('Enter the name of the log file you want to save as: ')
f = open(str(file_name), 'w')
counter = 0.0
successful_count = 0.0
failed_count = 0.0
switch = 0      # Making output prettier

print '==========Beginning of the Log=========='
f.write('==========Beginning of the Log==========\n')
start_time = datetime.now()
while (datetime.now()-start_time).seconds < (hours*60+minutes)*60:
    counter += 1
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(period)
    connection_start_time = datetime.now()
    try:
        sock.connect(addr)
        connection_end_time = datetime.now()
        delta_time = (connection_end_time - connection_start_time).seconds
        switch = 1
        if delta_time < period:
            sleep(period-delta_time)        
        print('\r%d: Successfully connecting to %s at [%s]' % (counter, addr, ctime())),
        f.write('%d: Successfully connecting to %s at [%s]\n' % (counter, addr, ctime()))
        sock.close()
        successful_count += 1
    except:
        connection_end_time = datetime.now()
        delta_time = (connection_end_time - connection_start_time).seconds
        if delta_time < period:
            sleep(period-delta_time)
        if switch == 1:
            print("")
        print '%d: Connection lost at [%s]' % (counter, ctime())
        switch = 0
        f.write('%d: Connection lost at [%s]\n' % (counter, ctime()))    
        sock.close()
        failed_count += 1

print '\n==========End of the log==========\n'
print 'Successful connection: %d\nFailed connection: %d' % (successful_count, failed_count)
print 'Successful rate: %.2f%%' % (successful_count/counter*100)
f.write('==========End of the Log==========\n\n')
f.write('Successful rate: %.2f%%\n' % (successful_count/counter*100))
f.write('Successful connection: %d\nFailed connection: %d' % (successful_count, failed_count))

f.close()
