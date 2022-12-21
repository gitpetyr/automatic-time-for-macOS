import time,os
'''
测试操作系统:macOS13.1
这里出现了/Users/Petyr/Applications/上课.app 和 /Users/Petyr/Applications/下课.app
这是两个自动操作app，可以替换。
say 是MacOS下预装的命令
'''

while True:
	if(time.strftime("%H:%M",time.localtime())=="08:27"): 
		os.system("open /Users/Petyr/Applications/上课.app")# 打开“下课”自动化
	if(time.strftime("%H:%M",time.localtime())=="11:40"):
		os.system("say '马上吃饭了，出去玩一会'")              #提醒自己
		os.system("echo Athena123456yuiop | sudo -S shutdown -s now") #使电脑处于睡眠状态
	if(time.strftime("%H:%M",time.localtime())=="18:00"):
		os.system("open /Users/Petyr/Applications/下课.app")# 打开“下课”自动化
	time.sleep(5)