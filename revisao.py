from pyzabbix import ZabbixAPI
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#Criar Classe para instanciar a API do Zabbix

hostname=[]
status=[]
error=[]
hostid=[]
templates=[]
h=[]
triggers=[]
nomehosttrigger = []
severidade = []
hgname=[]
hgid=[]

nome = str(raw_input("Digite o nome do cliente: "))
url=str(raw_input("Digite a URL: "))
user=str(raw_input("Digite o User: "))
password=str(raw_input("Digite a senha: "))

zapi = ZabbixAPI(url)

zapi.login(user, password)

print(zapi.api_version())

print "Working ..."

for x in zapi.host.get(output="extend"):
	hostname.append(x['host'])
        hostid.append(x['hostid'])
        #print (x['error'])
        error2 = (x['available'])

        if "2" in error2:
            error.append('Agent com problema')

        elif "0" in error2:
            error.append('Agent nao startado')

        else:
            error.append('Monitorado')

        status2 = (x['status'])

        if "0" in status2:
            status.append('Enable')
        else:
            status.append('Disable')

data=pd.DataFrame({'Hostname':hostname,'Status':status,'Agent':error})
data.to_csv(nome+'_zabbix_hosts.csv',index=False)


for linha in hostname:

   for y in zapi.host.get(selectParentTemplates={'parentTemplates':'name'},filter={'host':linha}):
       tam = (len(y['parentTemplates']))

       if tam == 0:
           h.append(linha)
           templates.append('Sem Templates')
       else:
           for z in range(0, tam):
               h.append(linha)
               templates.append(y['parentTemplates'][z]['name'])

data=pd.DataFrame({'Hostname':h,'Template':templates})
data.to_csv(nome+'_zabbix_templates.csv',index=False)

dicionario = {'1':'Information', '2':'Warning', '3':'Average', '4':'High', '5':'Disaster'}

for x in hostname:
    for item in zapi.trigger.get(output='extend', filter={'host':x}):
        nomehosttrigger.append(x)
        triggers.append(item['description'])
        severidade.append(dicionario[item['priority']])

data=pd.DataFrame({'Hostname':nomehosttrigger,'Triggers':triggers,'Severidade':severidade})
data.to_csv(nome+'_zabbix_triggers.csv',index=False)


for linha in zapi.hostgroup.get(output='extend'):
    hgid.append(linha['groupid'])

group = []
host=[]

for i in hostname:
    #print i
    for y in zapi.host.get(selectGroups='extend', filter={'host':i}):
            tam = len(y['groups'])
            for z in range(0, tam):
				host.append(i)
				group.append(y['groups'][z]['name'])

data=pd.DataFrame({'Hostname':host,'Host Group':group})
data.to_csv(nome+'_zabbix_groups.csv',index=False)
