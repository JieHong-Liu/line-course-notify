from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime
import os

# # 宣告一個排程
sched = BlockingScheduler()

# # 定義排程 : 在周一至周五，每分鐘就做一次 def scheduled_jog()

# print(datetime.datetime.now().ctime())


@sched.scheduled_job('interval', minutes=2)
def scheduled_job():
    print('awake app every minutes.')
    os.system("gunicorn app:app")
# 感謝大大救我一命:https://ivanjo39191.pixnet.net/blog/post/179453201-python-django-%E5%AF%A6%E4%BD%9C%28%E4%B8%89%29-%E7%94%A8-abschedule-%E5%9C%A8-heroku-%E5%BE%8C%E5%8F%B0


sched.start()
