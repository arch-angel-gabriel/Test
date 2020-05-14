import telnetlib
import sys
import getpass


user = input('username : ')
password = getpass.getpass()

file = open('devices.txt')

for device in file:
    print('Establishing connection To :', device)
    host = device.strip()
    tn = telnetlib.Telnet(host)
    
    tn.read_until('Username: ')
    tn.write(user + '\n')
    if password:
        tn.read_until('Password: ')
        tn.write(password + '\n')
    tn.write('terminal length 0 \n')
    tn.write('show run')
    tn.write('exit\n')
    
    readoutput = tn.read_all()
    saveoutput = open('Device' + host, 'w')
    saveoutput.write(readoutput)
    saveoutput.write('\n')
    saveoutput.close
    print (tn.read_all())
    