from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event


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