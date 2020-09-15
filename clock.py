from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
import datetime
from flask import Flask


# # 宣告一個排程
sched = BlockingScheduler()

# # 定義排程 : 在周一至周五，每 1 分鐘就做一次 def scheduled_jog()

# print(datetime.datetime.now().ctime())
app = Flask(__name__)


@sched.scheduled_job('cron', minute='*/1')
def scheduled_job():
    print('awake app every minutes.')
    url = 'https://line-course-notify.herokuapp.com/'
    conn = urllib.request.urlopen(url)

    for key, value in conn.getheaders():
        print(key, value)


if __name__ == '__main__':
    sched.init_app(app)
    sched.start()
    app.run()
