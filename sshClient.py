from jumpssh import SSHSession

class SSHclient:
    def __init__(self):
        self.jumphost = None
        self.remote_session = None

    def ConnectViaJH(self, JHname, user, pswd):
        print("connecting the jumphost...")
        gateway_session = SSHSession(JHname,user, password = pswd).open()
        print("connecting the device...")
        nexthop = '2a0b:2900:114a:50b::1:10'
        self.remote_session = gateway_session.get_remote_session(nexthop, username='ubuntu',private_key_file='D:\code\ssh\cso_id_rsa')
        print("try pwd")
        feedback = self.remote_session.get_cmd_output("bash -lc 'pwd'")

        print(feedback)

    def showVmanage(self):
        print("check VPN info ....")
        cmd = "bash -lc 'show vpn G20023349 vpn-state'"
        feedback = self.remote_session.get_cmd_output("bash -lc 'python test.py'")
        print(feedback)
        catlog = self.remote_session.get_cmd_output("bash -lc 'cat pytest_Vmanage.log'")
        f =open("D:\code\Vmanage.log",'a')
        f.write(str(catlog))
        f.close()

    def close(self):
        self.remote_session.close()
        #self.jumphost.close()
