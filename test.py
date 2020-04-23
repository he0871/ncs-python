import credential
#import client
import sshClient

cl = sshClient.SSHclient()
cl.ConnectViaJH(credential.jumphost,credential.username,credential.password)
cl.showVmanage()
cl.close()


'''
s1 = client.sshClient()
uname = credential.username
pswd = credential.password
host = credential.jumphost
print('try login ...')
s1.connect(host,uname,pswd)
print("jump...")
s1.jumpto()
s1.enterAdmin()
s1.showVPN()
'''