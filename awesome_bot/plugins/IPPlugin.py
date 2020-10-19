from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import requests


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


ipname = on_command("ip", priority=5)
@ipname.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args:
        state["ipname"] = args


@ipname.got("ipname", prompt="你想查神马...")
async def handle_city(bot: Bot, event: Event, state: dict):
    ipinfo = state["ipname"]
    ip_info = await get_ipinfo(ipinfo)
    await ipname.finish(ip_info)


async def get_ipinfo(ipinfo: str):
    ip = ipinfo
    url = 'http://ip-api.com/json/' + ip
    response = requests.get(url)
    strpp = {}
    strpp = response.json()
    try:
        return f'IP : ' + strpp['query']+'\nContry : ' + strpp['country']+'\nProvince : ' + strpp['regionName'] + '\nCity : ' + strpp['city'] + '\nLongitude : ' + str(strpp['lon'])+'\nLatitude : ' + str(strpp['lat'])+'\nISP : ' + strpp['isp']+'\nORG : ' + strpp['org']
    except Exception as e:
        return f"你的IP地址输入有误：{e}"
