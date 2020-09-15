from apscheduler.schedulers.blocking import BlockingScheduler
import urllib

# 宣告一個排程
sched = BlockingScheduler()

# 定義排程 : 在周一至周五，每 1 分鐘就做一次 def scheduled_jog()


@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/1')
def scheduled_job():
    url = "https://line-course-notify.herokuapp.com/"
    connect = urllib.request.urlopen(url)


sched.start()  # 啟動排程
