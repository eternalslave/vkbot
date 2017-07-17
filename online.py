# -*- coding: utf-8 -*-
import vk_api
import time
vk = vk_api.VkApi(login = 'artem.ebal@yandex.ru', password = 'ukeahi312ua')
vk.auth()
def online():
    g=0
    on=vk.method('messages.getChatUsers', {'chat_id':1, 'fields':'online'})
    for i in on:
        if i['online']:
            g+=1
    vk.method('status.set', {'text':u'Текущий Online: '+str(g), 'group_id':150358061})
    time.sleep(30)
online()
