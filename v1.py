# -*- coding: utf-8 -*-
import time
import vk_api
import random
vk = vk_api.VkApi(login = 'artem.ebal@yandex.ru', password = 'ukeahi312ua')
vk.auth()
adm = vk_api.VkApi(login = 'dark.fusrodah@gmail.com', password = 'srn1wpua')
adm.auth()
timer1 = time.time()
timer3 = time.time()-60*36
def write_msg(s):
    vk.method('messages.send', {'chat_id':1,'message':s})
values = {'out': 0,'count': 100,'time_offset': 60}
def name():
    title=adm.method('messages.getChat', {'chat_id':340})
    if title['title']!=u'=добро пожаловать= v1.2':
        vk.method('messages.editChat', {'chat_id':1, 'title':u'=добро пожаловать= v1.2'})
def adder():
    rqst=vk.method('friends.getRequests', {'need_mutual':0})
    if rqst:
        for id in rqst['items']:
            vk.method('friends.add', {'user_id':id})
            try:
                vk.method('messages.addChatUser', {'chat_id':1, 'user_id':id})
            except:
                vk.method('messages.send', {'user_id':id, 'message':'Ты уже есть в беседе'})
            else:
                us=vk.method('users.get', {'user_ids':id})
                write_msg(u'Добро пожаловать в =добро пожаловать=, '+us[0]['first_name']+u'! \n/help - Спиок комманд\nПодпишись на нашь паблик - https://vk.com/dobropojalovatv12')
            vk.method('account.banUser', {'user_id':id})
def kicker(name):
    adm.method('messages.removeChatUser', {'chat_id':340, 'user_id':name})
    write_msg(u'Succes затролил лолку)')    
    
while True:
    name()
    adder()
    if (time.time()-timer1>=60*60):
            timer1 = time.time()
            write_msg(u'Вступай в нашу группу вк - https://vk.com/dobropojalovatv12 :Р \nСписок комманд: /help')
    if (time.time()-timer3>=60*35):
            timer3 = time.time()
            post=vk.method('wall.get', {'domain':'onsmolny', 'count':100})
            while True:
                b=random.randint(0, 100)
                if post['items'][b]['text']:
                    write_msg(post['items'][b]['text'])
                    break
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
            if item['body']=='/id':
                write_msg(str(item['user_id']))
            if item['body']=='/help':
                write_msg(u'Список комманд:\n/rules - Правила беседы\n/profile - посмотреть свой профиль\n/prikol - мемы\n/kit - золото каждые 15 минут (кол-во зависит от уровня)\n/play [кол-во] - сыграть на голду (upd. выигрышь от 150% до 250% от ставки, шанс 20%)\n /give [id] [кол-во] - передать деньги\n/gift [id] [id подарка] - подарить подарок\n/gift list - список подарков\n/id - Получить свой id в чате\nhttps://vk.com/dobropojalovatv12 - Группа вк')
            if item['body']=='/rules':
                write_msg(u'правила тут https://vk.com/topic-150358061_35543589')
            if (item['body'][0:5]=='/kick' and (item['user_id']==32191511 or item['user_id']==287948150)): #32191511
                kicker(item['body'][6:len(item['body'])])
            if item['body']=='/prikol':
                pr=vk.method('photos.get', {'owner_id':32191511, 'album_id':221862225})
                b=random.randint(0, pr['count'])-1
                vk.method('messages.send', {'chat_id':1, 'attachment':'photo'+str(pr['items'][b]['owner_id'])+'_'+str(pr['items'][b]['id'])})
                
    time.sleep(1)
