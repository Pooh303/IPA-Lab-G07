import pexpect

PROMPT = '#'
IP = '172.31.107.4'
LOOPBACK = '172.16.2.2'
USERNAME = 'admin'
PASSWORD = 'cisco'

child = pexpect.spawn('telnet ' + IP)
child.expect('Username')
child.sendline(USERNAME)
child.expect('Password')
child.sendline(PASSWORD)

child.expect(PROMPT)
child.sendline('conf t')
child.expect(PROMPT)
child.sendline('interface loopback 0')
child.expect(PROMPT)
child.sendline('ip address ' + LOOPBACK + ' 255.255.255.255')
child.expect(PROMPT)

# result = child.before
# print(result)
# print()
# print(result.decode('UTF-8'))
print('Loopback0', LOOPBACK, 'is created on', IP)
child.sendline('exit')
