from pyzabbix import ZabbixAPI
import pandas as pd
#Criar Classe para instanciar a API do Zabbix

hostname=[]
hostid=[]
templates=[]
h=[]

url=str(raw_input("Digite a URL: "))
user=str(raw_input("Digite o User: "))
password=str(raw_input("Digite a senha: "))

zapi = ZabbixAPI(url=url, user=user, password=password)

print(zapi.api_version())

#colocar em lista hostname

for x in zapi.host.get(output="extend"):
	hostname.append(x['host'])
	hostid.append(x['hostid'])


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
data.to_csv('zabbix_templates.csv',index=False)
