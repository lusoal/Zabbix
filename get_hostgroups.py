from pyzabbix import ZabbixAPI
import pandas as pd

hgname=[]
hgid=[]
hi=[]
hh=[]

group = []
host=[]

url=''
user=''
password=''

zapi = ZabbixAPI(url=url, user=user, password=password)

print(zapi.api_version())

for x in zapi.host.get(output='extend'):
    hi.append(x['hostid'])
    hh.append(x['host'])

for linha in zapi.hostgroup.get(output='extend'):
    hgid.append(linha['groupid'])
    #print linha['name']

for i in hh:
    #print i
    for y in zapi.host.get(selectGroups='extend', filter={'host':i}):
            tam = len(y['groups'])

            if tam == 3:
                host.append(i)
                host.append(i)
                host.append(i)
                group.append(y['groups'][tam-3]['name'])
                group.append(y['groups'][tam-2]['name'])
                group.append(y['groups'][tam-1]['name'])

            if tam == 2:
                host.append(i)
                host.append(i)
                group.append(y['groups'][tam-2]['name'])
                group.append(y['groups'][tam-1]['name'])

            if tam == 1:
                host.append(i)
                group.append(y['groups'][tam-1]['name'])


data=pd.DataFrame({'Hostname':host,'Host Group':group})
data.to_csv('zabbix_groups.csv',index=False)
