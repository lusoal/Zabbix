from pyzabbix import ZabbixAPI
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

hgname=[]
hgid=[]
hi=[]
hh=[]

group = []
host=[]

url=str(raw_input("Digite a URL: "))
user=str(raw_input("Digite o User: "))
password=str(raw_input("Digite a senha: ")) 


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
            for z in range(0, tam):
				host.append(i)
				group.append(y['groups'][z]['name'])

data=pd.DataFrame({'Hostname':host,'Host Group':group})
data.to_csv('zabbix_groups.csv',index=False)
