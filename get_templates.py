from pyzabbix import ZabbixAPI
import pandas as pd
#Criar Classe para instanciar a API do Zabbix

hostname=[]
hostid=[]
templates=[]
h=[]



url=''
user=''
password=''

zapi = ZabbixAPI(url=url, user=user, password=password)

print(zapi.api_version())

#colocar em lista hostname

for x in zapi.host.get(output="extend"):
	hostname.append(x['host'])
	hostid.append(x['hostid'])


for linha in hostname:

	for y in zapi.host.get(selectParentTemplates={'parentTemplates':'name'},filter={'host':linha}):
		tam = (len(y['parentTemplates']))
 		if tam == 4:
				h.append(linha)
				h.append(linha)
				h.append(linha)
				h.append(linha)
			 	templates.append(y['parentTemplates'][tam-4]['name'])
			 	templates.append(y['parentTemplates'][tam-3]['name'])
			 	templates.append(y['parentTemplates'][tam-2]['name'])
			 	templates.append(y['parentTemplates'][tam-1]['name'])

		elif tam == 3:
				h.append(linha)
   			 	h.append(linha)
			 	h.append(linha)
			 	templates.append(y['parentTemplates'][tam-3]['name'])
			 	templates.append(y['parentTemplates'][tam-2]['name'])
			 	templates.append(y['parentTemplates'][tam-1]['name'])

		elif tam == 2:
			 h.append(linha)
			 h.append(linha)
			 templates.append(y['parentTemplates'][tam-2]['name'])
			 templates.append(y['parentTemplates'][tam-1]['name'])

		elif tam == 1:
			 h.append(linha)
			 templates.append(y['parentTemplates'][tam-1]['name'])

		elif tam == 0:
			 h.append(linha)
			 templates.append('Sem Templates')
			#templates.append(y)


print (h)
print(templates)

data=pd.DataFrame({'Hostname':h,'Template':templates})
data.to_csv('zabbix_templates.csv',index=False)
