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


explain = on_command("使用说明", priority=5)
@explain.handle()
async def explainsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message='使用说明网址：\nhttp://106.52.134.219:8081/'
    )


applicion = on_command("申请雨木", priority=5)
@applicion.handle()
async def applicionsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message='申请机器人网址：\nhttps://www.wenjuan.com/s/UZBZJvSiok/'
    )


opensource = on_command("开源", priority=5)
@opensource.handle()
async def opensourcesend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message='雨木机器人已开放部分源码，网址：\nhttps://gitee.com/pan_chi_ming/rainmuk_open'
    )


cfop = on_command("cfop", priority=5)
@cfop.handle()
async def cfopsend(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = '[CQ:image,file=9d68078d5880e8acaa71e0c9c1ebac07.image,url=http://c2cpicdw.qpic.cn/offpic_new/2637087493//2637087493-601208238-9D68078D5880E8ACAA71E0C9C1EBAC07/0?term=2]'
    )
