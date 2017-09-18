
from pyzabbix import ZabbixAPI
import pandas
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#Criar Classe para instanciar a API do Zabbix

hostIds= []
hostNames= []
hostStatus= []
hostAvailables= []
templates= []
hostAux= []
nvlAlerta = {'1':'Information', '2':'Warning', '3':'Average', '4':'High', '5':'Disaster'}
hostGroup = []
triggers= []
severidade= []
user = raw_input("Digite o User: ")
password = raw_input("Digite a senha: ")
organizacao = raw_input("Digite o nome do cliente: ")

zabbix = ZabbixAPI(raw_input("Digite a URL: "))
zabbix.login(user,password)

for host in zabbix.host.get(output="extend"):
	hostNames.append(host['host'])
	hostIds.append(host['hostid'])
	hostStatus.append('Enable' if host['status'] is '0' else 'disable')
	hostAvailables.append('Agent com problema' if host['available'] is '2' else 'Agent nao startado' if host['available'] is '0' else 'Monitorado')

data = pandas.DataFrame({'Hostname':hostNames, 'Status': hostStatus,'Agent': hostAvailables})
data.to_csv(organizacao +'_zabbix_hosts.csv',index=False)

for hostName in hostNames:
	for template in zabbix.host.get(selectParentTemplates={'parentTemplates':'name'},filter={'host':hostName}):
		if len(template['parentTemplates']) == 0:
			hostAux.append(hostName)
			templates.append('Sem Templates')
        else:
            for index in range(0, len(template['parentTemplates'])):
				hostAux.append(hostName)
				templates.append(template['parentTemplates'][index]['name'])

data=pandas.DataFrame({'Hostname':hostAux,'Template':templates})
data.to_csv(organizacao+'_zabbix_templates.csv',index=False)

hostAux = []
for host in hostNames:
	for trigger in zabbix.trigger.get(output='extend', filter={'host':host}):
		hostAux.append(host)
		triggers.append(trigger['description'])
		severidade.append(nvlAlerta[trigger['priority']])

data=pandas.DataFrame({'Hostname':hostAux,'Triggers':triggers,'Severidade':severidade})
data.to_csv(organizacao+'_zabbix_triggers.csv',index=False)

hostAux = []
for host in hostNames:
    for group in zabbix.host.get(selectGroups='extend', filter={'host':host}):
        for index in range(0, len(group['groups'])):
			hostAux.append(index)
			hostGroup.append(group['groups'][index]['name'])

data=pandas.DataFrame({'Hostname':host,'Host Group':hostGroup})
data.to_csv(organizacao+'_zabbix_groups.csv',index=False)
