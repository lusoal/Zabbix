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


url= str(raw_input("Digite a URL do Cliente: "))
user=str(raw_input("Digite o usuario: "))
password=str(raw_input("Digite a senha: "))

zapi = ZabbixAPI(url=url, user=user, password=password)

print(zapi.api_version())

for l in zapi.host.get(output='extend'):
    hostid.append(l['hostid'])
    hostname.append(l['host'])


for x in hostname:
    #print(x)
    for item in zapi.trigger.get(output='extend', filter={'host':x}):
        nomehosttrigger.append(x)
        triggers.append(item['description'])
        severidade.append(item['priority'])


#data=pd.DataFrame({'Hostname':nomehosttrigger,'Triggers':triggers,'Severidade':severidade})
#data.to_csv('triggers_hosts.csv',index=False)

csv_out = open('triggers_hosts.csv','wb')

mywriter = csv.writer(csv_out)

for row in zip(nomehosttrigger,triggers,severidade):
    mywriter.writerow(row)

csv_out.close()
