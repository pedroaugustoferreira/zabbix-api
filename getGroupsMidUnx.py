import apizabbix

def getGroupsMidUnx():
    api = apizabbix.connect()
    
    hostgroups = api.hostgroup.get(
        output='extend',
        excludeSearch=True,
        search={
            'name': 'Templates'
        }
    )
    
    keywords1 = ["LINUX", "MID","IIS","OPENSHIFT","EKS","SUPUNX","*" ]
    keywords2 = ["MARABRAZ","ACFIN","ODONTO","UNIMED","SASCAR","CSE","CNU","RANDON","FRG","OVD","EQUINIX","JSL","SIMPAR"]
    
    
    result = []  
    for hostgroup in hostgroups:
        group_name = hostgroup['name']
        # print(group_name)
        if any(keyword in group_name for keyword in keywords1) and any(excluded_keyword in group_name for excluded_keyword in keywords2):
            # print(group_name)
            result.append({'group_name': group_name})  # Adicionar o resultado à lista
        
    api.user.logout()
    return result


