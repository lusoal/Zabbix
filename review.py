#coding=utf-8
from pyzabbix import ZabbixAPI
from datetime import datetime
from funcoes import *
import pandas
import pygsheets
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#Criar Classe para instanciar a API do Zabbix

#Autorização para trabalhar com a api do google Drive e Sheets
gc = pygsheets.authorize(service_file='service_key.json')
#Data atual
date = str((datetime.now()).month) + '/' + str((datetime.now()).year)
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
#printa o menu para escolher o time responsavel pelo cliente
print(menu_team())
#pede o valor correspondente ao time
team_id = raw_input("Digite o número correspondete ao time: ")
#Printa o menu para escolher qual o cliente
print(menu_folders(team_id))
#Solicita qual cliente selecionado
cliente_id = raw_input("Digite o número correspondete ao cliente: ")
#Pega o id da pasta que vai ser salva a planilha
folder_id = id_folders(team_id, cliente_id)
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


#Cria a Google sheet no Google Drive
sh = gc.create('Revisão de monitoramento ' + organizacao + ' - ' + date, parent_id=folder_id)
#Seleciona a sheet a ser preenchida sheet
wks = sh.sheet1
#modifica o titulo da aba da planilha atual
wks.title = organizacao +'_zabbix_hosts'
#Cria um dataframe com as listas coletadas do Zabbix server
data = pandas.DataFrame({'Hostname':hostNames, 'Status': hostStatus,'Agent': hostAvailables})
#Envia a matriz do Dataframe para a planilha selecionada, iniciando na celula (1,1)
wks.set_dataframe(data, (1, 1))

for hostName in hostNames:
	for template in zabbix.host.get(selectParentTemplates={'parentTemplates':'name'},filter={'host':hostName}):
		if len(template['parentTemplates']) == 0:
			hostAux.append(hostName)
			templates.append('Sem Templates')
        else:
            for index in range(0, len(template['parentTemplates'])):
				hostAux.append(hostName)
				templates.append(template['parentTemplates'][index]['name'])

#Cria um dataframe com as listas coletadas do Zabbix server
data = pandas.DataFrame({'Hostname':hostAux,'Template':templates})
#Cria uma nova aba dentro da planilha
wks = sh.add_worksheet(organizacao+'_zabbix_templates')
#Envia a matriz do Dataframe para a planilha selecionada, iniciando na celula (1,1)
wks.set_dataframe(data, (1, 1))

hostAux = []
for host in hostNames:
	for trigger in zabbix.trigger.get(output='extend', filter={'host':host}):
		hostAux.append(host)
		triggers.append(trigger['description'])
		severidade.append(nvlAlerta[trigger['priority']])

#Cria um dataframe com as listas coletadas do Zabbix server
data=pandas.DataFrame({'Hostname':hostAux,'Triggers':triggers,'Severidade':severidade})
#Cria uma nova aba dentro da planilha
wks = sh.add_worksheet(organizacao+'_zabbix_triggers')
#Envia a matriz do Dataframe para a planilha selecionada, iniciando na celula (1,1)
wks.set_dataframe(data, (1, 1))

hostAux = []
for host in hostNames:
    for group in zabbix.host.get(selectGroups='extend', filter={'host':host}):
        for index in range(0, len(group['groups'])):
			hostAux.append(index)
			hostGroup.append(group['groups'][index]['name'])

#Cria um dataframe com as listas coletadas do Zabbix server
data=pandas.DataFrame({'Hostname':host,'Host Group':hostGroup})
#Cria uma nova aba dentro da planilha
wks = sh.add_worksheet(organizacao+'_zabbix_groups')
#Envia a matriz do Dataframe para a planilha selecionada, iniciando na celula (1,1)
wks.set_dataframe(data, (1, 1))
