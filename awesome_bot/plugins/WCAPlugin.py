import requests
import socket
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
from bs4 import BeautifulSoup as BS


'''
The MIT License (MIT)
Copyright (c) 2020 Pan Qiming

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''


def getHTMLText(url):
    kv = {'user-agent': 'Mozilla/5.0'}
    try:
        r = requests.get(url, timeout=30, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getPersonList(personList, html):
    soup = BS(html, 'html.parser')
    count = 0
    for tr in soup.tbody.find_all('tr'):
        try:
            personList.append(
                [tr.td.div.label.input['data-name'], tr.td.div.label.input['data-id']])
            count += 1
        except AttributeError:
            continue
    return count


def getPersonURL(personList):
    rootURL = 'https://cubingchina.com/results/person/'
    for eachPerson in personList:
        eachPerson.append(rootURL+eachPerson[1])


def getPersonInfo(personList):
    for eachPerson in personList:
        html = getHTMLText(eachPerson[2])
        soup = BS(html, 'html.parser')
        eventsDict = {}

        trList = soup.tbody.find_all('tr')
        trList = list(trList)
        for example in trList:
            try:
                if len(example('a')) == 3:
                    eventsDict[example.td.i['title']] = [
                        example('a')[1].string, example('a')[2].string]
                elif len(example('a')) == 2:
                    eventsDict[example.td.i['title']] = [
                        example('a')[1].string, ' ']
            except:
                continue
        eachPerson.append(eventsDict)
        return


wca = on_command("wca",priority=5)
@wca.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args:
        state["person"] = args


@wca.got("person", prompt="你想查神马...")
async def handle_persom(bot: Bot, event: Event, state: dict):
    personname = state["person"]
    person_wca = await get_wca(personname)
    await wca.finish(person_wca)


async def get_wca(personname: str):
    socket.setdefaulttimeout(3)
    try:
        rootURL = 'https://cubingchina.com/results/person?region=World&gender=all&name='
        personList = []
        num = int()
        resultHTML = getHTMLText(rootURL+personname)
        num = getPersonList(personList, resultHTML)
        getPersonURL(personList)
        getPersonInfo(personList)
        if num == 1:
            personinfo = ''
            personinfo2 = ''
            for person in personList:
                personinfo += person[0]+'\n'+person[1]+'\n'
                for item in person[3].keys():
                    personinfo2 += item+'  '+person[3][item][0]+'|'+person[3][item][1]+'\n'
            return f""+str(personinfo)+str(personinfo2)
        else:
            itemsinfo = ''
            items = str(len(personList))+' items\n'
            for i in range(4):
                try:
                    itemsinfo += str(i+1)+' | '+str(personList[i][0])+'\n'+str(personList[i][1])+'\n------\n'
                except IndexError:
                    return f'木有这位外星人...'
            return f""+items+itemsinfo
    except:
        return f'请求超时，网络错误...'
        
context = on_command("近期赛事",priority=5)
@context.handle()
async def contextsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '近期赛事如下：\n1.深圳魔方早安赛    2020-11-15\n2.深圳魔方午安赛    2020-11-15\n回复“.赛事 编号”可查看信息'
    )
    

cont1 = on_command("赛事 1",priority=5)
@cont1.handle()
async def cont1send(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '深圳魔方早安赛\n2020-11-15\n三阶、二阶、单手、金字塔、斜转\n南山区蛇口湾厦路126号电子创新服务基地2期1楼会议室\n[CQ:image,file=edb3f7b7a0ab84749e9681fb9f0eef23.image]'
    )


cont2 = on_command("赛事 2",priority=5)
@cont2.handle()
async def cont2send(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '深圳魔方午安赛\n2020-11-15\n三阶、二阶、单手、金字塔、斜转\n南山区蛇口湾厦路126号电子创新服务基地2期1楼会议室\n[CQ:image,file=edb3f7b7a0ab84749e9681fb9f0eef23.image]'
    )
