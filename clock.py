from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import datetime


# 宣告一個排程
sched = BlockingScheduler()

# 定義排程 : 在周一至周五，每 1 分鐘就做一次 def scheduled_jog()

print(datetime.datetime.now().ctime())


@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/1')
def timed_job_awake_your_app():
    print('awake app every minute.')
    url = 'https://app.herokuapp.com/'
    r = requests.get(url)
    # print("--> r.content")
    # print(r.content)


sched.start()  # 啟動排程
