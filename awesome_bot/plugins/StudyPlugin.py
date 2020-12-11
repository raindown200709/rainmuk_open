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


study = on_command("study", priority=5) # 设置词库功能，并存到txt文件
@study.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args:
        state["study"] = args


@study.got("study", prompt="词库没有内容(@_@)...")
async def handle_study(bot: Bot, event: Event, state: dict):
    studytext = state["study"]
    file = open('(empty)'+str(event.group_id)+'.txt' , 'w') # 设置一个存放文件目录，将目录粘贴到(empty)上
    file.write(studytext)
    file.close()
    await bot.send(
        event=event,
        message = '设置成功'
    )


studyask = on_command("", priority=5) # 根据已有的命令回复消息
@studyask.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args:
        state[""] = args


@studyask.got("", prompt="没用找到指令...")
async def handle_studyask(bot: Bot, event: Event, state: dict):
    studyasktext = state[""]
    file = open('(empty)'+str(event.group_id)+'.txt' , 'r') # 设置一个存放文件目录，将目录粘贴到(empty)上
    studyasksend = file.read()
    file.close()
    studyasksend2 = studyasksend.split('//')
    sdutyasksend3 = str(studyasksend2[1])
    if studyasksend2[0] == studyasktext:
        await bot.send(
            event=event,
            message = sdutyasksend3
        )
    else:
            await bot.send(
            event=event,
            message = '词库内部错误，请重新设置'
        )

studylist = on_command("查看词库", priority=5)
@studylist.handle()
async def studylistsend(bot: Bot, event: Event, state: dict):
    file = open('(empty)'+str(event.group_id)+'.txt' , 'r') # 设置一个存放文件目录，将目录粘贴到(empty)上
    studylistsend = file.read()
    file.close()
    await bot.send(
        event=event,
        message='词库内容：\n'+studylistsend
    )
