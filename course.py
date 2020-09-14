import json
import requests
from bs4 import BeautifulSoup
url = 'https://querycourse.ntust.edu.tw/querycourse/api/courses'
payload = "{'Semester': '1091', 'CourseNo': 'FE2172701', 'CourseName': '', 'CourseTeacher': '',      'Dimension': '', 'CourseNotes': '','ForeignLanguage': 0, 'OnlyGeneral': 0, 'OnleyNTUST': 0, 'OnlyMaster': 0, 'OnlyUnderGraduate': 0, 'OnlyNode': 0, 'Language': 'zh'}"
header = {
    "origin": "https://querycourse.ntust.edu.tw",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40",
    "content-type": "application/json; charset=utf-8",
    "cookie": "_ga = GA1.3.1074523563.1555171596 _gid = GA1.3.14635500021600065844_gat_gtag_UA_134331597_1 = 1",
    "referer": "https://querycourse.ntust.edu.tw/querycourse/"
}
resp = requests.post(url, data=payload.encode('utf-8'), headers=header)
json_file = json.loads(resp.text)
numOfStudent = json_file[0]['Restrict1']
if int(numOfStudent) <= 30:
    print('現在的選課人數為'+numOfStudent+'，請盡快加簽')
