from pyzabbix import ZabbixAPI
import pandas as pd

templateid=[]
items=[]
nometemplate=[]
n = 1

url=str(raw_input("Digite a URL: "))
user=str(raw_input("Digite o User: "))
password=str(raw_input("Digite a senha: "))

zapi = ZabbixAPI(url=url, user=user, password=password)

print(zapi.api_version())


for i in zapi.template.get(output='extend'):
    templateid.append(i['host'])

for x in templateid:
    #print x
    for linha in zapi.template.get(selectItems={'items':'name'}, filter={'name':x}):
        tam = len(linha['items'])
        #nometemplate.append(x)
        #items.append(linha['items'])
        for h in range(0, tam):
            nometemplate.append(x)
            items.append(linha['items'][h]['name'])
        #tam = len(linha['items'])
        #p =  len(items)

data=pd.DataFrame({'Template Name':nometemplate,'Items':items})
data.to_csv('zabbix_templates_items.csv',index=False)
