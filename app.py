from bs4 import BeautifulSoup
import json
import requests
import time
from flask import *

app = Flask(__name__)
# if __name__ == '__main__':
#     app.run()  # correct one -> use app in all lower case


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    massage = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=massage)
    return r.status_code


token = 'yRbTBLap7Oxm1wZdy221LH422OlJqpfJRVzO80v5vtg'  # 權杖值

url = 'https://querycourse.ntust.edu.tw/querycourse/api/courses'
payload = "{'Semester': '1091', 'CourseNo': 'FE2172701', 'CourseName': '', 'CourseTeacher': '',      'Dimension': '', 'CourseNotes': '','ForeignLanguage': 0, 'OnlyGeneral': 0, 'OnleyNTUST': 0, 'OnlyMaster': 0, 'OnlyUnderGraduate': 0, 'OnlyNode': 0, 'Language': 'zh'}"
# 日文＝'FE2172701',
header = {
    "origin": "https://querycourse.ntust.edu.tw",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40",
    "content-type": "application/json; charset=utf-8",
    "cookie": "_ga = GA1.3.1074523563.1555171596 _gid = GA1.3.14635500021600065844_gat_gtag_UA_134331597_1 = 1",
    "referer": "https://querycourse.ntust.edu.tw/querycourse/"
}
yeah = True
while(yeah):
    resp = requests.post(url, data=payload.encode('utf-8'), headers=header)
    json_file = json.loads(resp.text)
    numOfStudent = json_file[0]['ChooseStudent']
    print('現在的選課人數為' + str(numOfStudent))
    if int(numOfStudent) < int(json_file[0]['Restrict1']):
        yeah = False
        message = '現在的選課人數為'+str(numOfStudent)+' 人，上限制人數為，請盡快加簽'
        lineNotifyMessage(token, message)
    time.sleep(1)
