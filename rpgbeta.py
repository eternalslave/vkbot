# -*- coding: utf-8 -*-
import time
import vk_api
import math
import emoji
import random
vk = vk_api.VkApi(login = 'artem.ebal@yandex.ru', password = 'ukeahi312ua')
vk.auth()
values = {'out': 0,'count': 100,'time_offset': 60}
count=open('gifts/count.txt', 'r')
gifts_count=int(count.read())+1
count.close()
def status(id):
    try:
        file=open('status/'+str(item['user_id'])+'.txt', 'r')
    except IOError as e:
        file=open('status/'+str(item['user_id'])+'.txt', 'w')
        file.write('User')
        file.close()
    else:
        r=file.read()
        file.close()
        return r
def icon(lvl):
    if lvl<5:
        return emoji.emojize(':baby:', use_aliases=True)
    if lvl<10:
        return emoji.emojize(':leaves:', use_aliases=True)
    return emoji.emojize(':sunrise:', use_aliases=True)
def gifts(id):
    ret='\nGifts\n—————————————————————\n'
    try:
        gift=open('gift/'+str(id)+'.txt')
    except IOError as e:
        ret=ret+'No gifts'
    else:
        giftss=gift.read()
        gift.close()
        ret=ret+giftss
    return ret
def write_msg(s):
    vk.method('messages.send', {'chat_id':1,'message':s})
def write_msg1(s):
    vk.method('messages.send', {'chat_id':1,'message':s})
while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        try:
            file=open('gld/'+str(item['user_id'])+'.txt', 'r')
            int(float(file.read()[4:]))
        except IOError as e:
            file=open('gld/'+str(item['user_id'])+'.txt', 'w')
            file.write('gld=0')
            file.close()
        except ValueError:
            file=open('gld/'+str(item['user_id'])+'.txt', 'w')
            file.write('gld=0')
            file.close()
            print('valueeror')
        try:
            file=open('rpg/'+str(item['user_id'])+'.txt', 'r')
        except IOError as e:
            file=open('rpg/'+str(item['user_id'])+'.txt', 'w')
            file.write('exp=1')
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
                    current=int((float(gold.read()[4:])))+3**int(math.log(expN/5+1, 2))+100
                    gold.close()
                    gold=open('gld/'+str(item['user_id'])+'.txt', 'w')
                    gold.write('gld='+str(current))
                    gold.close()
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
            write_msg(u'Профиль @id'+str(item['user_id'])+' (' + vk.method('users.get', { 'user_ids':item['user_id']})[0]['first_name']+ u') '+icon(int(math.log(int(exp)/5+1, 2)))+'\nLVL: '+str(int(math.log(int(exp)/5+1, 2)))+emoji.emojize(':bust_in_silhouette:\nexp: ')+str(int(exp))+'/'+str((2**(int(math.log(int(exp)/5+1, 2))+1)-1)*5)+emoji.emojize(':books:\nGold: ')+gold[4:]+emoji.emojize(':money_with_wings:')+'\nStatus: '+status(item['user_id'])+emoji.emojize(gifts(item['user_id']), use_aliases=True))
        if item['body']=='/kit':
            try:
                file=open('gld/'+str(item['user_id'])+'_kit.txt', 'r')
            except IOError as e:
                file=open('gld/'+str(item['user_id'])+'_kit.txt', 'w')
                file.write(str(time.time()))
                file.close()
                file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                gold=file.read()
                gold=int(float(gold[4:]))
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
        if item['body'][0:6]=='/play ':
            try:
                int(item['body'][6:])
            except ValueError:
                write_msg('Можно играть только на целые числа')
            else:
                if random.randint(0,1):
                    win=random.randint(50, 150)
                    file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                    gold=file.read()
                    gold=int(float(gold[4:]))
                    file.close()
                    if gold>=int(float(item['body'][6:])) and int(float(item['body'][6:]))>0:
                        file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                        file.write('gld='+str(gold+int(int(item['body'][6:])*(win/100))))
                        print(str(int(int(item['body'][6:])*(win/100))))
                        file.close()
                        write_msg('Победа! +'+str(int(int(item['body'][6:])*(win/100))))
                else:
                    file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                    gold=file.read()
                    gold=int(gold[4:])
                    file.close()
                    if gold>=int(float(item['body'][6:])) and int(float(item['body'][6:]))>0 :
                        file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                        file.write('gld='+str(gold-int(item['body'][6:])))
                        file.close()
                        write_msg('Поражение :(')
        if item['body'][0:6]=='/give ':
            gg=item['body'][6:].split()
            if float(gg[1])>0:
                try:
                    int(gg[1])
                except ValueError:
                    write_msg('Допустимы только целые числа')
                else:
                    try:
                        open('gld/'+str(item['user_id'])+'.txt', 'r')
                    except IOErros as e:
                        give=open('gld/'+str(item['user_id'])+'.txt', 'w')
                        give.write('gld=0')
                        give.close()
                    try:
                        open('gld/'+str(gg[0])+'.txt', 'r')
                    except IOError as e:
                        write_msg('Ошибка! /give [id] [кол-во]')
                    else:
                        give=open('gld/'+str(item['user_id'])+'.txt', 'r')
                        ggold=int(give.read()[4:])
                        give.close()
                        if ggold>int(gg[1]):
                            take=open('gld/'+str(gg[0])+'.txt', 'r')
                            tgold=int(take.read()[4:])
                            take.close()
                            give=open('gld/'+str(item['user_id'])+'.txt', 'w')
                            give.write('gld='+str(ggold-int(gg[1])))
                            take=open('gld/'+gg[0]+'.txt', 'w')
                            take.write('gld='+str(tgold+int(gg[1])))
                            give.close()
                            take.close()
                            write_msg('Успешно!')
        if item['body'][0:6]=='/gift ':
            if item['body'][6:10]=='list':
                i=1
                gstr=''
                while i<gifts_count:
                    file=open('gifts/'+str(i)+'.txt')
                    gstr=gstr+str(i)+') '+file.readline()+'Cost: '+file.readline()+'\n'
                    file.close()
                    i+=1
                write_msg(emoji.emojize(gstr, use_aliases=True))
            else:
                gift=item['body'][6:].split()
                try:
                    int(gift[0])
                    int(gift[1])
                except:
                    write_msg('Ошибка! \n/gift [id] [id подарка]\n/gift list - список подарков')
                else:
                    if int(gift[1])>gifts_count or int(gift[1])<1 or item['user_id']==int(gift[0]):
                        write_msg('Ошибка! \n/gift [id] [id подарка]\n/gift list - список подарков\nСебе подарки дарить нельзя')
                    else:
                        pod=open('gifts/'+gift[1]+'.txt', 'r')
                        smile=pod.readline()
                        smile=smile[0:len(smile)-1]
                        cost=int(pod.readline())
                        pod.close()
                        give=open('gld/'+str(item['user_id'])+'.txt', 'r')
                        gold=int(give.read()[4:])
                        give.close()
                        if gold>cost:
                            try:
                                open('gift/'+gift[0]+'.txt', 'r')
                            except IOError as e:
                                open('gift/'+gift[0]+'.txt', 'w')
                            take=open('gift/'+gift[0]+'.txt', 'r')
                            takel=take.read()
                            take.close()
                            take=open('gift/'+gift[0]+'.txt', 'w')
                            take.write(takel+smile+' ')
                            take.close()
                            give=open('gld/'+str(item['user_id'])+'.txt', 'w')
                            give.write('gld='+str(gold-cost))
                            give.close()
                            write_msg('Подарок отправлен! +'+emoji.emojize(smile, use_aliases=True))
                        
                    
            
                        
            
            
            
                
                
