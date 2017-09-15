from pyzabbix import ZabbixAPI
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

trigger2=[]
template2=[]

zapi = ZabbixAPI('')

zapi.login('', '')

for template in zapi.template.get(selectTriggers='triggerid'):
    #print (template['name'])
    for trigger in template['triggers']:
        id = trigger['triggerid']
        for t in zapi.trigger.get(filter={'triggerid':id}):
            template2.append(template['name'])
            trigger2.append(t['description'])


data=pd.DataFrame({'Template Name':template2,'Trigger':trigger2})
data.to_csv('triggers_templates.csv',index=False)
