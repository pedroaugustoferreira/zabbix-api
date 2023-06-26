import apizabbix

def getIP(group_name):
    api = apizabbix.connect()

    # Obter o grupo pelo nome
    hostgroups = api.hostgroup.get(
        output='extend',
        filter={'name': group_name}
    )

    if hostgroups:
        group_id = hostgroups[0]['groupid']

        # Obter hosts do grupo
        hosts = api.host.get(
            output='extend',
            groupids=[group_id],
            selectInterfaces=['ip']  # Solicitar explicitamente o campo 'ip' das interfaces
        )
        result = []  # Lista para armazenar os resultados
        if hosts:
            for host in hosts:
                host_name = host['name']
                host_ip = host['interfaces'][0]['ip']
                # print(f"Host: {host_name} - IP: {host_ip}")
                result.append({'host_name': host_name, 'host_ip': host_ip})  # Adicionar o resultado à lista

    api.user.logout()
    return result


