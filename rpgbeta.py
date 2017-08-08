# -*- coding: utf-8 -*-
import time
import vk_api
import math
import emoji
import random
import os
vk = vk_api.VkApi(login = 'artem.ebal@yandex.ru', password = 'ukeahi312ua')
vk.auth()
adm = vk_api.VkApi(login = 'dark.fusrodah@gmail.com', password = 'srn1wpua')
adm.auth()
values = {'out': 0,'count': 100,'time_offset': 60}
gifts_count=len(os.listdir('gifts/'))+1
doms_count=len(os.listdir('doms/'))+1
def petprof(id):
    try:
        file=open('pet/'+str(id)+'.txt')
    except IOError:
        return 'Has no pet'
    else:
        pet_id=file.readline()
        pet_id=pet_id[0:len(pet_id)-1]
        exp=file.readline()
        exp=exp[0:len(exp)-1]
        file.close()
        file=open('pets/'+pet_id+'.txt')
        pet_name=file.readline()
        pet_name=pet_name[0:len(pet_name)-1]
        return 'Pet: '+emoji.emojize(pet_name, use_aliases=True)+'['+str(exp)+']'
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
                write_msg(u'Добро пожаловать в Slavery, '+us[0]['first_name']+u'! \n/help - Спиок комманд\nПодпишись на нашь паблик - https://vk.com/dobropojalovatv12')
            vk.method('account.banUser', {'user_id':id})
def namer():
    title=adm.method('messages.getChat', {'chat_id':340})
    if title['title']!=u'Slavery BETA':
        vk.method('messages.editChat', {'chat_id':1, 'title':u'Slavery BETA'})
def marriage(id):
    try:
        m=open('marriage/'+str(id)+'.txt')
    except IOError as e:
        return 'Marital Status: Single :broken_heart:'
    else:
        id=m.read()
        return 'Marital Status: @id'+id+'(Married) :heart:'
def get_money(id):
    try:
        doms=open('dom/'+str(id)+'.txt', 'r')
    except IOError as e:
        pass
    else:
        try:
            timer=open('dom/'+str(id)+'_timer.txt', 'r')
        except IOError as e:
            timer=open('dom/'+str(id)+'_timer.txt', 'w')
            timer.write(str(time.time()))
        else:
            times=int((int(time.time())-int(float(timer.read())))/60)
            timer.close()
            timer=open('dom/'+str(id)+'_timer.txt', 'w')
            timer.write(str(time.time()))
            timer.close()
            domss=[]
            while True:
                l=doms.readline()
                if l=='':
                    break
                domss.append(l[0:len(l)-1])
            expF=0
            moneyF=0
            for dom in domss:
                file=open('doms/'+str(dom)+'.txt')
                file.readline()
                file.readline()
                expF=expF+int(file.readline())
                moneyF=moneyF+int(file.readline())
                file.close()
            file=open('rpg/'+str(id)+'.txt')
            expF=expF*times
            cexp=int(float(file.read()[4:]))
            file.close()
            file=open('rpg/'+str(id)+'.txt', 'w')
            file.write('exp='+str(expF+cexp))
            file.close()
            file=open('gld/'+str(id)+'.txt')
            moneyF=moneyF*times
            cmoney=int(float(file.read()[4:]))
            file.close()
            file=open('gld/'+str(id)+'.txt', 'w')
            file.write('gld='+str(moneyF+cmoney))
            file.close()
            write_msg('Получено:\nexp: '+str(expF)+'\nGold: '+str(moneyF)+'\nЗа последние '+str(times)+' минут')
def doms(id):
    r='Own: '
    try:
        pod=open('dom/'+str(id)+'.txt', 'r')
    except IOError as e:
        return r+'nothing'
    else:
        domes=[]
        i=1
        while i<=doms_count-1:
            domes.append(0)
            i+=1
        while True:
            l=pod.readline()
            l=l[0:len(l)-1]
            if l=='':
                break
            domes[int(l)-1]+=1
        i=1
        while i<=doms_count-1:
            if domes[i-1]>0:
                file=open('doms/'+str(i)+'.txt')
                r=r+file.readline()
                r=r[0:len(r)-1]+'[x'+str(domes[i-1])+']; '
                file.close()
            i+=1
        return r

        
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
        if r=='Admin':
            return r+' '+emoji.emojize(':hammer:', use_aliases=True)
        return r
def icon(lvl):
    r=''
    high=False
    try:
        int(str(lvl)[0:len(str(lvl))-1])
    except ValueError:
        pass
    else:
        high=True
        if int(str(lvl)[0:len(str(lvl))-1])==1:
            r=':sparkles:'
        if int(str(lvl)[0:len(str(lvl))-1])==2:
            r=':boom:'
        if int(str(lvl)[0:len(str(lvl))-1])==3:
            r=':star:'
    lvl=int(str(lvl)[len(str(lvl))-1:])
    if high==False:
        if lvl<5:
            return emoji.emojize(':baby:', use_aliases=True)
        if lvl==5:
            return emoji.emojize(':leaves:', use_aliases=True)
        if lvl==6:
            return emoji.emojize(':four_leaf_clover:', use_aliases=True)
        if lvl==7:
            return emoji.emojize(':hibiscus:', use_aliases=True)
        if lvl==8:
            return emoji.emojize(':zap:', use_aliases=True)
        if lvl==9:
            return emoji.emojize(':cloud:', use_aliases=True)
    if lvl==0:
        return emoji.emojize(r+':leaves:', use_aliases=True)
    if lvl==1:
        return emoji.emojize(r+':four_leaf_clover:', use_aliases=True)
    if lvl==2:
        return emoji.emojize(r+':hibiscus:', use_aliases=True)
    if lvl==3:
        return emoji.emojize(r+':zap:', use_aliases=True)
    if lvl==4:
        return emoji.emojize(r+':cloud:', use_aliases=True)
    if lvl==5:
        return emoji.emojize(r+':crescent_moon:', use_aliases=True)
    if lvl==6:
        return emoji.emojize(r+':ocean:', use_aliases=True)
    if lvl==7:
        return emoji.emojize(r+':city_sunset:', use_aliases=True)
    if lvl==8:
        return emoji.emojize(r+':japanese_castle:', use_aliases=True)
    if lvl==9:
        return emoji.emojize(r+':volcano:', use_aliases=True)
def gifts(id):
    ret='\nGifts\n——————————————————————\n'
    try:
        gift=open('gift/'+str(id)+'.txt')
    except IOError as e:
        ret=ret+'No gifts'
    else:
        giftss=gift.read()
        gift.close()
        ret=ret+giftss
    return ret+'\n——————————————————————'
def write_msg(s):
    try:
        vk.method('messages.send', {'chat_id':1,'message':s})
    except:
        adm.method('messages.send', {'chat_id':340, 'message':'Рестарт бота через 5 минут'})
        time.sleep(60*5)
        print(u'Капча')
def write_msgp(s, id):
    try:
        file=open('photo/'+str(id)+'.txt')
    except IOError as e:
        try:
            vk.method('messages.send', {'chat_id':1,'message':s})
        except:
            adm.method('messages.send', {'chat_id':340, 'message':'Рестарт бота через 5 минут'})
            time.sleep(60*5)
            print(u'Капча')
    else:
        try:
            music=open('faudio/'+str(id)+'.txt')
        except IOError as e:
            try:
                vk.method('messages.send', {'chat_id':1,'message':s, 'attachment':file.read()})
            except:
                adm.method('messages.send', {'chat_id':340, 'message':'Рестарт бота через 5 минут'})
                time.sleep(60*5)
                print(u'Капча')
        else:
            try:
                vk.method('messages.send', {'chat_id':1,'message':s, 'attachment':file.read()+','+music.read()})
            except:
                adm.method('messages.send', {'chat_id':340, 'message':'Рестарт бота через 5 минут'})
                time.sleep(60*5)
                print(u'Капча')
            music.close()
        file.close()
while True:
    adder()
    namer()
    try:
        response = vk.method('messages.get', values)
        if response['items']:
            values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
            try:
                file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                int(float(file.read()[4:]))
            except IOError as e:
                file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                file.write('gld=4000')
                file.close()
            except ValueError:
                file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                file.write('gld=4000')
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
                try:
                    write_msgp(u'Профиль @id'+str(item['user_id'])+' (' + vk.method('users.get', { 'user_ids':item['user_id']})[0]['first_name']+ u') '+icon(int(math.log(int(exp)/5+1, 2)))+'\nLVL: '+str(int(math.log(int(exp)/5+1, 2)))+emoji.emojize(':bust_in_silhouette:\nexp: ')+str(int(exp))+'/'+str((2**(int(math.log(int(exp)/5+1, 2))+1)-1)*5)+emoji.emojize(':books:\nGold: ')+gold[4:]+emoji.emojize(':moneybag:', use_aliases=True)+'\n'+emoji.emojize(marriage(item['user_id']), use_aliases=True)+'\n'+emoji.emojize(doms(item['user_id']), use_aliases=True)+'\n'+petprof(item['user_id'])+'\nStatus: '+status(item['user_id'])+emoji.emojize(gifts(item['user_id']), use_aliases=True), item['user_id'])
                except TypeError:
                    pass
            if item['body'][0:4]=='/kit':
                try:
                    file=open('gld/'+str(item['user_id'])+'_kit.txt', 'r')
                except IOError as e:
                    file=open('gld/'+str(item['user_id'])+'_kit.txt', 'w')
                    file.write(str(time.time()))
                    file.close()
                    file=open('rpg/'+str(item['user_id'])+'.txt', 'r')
                    exp=int(float(file.read()[4:]))
                    file.close()
                    file=open('gld/'+str(item['user_id'])+'.txt', 'r')
                    gold=file.read()
                    gold=int(float(gold[4:]))
                    file.close()
                    file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                    file.write('gld='+str(gold+25+int(math.log(int(exp)/5+1, 2))**3))
                    file.close()
                    write_msg('+'+str(25+int(math.log(int(exp)/5+1, 2))**3)+'gold')
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
                        file=open('rpg/'+str(item['user_id'])+'.txt', 'r')
                        exp=int(float(file.read()[4:]))
                        file.close()
                        file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                        file.write('gld='+str(gold+25+int(math.log(int(exp)/5+1, 2))**3))
                        file.close()
                        write_msg('+'+str(25+int(math.log(int(exp)/5+1, 2))**3)+'gold')
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
                        else:
                            write_msg('Недостаточно средтв')
            if item['body'][0:6]=='/give ':
                gg=item['body'][6:].split()
                try:
                    int(float(gg[1]))
                    int(float(gg[0]))
                except ValueError:
                    write_msg('Допустимы только целые числа')
                except IndexError:
                    write_msg('Ошибка! /give [id] [кол-во]')
                else:
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
                                if ggold>=int(gg[1]):
                                    take=open('gld/'+str(gg[0])+'.txt', 'r')
                                    tgold=int(take.read()[4:])
                                    take.close()
                                    expf1=open('rpg/'+str(item['user_id'])+'.txt', 'r')
                                    exp1=int(float(expf1.read()[4:]))
                                    expf1.close()
                                    expf2=open('rpg/'+gg[0]+'.txt', 'r')
                                    exp2=int(float(expf2.read()[4:]))
                                    expf2.close()
                                    pr=0
                                    if exp2<exp1:
                                        pr=int(math.log(int(exp1)/5+1, 2))-int(math.log(int(exp2)/5+1, 2))
                                        if pr>10:
                                            pr=0.99
                                        else:
                                            pr=pr/10
                                    give=open('gld/'+str(item['user_id'])+'.txt', 'w')
                                    give.write('gld='+str(ggold-int(gg[1])))
                                    take=open('gld/'+gg[0]+'.txt', 'w')
                                    take.write('gld='+str(tgold+(int(float(gg[1])*(1-pr)))))
                                    give.close()
                                    take.close()
                                    write_msg('Успешно! Комиссия: '+str(pr*100)+'%')
                                else:
                                    write_msg('Недостаточно средств')
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
            if item['body'][0:5]=='/buy ':
                if item['body'][5:9]=='list':
                    i=1
                    gstr='Список имуществ для покупки: \n'
                    while i<doms_count:
                        file=open('doms/'+str(i)+'.txt')
                        gstr=gstr+str(i)+') '+file.readline()+'Cost: '+file.readline()+'Exp/min: '+ file.readline()+'Money/min: '+file.readline()+'\n'
                        file.close()
                        i+=1
                    write_msg(emoji.emojize(gstr, use_aliases=True))
                else:
                    try:
                        dom=int(item['body'][5:])
                    except ValueError:
                        write_msg('Ошибка!\n/buy [id имущества]\n/buy list - список имуществ')
                    else:
                        if doms_count<=dom or dom<=0:
                            write_msg('/buy list - список имущества')
                        else:
                            pod=open('doms/'+str(dom)+'.txt')
                            name=pod.readline()
                            cost=pod.readline()
                            cost=int(cost[0:len(cost)-1])
                            pod.close()
                            g=open('gld/'+str(item['user_id'])+'.txt')
                            gold=int(g.read()[4:])
                            g.close()
                            if gold>=cost:
                                try:
                                    open('dom/'+str(item['user_id'])+'.txt', 'r')
                                except IOError as e:
                                    pod=open('dom/'+str(item['user_id'])+'.txt', 'w')
                                    pod.close()
                                pod=open('dom/'+str(item['user_id'])+'.txt', 'r')
                                lst=pod.read()
                                pod.close()
                                pod=open('dom/'+str(item['user_id'])+'.txt', 'r')
                                i=1
                                ok=True
                                while True:
                                    chek=pod.readline()
                                    if chek=='':
                                        break
                                    if (chek[0:len(chek)-1]=='2' or chek[0:len(chek)-1]=='3')and chek[0:len(chek)-1]==str(dom):
                                        ok=False
                                        break
                                pod.close()
                                if ok:
                                    get_money(item['user_id'])
                                    g=open('gld/'+str(item['user_id'])+'.txt')
                                    gold=int(g.read()[4:])
                                    g.close()
                                    pod=open('dom/'+str(item['user_id'])+'.txt', 'w')
                                    current=lst+str(dom)+'\n'
                                    pod.write(current)
                                    pod.close()
                                    g=open('gld/'+str(item['user_id'])+'.txt', 'w')
                                    g.write('gld='+str(gold-cost))
                                    g.close()
                                    write_msg('Вы приобрели: '+emoji.emojize(name, use_aliases=True))
                                else:
                                    file=open('doms/'+chek[0:len(chek)-1]+'.txt')
                                    chek=file.readline()
                                    file.close()
                                    write_msg('У вас уже есть '+emoji.emojize(chek[0:len(chek)-1], use_aliases=True))
                            else:
                                write_msg('Недостаточно средств!')
            if item['body']=='/withdraw':
                get_money(item['user_id'])
            if item['body'][0:9]=='/marriage' and str(item['user_id'])!=item['body'][10:]:
                try:
                    int(item['body'][10:])
                except ValueError:
                    write_msg('Ошибка! /marriage [id]')
                else:
                    id1=str(item['user_id'])
                    id2=item['body'][10:]
                    try:
                        open('marriage/'+id1+'.txt')
                    except IOError as e:
                        try:
                            open('marriage/'+id2+'.txt')
                        except IOError as e:
                            gold=open('gld/'+id1+'.txt')
                            gold=gold.read()[4:]
                            if int(gold)>=50000:
                                body=vk.method('users.get', {'user_ids':id1+', '+id2})
                                write_msg('Ожидание ответа от '+body[1]['first_name']+'. Осталось 5 секунд')
                                mtime=time.time()
                                while True:
                                    if time.time()-mtime>5:
                                        break
                                    response = vk.method('messages.get', values)
                                    if response['items']:
                                        values['last_message_id'] = response['items'][0]['id']
                                    for item in response['items']:
                                        if int(item['user_id'])==int(id2) and item['body']=='/accept':
                                            m1=open('marriage/'+str(id1)+'.txt', 'w')
                                            m1.write(id2)
                                            m2=open('marriage/'+str(id2)+'.txt', 'w')
                                            m2.write(id1)
                                            m1.close()
                                            m2.close()
                                            write_msg('Успешно!')
                                            goldw=open('gld/'+id1+'.txt', 'w')
                                            goldw.write('gld='+str(int(float(gold))-50000))
                                            goldw.close()
                            else:
                                write_msg('Для свадьбы требуется 50000gold!')
                        else:
                            write_msg(id2+'уже занят!')
                    else:
                        write_msg('Вы уже заняты!')
            if item['body']=='/break':
                try:
                    m=open('marriage/'+str(item['user_id'])+'.txt')
                except IOError as e:
                    write_msg('Вы и так свободны!')
                else:
                    idd=m.read()
                    m.close()
                    os.remove('marriage/'+str(idd)+'.txt')
                    os.remove('marriage/'+str(item['user_id'])+'.txt')
                    write_msg('Успешно!')
            if item['body']=='/id':
                write_msg(str(item['user_id']))
            if item['body']=='/help':
                write_msg('Список комманд:\n/profile - посмотреть свой профиль\n/play [кол-во] - сделать ставку\n/kit - деньги каждые 15 минут(кол-во зависит от уровня)\n/withdraw - получить деньги за имущества\n/buy [id]/list - купить имущество/список имуществ\n/give [id] [кол-во] - передать деньги(КОМИССИЯ ЗА РАЗНИЦУ В УРОВНЯХ)\n/gift [id] [id подарка](/gift list - список подарков)\n/marriage [id] - пожениться(цель должна будет написать /accept)(/break - развод)')
            if item['body'][0:5]=='/pet ':
                petc=item['body'].split()
                if petc[1]=='catch':
                    try:
                        open('pet/'+str(item['user_id'])+'.txt')
                    except IOError as e:
                        file=open('gld/'+str(item['user_id'])+'.txt')
                        gold=int(file.read()[4:])
                        file.close()
                        if gold>=10000:
                            win=random.randint(1, 100)
                            petn=1
                            if win>60:
                                petn=2
                            if win>89:
                                petn=3
                            file=open('pet/'+str(item['user_id'])+'.txt', 'w')
                            file.write(str(petn)+'\n0\n'+str(time.time()))
                            file.close()
                            file=open('pets/'+str(petn)+'.txt')
                            name=file.readline()
                            name=name[0:len(name)-1]
                            write_msg('Вы успещно поймали '+emoji.emojize(name, use_aliases=True))
                            file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                            file.write('gld='+str(int(gold)-10000))
                            file.close()
                        else:
                            write_msg('Требуется 10000 gold для поимки питомца')
                    else:
                        write_msg('У вас уже есть питомец')
                if petc[1]=='free':
                    try:
                        open('pet/'+str(item['user_id'])+'.txt')
                    except IOError as e:
                        write_msg('У вас нет питомца')
                    else:
                        os.remove('pet/'+str(item['user_id'])+'.txt')
                        write_msg('Ваш питомец свободен')
                if petc[1]=='sell':
                    try:
                        file=open('pet/'+str(item['user_id'])+'.txt')
                    except IOError as e:
                        write_msg('У вас нет питомца')
                    else:
                        pet_id=file.readline()
                        pet_id=pet_id[0:len(pet_id)-1]
                        exp=file.readline()
                        exp=int(exp[0:len(exp)-1])
                        file.close()
                        if exp>=15:
                            file=open('pets/'+pet_id+'.txt')
                            file.readline()
                            cost=file.readline()
                            file=open('gld/'+str(item['user_id'])+'.txt')
                            gold=file.read()[4:]
                            file.close()
                            file=open('gld/'+str(item['user_id'])+'.txt', 'w')
                            file.write('gld='+str(int(cost)+int(gold)))
                            file.close()
                        else:
                            write_msg('Ваш питомец слишком мал для продажи')
                if petc[1]=='feed':
                    try:
                        file=open('pet/'+str(item['user_id'])+'.txt')
                    except IOError as e:
                        write_msg('У вас нет питомца')
                    else:
                        pet_id=file.readline()
                        exp=file.readline()
                        timer=file.readline()
                        file.close()
                        file=open('gld/'+str(item['user_id'])+'.txt')
                        gold=int(file.readline()[4:])
                        file.close()
                        if gold>=1000:
                            if time.time()-int(float(timer[0:len(timer)-1]))>60*10:
                                file=open('pet/'+str(item['user_id'])+'.txt', 'w')
                                file.write(pet_id+str(int(exp[0:len(exp)-1])+1)+'\n'+str(time.time()))
                                file=open('gld/'+item['user_id']+'.txt', 'w')
                                file.write('gld='+str(gold-1000))
                                file.close()
                            else:
                                write_msg('Питомец проголодается через '+str(int((60*10-time.time()+int(float(timer[0:len(timer)-1])))/60))+' минут')
                        else:
                            write_msg('Требуется 1000 gold')
    except:
        adm.method('messages.send', {'chat_id':340, 'message':'Неизвестная ошибка! Рестарт бота через 15 секунд'})
        time.sleep(15)
                            

