import os, subprocess, time, datetime

# Change working directory to Desktop
username = os.getlogin()
os.chdir('C:\\Users\\' + username + '\\Desktop')

# Create a file name to store the output, default: new_icmp_log_dates.txt
filename = input('Enter the name of the text file youd like the output to be saved as: ')
if not filename:
    date = str(datetime.datetime.now().date()).replace('-', '')
    filename = 'new_icmp_log_' + date + '.txt'
else:
    filename = filename + '.txt'

# Choose if printing the output on the console or not, default: Y 
print_on_screen = input('Would you like to print the output on the console as well?(Y/N) ')

destination_ip = input('Please enter the destination IP address: ')

# Input monitor duration
duration = {}
print('How long to monitor the ICMP response.')
duration['days'] = input('\tHow many days: ')
duration['hours'] = input('\tHow many hours: ')
duration['minutes'] = input('\tHow many minutes: ')
duration['seconds'] = input('\tHow many seconds: ')
for element in duration:
    if not duration[element]:
        duration[element] = 0
    else:
        duration[element] = int(duration[element])
if not duration['seconds']:
    duration['seconds'] = 1
duration = (((((duration['days'] * 24) + duration['hours']) * 60) + duration['minutes']) * 60) + duration['seconds']

start_time = datetime.datetime.now()
output = ''
sent_count = 0
successful_count = 0
failed_count = 0

with open(filename, 'w') as new_file:
    while (datetime.datetime.now() - start_time).seconds < duration:
        try:
            response = subprocess.check_output(['ping', '-n', '1', destination_ip]).decode('utf-8').strip().split('\n')[1].strip()
        except:
            response = 'Request timed out.'
        sent_count += 1
        if 'TTL=' in response:
            successful_count += 1
        else:
            failed_count += 1
        line = str(datetime.datetime.now()) + '\t' + response
        new_file.write(output + line + '\n')
        if print_on_screen.upper() != 'N':
            print(line)
    loss_percentage = str(round(((failed_count/sent_count) * 100), 2))
    result = 'Ping statistics for ' + destination_ip + ':\n\tPackets: Sent = ' + str(sent_count) + ', Received = ' + str(successful_count) + \
        ', Lost = ' + str(failed_count) + ' (' + loss_percentage + '% loss)\n'
    new_file.write('\n' + result)
    if print_on_screen.upper() != 'N':
        print('\n' + result)
    
new_file.close()