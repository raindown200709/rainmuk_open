from nonebot import on_command, on_notice
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


setwelcome = on_command("设置欢迎语", priority=5)
@setwelcome.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()
    if args:
        state["welcome"] = args


@setwelcome.got("welcome", prompt="你想设置神马...")
async def handle_welcome(bot: Bot, event: Event, state: dict):
    welcometext = state["welcome"]
    if len(welcometext) >= 100:
        await setwelcome.reject("错误：超过100个字符")
    file = open('C:/Users/86139/Desktop/GO-CQHTTPBOT/AweSome-Bot/awesome_bot/plugins/WelcomeSQL/'+str(event.group_id)+'.txt' , 'w')
    file.write(welcometext)
    file.close()
    await bot.send(
        event=event,
        message = '设置成功'
    )

# 群事件未写完
