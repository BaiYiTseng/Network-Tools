import datetime

x = int(input("Please enter the ceiling: "))
string = "abcdefg"
serverIP = "192.168.4.3"
serverPort = 9999
startT = datetime.datetime.now()

for i in range(x):
    # print('\r %s counting: %s' % (string, str(i),), end=' ')
    currentT = datetime.datetime.now()
    deltaT = (currentT-startT).seconds
    print("\r Successfully connect to %s:%d, startT:%s, currentT:%s" % (serverIP, serverPort, str(startT), str(currentT),), end=' ')
    # print("\r Successfully connect to %s:%d, startT:%s, currentT:%s" % (str(serverIP), serverPort, str(startT), str(currentT),), end=' ')
    # print("\r Successfully connect to %s:%d, current Time: %s, deltaT: %d" % (serverIP, serverPort, str(currentT), deltaT,), end=' ')
    # print("\r Successfully connect to %s:%d, startT:%s, currentT:%s, deltaT:%d" % (serverIP, serverPort, str(startT), str(currentT), deltaT,), end=' ')