import getpass
import telnetlib
import time

HOST = "172.31.107.3"
user = 'admin'
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
time.sleep(1)

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
time.sleep(1)

tn.write(b"conf t\n")
tn.write(b"int g0/1\n")
tn.write(b"vrf forwarding control-data\n")
tn.write(b"ip address 192.168.1.1 255.255.255.0\n")
tn.write(b"no shut\n")

tn.write(b"int g0/2\n")
tn.write(b"vrf forwarding control-data\n")
tn.write(b"ip address 192.168.2.1 255.255.255.0\n")
tn.write(b"no shut\n")

tn.write(b"exit\n")
time.sleep(1)

# print(tn.read_all().decode('ascii'))
output = tn.read_very_eager()
print(output.decode('ascii'))

tn.close()