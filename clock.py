from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime
import os

# # 宣告一個排程
sched = BlockingScheduler()

# # 定義排程 : 在周一至周五，每分鐘就做一次 def scheduled_jog()

# print(datetime.datetime.now().ctime())


@sched.scheduled_job('interval', minutes=1)
def scheduled_job():
    print('awake app every minutes.')
    os.system("python app.py")


sched.start()
