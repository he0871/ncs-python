"""
structure of Vmanage
['__class__', '__delattr__', '__doc__', '__format__', '__get__', '__getattribute__', '__hash__', 
'__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__self_class__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__thisclass__', 'controllers', 'csrs', 
'device_ip', 'device_name', 'dics', 'hostname', 'id', 'interface', 'mgmt_ip_address', 'name', 
'password', 'recovery', 'shadow', 'username', 'vedges', 'viptela_serial_file', 'vm_id']
"""
import ncs
from datetime import datetime
def showVmanage():
    with ncs.maapi.single_write_trans('admin', 'python', groups=['ncsadmin']) as t:
        root = ncs.maagic.get_root(t)
        vm = root.ngena_vmanage_data__vmanage_data
        f = open("pytest_Vmanage.log", "a")
        timestamp = datetime.now()
        f.write(str(timestamp))
        f.write("\nVmange status\n")
        for item in vm:
            #print(dir(item))
            f.write("---------------\n")
            f.write('name : ' + str(item.name) + '\n')
            f.write('device_ip : ' + str(item.device_ip) +'\n')
            f.write('device_name : ' + str(item.device_name) + '\n')
            f.write('hostname : ' + str(item.hostname) + '\n')
            f.write('id : ' + str(item.id) + '\n')
            f.write('vedges : ' + str(item.vedges) + '\n')
        f.close()
        print("vmanage log generate success")

showVmanage()