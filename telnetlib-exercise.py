import getpass
import telnetlib
import time

HOST = "10.0.15.31"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
time.sleep(1)

tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
time.sleep(1)

def vrf(intf, ip):
    interface = b"interface " + intf.encode('ascii') + b"\n"
    ip_command = b"ip address " + ip.encode('ascii') + b" 255.255.255.0\n"
    tn.write(b"conf t\n")
    tn.write(interface)
    tn.write(b"vrf forwarding control-data\n")
    tn.write(ip_command)
    tn.write(b"no shut\n")

vrf('g0/1', '192.168.1.1')
vrf('g0/2', '192.168.2.1')
tn.write(b"exit\n")
time.sleep(1)

# print(tn.read_all().decode('ascii'))
output = tn.read_very_eager()
# print(output.decode('ascii'))
print("192.168.1.1 of Gi0/1 is assigned to VRF control-data")
print("192.168.2.1 of Gi0/2 is assigned to VRF control-data")

tn.close()