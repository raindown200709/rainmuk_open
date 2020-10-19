import json,requests
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event


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


express = on_command("查快递", priority=5)
@express.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["number"] = args  # 如果用户发送了参数则直接赋值


@express.got("number", prompt="你想查询神马...")
async def handle_city(bot: Bot, event: Event, state: dict):
    number = state["number"]
    number_express = await get_express(number)
    await express.finish(number_express)


async def get_express(number: str):
    try:
        packageNum = number
        url1 = 'http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum
        #用url1查询运单号对应的快递公司，如中通，返回：zhongtong。
        companyName = json.loads(requests.get(url1).text)['auto'][0]['comCode']
        #在用url2查询和运单号、快递公司来查询快递详情，结果是一个json文件，用dict保存在resultdict中。
        url2 = 'http://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum #还有个temp字段加不加都可以。如：'&temp=0.9829438147420106'
        for item in json.loads(requests.get(url2).text)['data']:
            track = item['time'],item['context'] + '\n'
            return track
    except Exception as e: 
         return f"查询快递单号错误：{e}"
