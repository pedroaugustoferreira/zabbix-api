from pyzabbix import ZabbixAPI

import os

def connect():
    
    zapi = ZabbixAPI(os.getenv('server'))
    zapi.session.verify = False
    zapi.login(os.getenv('user'), os.getenv('password'))
    
    return zapi

