import requests
import socket
import json
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
    url = 'http://wcads.lz1998.xin/wcaPerson/searchPeople?q='+personname
    strhtml = requests.get(url)
    html = json.loads(strhtml.text)
    data = html['data']
    if len(data) == 1:
        idname = data[0]['id']
        url1 = 'http://wcads.lz1998.xin/wcaSingle/findBestResultsByPersonId?personId=' + idname
        strhtml1 = requests.get(url1)
        html1 = json.loads(strhtml1.text)
        data1 = html1['data']
        url2 = 'http://wcads.lz1998.xin/wcaAverage/findBestResultsByPersonId?personId=' + idname
        strhtml2 = requests.get(url2)
        html2 = json.loads(strhtml2.text)
        data2 = html2['data']
        info1 = '单次：\n'
        for i in range(len(data1)):
            info1 += data1[i]['eventId'] + '    ' + \
                str(float(data1[i]['best']) / 100) + '\n'
        info2 = '平均：\n'
        for i in range(len(data2)):
            info2 += data2[i]['eventId'] + '    ' + \
                str(float(data2[i]['best']) / 100) + '\n'
        send = info1+info2
        return send
    elif len(data) > 1:
        item = str(len(data))+'items\n'
        info = ''
        for i in range(6):
            info += data[i]['name'] + '   ||  ' + data[i]['id'] + '\n'
        send = item+info
        return send
    elif len(data) == 0:
        return f"木有这位外星人..."



context = on_command("近期赛事",priority=5)
@context.handle()
async def contextsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '正在更新...'
    )
    

cont1 = on_command("赛事 1",priority=5)
@cont1.handle()
async def cont1send(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message='正在更新...'
    )


cont2 = on_command("赛事 2",priority=5)
@cont2.handle()
async def cont2send(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message='正在更新...'
    )
