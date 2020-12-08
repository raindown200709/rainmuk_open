# RainMuk_open 雨木机器人开源部分

#### LICENSE许可
[MIT](https://gitee.com/raindown/rainmuk_open/blob/master/LICENSE)

#### 介绍
使用Python NoneBot2编写，QQ协议端使用go-cqhttp

#### 使用说明

使用请下载nonebot-cli工具

```sh
pip install nonebot2[cli]
```

为防止方便，在代码添加了<kbd>bot.bat</kbd>和<kbd>bot.sh</kbd>，可以直接打开这两个运行
运行用nb run来打开，同时需要配置好QQ协议端[go-cqhttp](https://github.com/Mrs4s/go-cqhttp/releases/tag/v0.9.28)

#### 开源部分

机器人开源部分：

- [x] 内置命令 BulitInPlugin
- [x] 快递 Express
- [x] IP地址查询 IPPlugin
- [x] 打乱 ScramblePlugin
- [x] 词库学习 StudyPlugin
- [x] 测试发送信息 TestPlugin
- [x] 翻译英语单词 TransPlugin
- [x] WCA成绩查询 WCAPlugin
- [x] 天气查询 WeatherPlugin
- []  欢迎插件 WelcomePlugin

#### 附录
更新控制台：[https://gitee.com/raindown/rainmuk_open/tree/control](https://gitee.com/raindown/rainmuk_open/tree/control)

#### 感谢人员
感谢NoneBot的编写者和对我指导的人员：[低调](https://github.com/yanyongyu)、[lz1998](https://github.com/lz1998)