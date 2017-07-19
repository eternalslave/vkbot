# -*- coding: utf-8 -*-
import time
import vk_api
adm = vk_api.VkApi(login = 'dark.fusrodah@gmail.com', password = 'srn1wpua')
adm.auth()
bot = vk_api.VkApi(login = 'artem.ebal@yandex.ru', password = 'ukeahi312ua')
bot.auth()
values = {'out': 0,'count': 100,'time_offset': 60}
def write_msg(s):
    bot.method('messages.send', {'chat_id':1,'message':s})
def kick(id):
    adm.method('messages.removeChatUser', {'chat_id':340, 'user_id':id})
def panel():
    while True:
        response = bot.method('messages.get', values)
        if response['items']:
            values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
            if item['body']=='/admin':
                try:
                    open('status/'+str(item['user_id'])+'.txt')
                except IOError as e:
                    write_msg('Вы не админ')
                    pass
                else:
                    idd=item['user_id']
                    status=open('status/'+str(idd)+'.txt')
                    stat=status.read()
                    if stat=='Admin':
                        write_msg('1) Kick \n 2) Отмена')
                        go=True
                        while go:
                            response = bot.method('messages.get', values)
                            if response['items']:
                                values['last_message_id'] = response['items'][0]['id']
                            for item1 in response['items']:
                                if item1['user_id']==idd and item1['body']=='1':
                                    write_msg('Загружается список..')
                                    lst=adm.method('messages.getChatUsers', {'chat_id':340})
                                    num=1
                                    usersSTR=u'Выберите пользователя\n'
                                    users=[]
                                    for id in lst:
                                        user=bot.method('users.get', {'user_ids':id})
                                        users.append(user[0]['id'])
                                        usersSTR=usersSTR+str(num)+') '+user[0]['first_name']+' '+user[0]['last_name']+', '
                                        num+=1
                                    write_msg(usersSTR)
                                    while go:
                                        response = bot.method('messages.get', values)
                                        if response['items']:
                                            values['last_message_id'] = response['items'][0]['id']
                                        for item2 in response['items']:
                                            if item2['user_id']==idd and item2['body']=='/stop':
                                                go=False
                                                write_msg('Завершено')
                                                break
                                            if item2['user_id']==idd and int(item2['body'], 10)>=0 and int(item2['body'], 10)<num:
                                                adm.method('messages.removeChatUser', {'chat_id':340, 'user_id':users[int(item2['body'], 10)-1]})
                                                write_msg('Пользователь удален')
                                                break
                                    break
                                            
                                if item1['user_id']==idd and item1['body']=='2':
                                    write_msg('Завершено')
                                    go=False
                                    break
                                if item1['user_id']==idd:
                                    write_msg(u'Выберите пункт')
        panel()

