from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event

weather = on_command("测试", priority=5)
@weather.handle()
async def test(bot: Bot, event: Event, state: dict):
    await bot.send(
        event=event,
        message = "测试发送信息"
    )
    await bot.send(
        event=event,
        message = "测试发送信息"
    )
    await bot.send(
        event=event,
        message = "测试发送信息"
    )
    
