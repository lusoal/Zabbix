from pyzabbix import ZabbixAPI
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

hostid = []
hostname = []
triggers=[]
nomehosttrigger = []
severidade = []

dicionario = {'1':'Information', '2':'Warning', '3':'Average', '4':'High', '5':'Disaster'}

url=''
user=''
password=''

zapi = ZabbixAPI(url)
zapi.login(user,password)
print(zapi.api_version())


for l in zapi.host.get(output='extend'):
    hostname.append(l['host'])

triggers.append('Trigger')
nomehosttrigger.append('Hostname')
severidade.append('Severidade')


for x in hostname:
    for item in zapi.trigger.get(output='extend', filter={'host':x}):
        nomehosttrigger.append(x)
        triggers.append(item['description'])
        severidade.append(dicionario[item['priority']])


#data=pd.DataFrame({'Hostname':nomehosttrigger,'Triggers':triggers,'Severidade':severidade})
#data.to_csv('triggers_hosts.csv',index=False)

csv_out = open('Zabbix-Hosts Triggers.csv','wb')

mywriter = csv.writer(csv_out)

for row in zip(nomehosttrigger,triggers,severidade):
    mywriter.writerow(row)

csv_out.close()
