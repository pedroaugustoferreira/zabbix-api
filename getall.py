
from getGroupsMidUnx import *
from getIP import *



groups = getGroupsMidUnx()

for group in groups:
    group_name = group['group_name']
    # print(group_name)
    
    hosts = getIP(group_name)
    for host in hosts:
        host_name = host['host_name']
        host_ip = host['host_ip']
        print(f'{group_name} : {host_name}: {host_ip}')


 

