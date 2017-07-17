# -*- coding: utf-8 -*-
import time
import vk_api
import math
vk = vk_api.VkApi(login = 'artem.ebal@yandex.ru', password = 'ukeahi312ua')
vk.auth()
values = {'out': 0,'count': 100,'time_offset': 60}
def write_msg(s):
    vk.method('messages.send', {'chat_id':1,'message':s})
while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        try:
            file=open('rpg/'+str(item['user_id'])+'.txt', 'r')
        except IOError as e:
            file=open('rpg/'+str(item['user_id'])+'.txt', 'w')
            file.write('exp=1')
            file.close()
            file=open('gld/'+str(item['user_id'])+'.txt', 'w')
            file.write('gld=0')
            file.close()
            
        else:
            exp=file.read()
            if exp:
                expN=float(exp[4:])+1
                if (math.log(expN/5+1, 2)%1==0):
                    write_msg(u'Грац, @id'+str(item['user_id'])+' (' + vk.method('users.get', { 'user_ids':item['user_id']})[0]['first_name']+u'), с '+str(int(math.log(expN/5+1, 2)))+u' лвлом!\n+'+str(5**int(math.log(expN/5+1, 2))+100)+'gold')
                    gold=open('gld/'+str(item['user_id'])+'.txt', 'r')
                    current=int(gold.read()[4:])+5**int(math.log(expN/5+1, 2))+100
                    gold.close()
                    gold=open('gld/'+str(item['user_id'])+'.txt', 'w')
                    gold.write('gld='+str(current))
            file=open('rpg/'+str(item['user_id'])+'.txt', 'w')
            file.write('exp='+str(expN))
            file.close()
        if item['body']=='/profile':
            file=open('rpg/'+str(item['user_id'])+'.txt', 'r')
            exp=file.read()
            exp=float(exp[4:])
            file.close()
            file=open('gld/'+str(item['user_id'])+'.txt', 'r')
            gold=file.read()[4:]
            write_msg(u'Профиль @id'+str(item['user_id'])+' (' + vk.method('users.get', { 'user_ids':item['user_id']})[0]['first_name']+ u')\nLVL: '+str(int(math.log(int(exp)/5+1, 2)))+'\nexp:'+str(int(exp))+'/'+str((2**(int(math.log(int(exp)/5+1, 2))+1)-1)*5)+'\nGOLD: '+gold)
