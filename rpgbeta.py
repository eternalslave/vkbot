# -*- coding: utf-8 -*-
import time
import vk_api
import math
import emoji
import random
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
            file=open('cd/'+str(item['user_id'])+'.txt', 'w')
            file.write(str(time.time()))
            file.close()
            
        else:
            timing=open('cd/'+str(item['user_id'])+'.txt', 'r')
            times=timing.read()
            if time.time()-float(times)>=5:
                exp=file.read()
                expN=float(exp[4:])+1
                if (math.log(expN/5+1, 2)%1==0):
                    write_msg(u'Грац, @id'+str(item['user_id'])+' (' + vk.method('users.get', { 'user_ids':item['user_id']})[0]['first_name']+u'), с '+str(int(math.log(expN/5+1, 2)))+u' лвлом!\n+'+str(3**int(math.log(expN/5+1, 2))+100)+' gold')
                    gold=open('gld/'+str(item['user_id'])+'.txt', 'r')
                    current=int(gold.read()[4:])+3**int(math.log(expN/5+1, 2))+100
                    gold.close()
                    gold=open('gld/'+str(item['user_id'])+'.txt', 'w')
                    gold.write('gld='+str(current))
                file=open('rpg/'+str(item['user_id'])+'.txt', 'w')
                file.write('exp='+str(expN))
                file.close()
            timing.close()
            file=open('cd/'+str(item['user_id'])+'.txt', 'w')
            file.write(str(time.time()))
            file.close()
        if item['body']=='/profile':
            file=open('rpg/'+str(item['user_id'])+'.txt', 'r')
            exp=file.read()
            exp=float(exp[4:])
            file.close()
            file=open('gld/'+str(item['user_id'])+'.txt', 'r')
            gold=file.read()
            file.close()
            write_msg(u'Профиль @id'+str(item['user_id'])+' (' + vk.method('users.get', { 'user_ids':item['user_id']})[0]['first_name']+ u')\nLVL: '+str(int(math.log(int(exp)/5+1, 2)))+emoji.emojize(':bust_in_silhouette:\nexp: ')+str(int(exp))+'/'+str((2**(int(math.log(int(exp)/5+1, 2))+1)-1)*5)+emoji.emojize(':books:\nGold: ')+gold[4:]+emoji.emojize(':money_with_wings:'))
        if item['body']=='/kit':
            try:
                file=open('gld/'+str(item['user_id'])+'_kit.txt', 'r')
            except IOError as e:
                file=open('gld/'+str(item['user_id'])+'_kit.txt', 'w')
                file.write(str(time.time()))
                file.close()
                file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                gold=file.read()
                gold=int(gold[4:])
                file.close()
                file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                file.write('gld='+str(gold+25))
                file.close()
                write_msg(emoji.emojize('+25 gold'))
            else:
                times=int(float(file.read()))
                if time.time()-times>=15*60:
                    file=open('gld/'+str(item['user_id'])+'_kit.txt', 'w')
                    file.write(str(time.time()))
                    file.close()
                    file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                    gold=file.read()
                    gold=int(gold[4:])
                    file.close()
                    file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                    file.write('gld='+str(gold+25))
                    file.close()
                    write_msg(emoji.emojize('+25 gold'))
                else:
                    write_msg('До следующего золота: '+str((15*60-(int(time.time())-times))//60)+' минут')
        if item['body'][0:5]=='/play':
            if random.randint(0,1):
                win=random.randint(50, 150)
                file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                gold=file.read()
                gold=int(gold[4:])
                file.close()
                if gold>=int(item['body'][6:]):
                    file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                    file.write('gld='+str(gold+int((item['body'][6:])*(win/100))))
                    file.close()
                    write_msg('Победа! +'+str(int(int(item['body'][6:])*(win/100))))
            else:
                file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                gold=file.read()
                gold=int(gold[4:])
                file.close()
                if gold>=int(item['body'][6:]):
                    file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                    file.write('gld='+str(gold-int(item['body'][6:])))
                    file.close()
                    write_msg('габела')
