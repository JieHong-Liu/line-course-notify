import requests
from bs4 import BeautifulSoup
import json

header = {
    "origin": "https://querycourse.ntust.edu.tw",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40",
    "content-type": "application/json; charset=utf-8",
    "cookie": "_ga = GA1.3.1074523563.1555171596 _gid = GA1.3.14635500021600065844_gat_gtag_UA_134331597_1 = 1",
    "referer": "https://querycourse.ntust.edu.tw/querycourse/"
}
url = "https://querycourse.ntust.edu.tw/querycourse/api/courses"
payload = '{"Semester":"1091","CourseNo":"","CourseName":"人工智慧","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":0,"OnlyGeneral":0,"OnleyNTUST":0,"OnlyMaster":0,"OnlyUnderGraduate":0,"OnlyNode":0,"Language":"zh"}'

x = requests.post(url, headers=header, data=payload.encode('utf-8'))

print(x.text)
