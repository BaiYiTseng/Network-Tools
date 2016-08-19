import telnetlib, socket, datetime, os

serverIP = input("Please enter the server IP: ")
serverPort = int(input("Please enter the application port: "))
# protocol = input("Please enter the protocol: (TCP/UDP")
successfulInterval = int(input("Please enter how often you would like to print successful connection: "))
monitoringDuration = int(input("Please enter how long you would like to monitor in seconds: "))
file = open("monitoring_telnet.txt", "w")
startT = datetime.datetime.now()
initialT = startT

print("The output is saved in the following directory:", os.getcwd())
print("File name: monitoring_telnet.txt")

while True:
	try:
		tn = telnetlib.Telnet(serverIP, serverPort)
		currentT = datetime.datetime.now()
		deltaT = (currentT - startT).seconds
		totalDuration = (currentT - initialT).seconds
		print("\r Successfully connecting to %s:%d, Start time: %s, End time: %s, DeltaT: %d seconds, Total Duration: %d seconds" % 
		      (serverIP, serverPort,
		       str(startT.hour)+":"+str(startT.minute)+":"+str(startT.second),
		       str(currentT.hour)+":"+str(currentT.minute)+":"+str(currentT.second), 
		       deltaT, totalDuration,), end=' ')
		if deltaT >= successfulInterval:
			message = "Connected for the last " + str(successfulInterval) + " seconds or more...\n"
			file.write(message)
			startT = datetime.datetime.now()
	except:
		print("Lost connection at", datetime.datetime.now())
		message = "Lost Connection at " + str(datetime.datetime.now()) + "\n"
		file.write(message)
		startT = datetime.datetime.now()
	if (datetime.datetime.now() - initialT).seconds >= monitoringDuration:
		break
file.close()