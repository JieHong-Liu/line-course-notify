import json
import requests
from bs4 import BeautifulSoup
url = 'https://querycourse.ntust.edu.tw/querycourse/api/courses'
payload = '{"Semester":"1091","CourseNo":"FE2172701","CourseName":"","CourseTeacher":"","Dimension":"","CourseNotes":"","ForeignLanguage":0,"OnlyGeneral":0,"OnleyNTUST":0,"OnlyMaster":0,"OnlyUnderGraduate":0,"OnlyNode":0,"Language":"zh"}'
header = {
    "origin": "https://querycourse.ntust.edu.tw",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40",
    "content-type": "application/json; charset=utf-8",
    "cookie": '_ga=GA1.3.275763787.1581570015; _gid=GA1.3.2070632770.1600005885; .ASPXAUTH=4D9C3DB6A8E2D452B095E9B977C6CE0CAF7FF581B032813FF906E177291E80588670F4C0D7C028AFAEE9BA4AADEFB2B4FFBC6C691774CE1E0E3A2D8B07442D8676B83D201DFE400868478EE66D8D696205A737096E4068B435D1CB24DA3B6F45917F6A4F29FCCED8F34C6E56CABCAF40112B1F93C38D1D1ADC08561A7E131167BC9792F44DDB3EA1D3414EBD3C46AF360A34752FB884A4A8F43E45F136E6FCBEB86C39AEE1A28B10C50487FB58685FD5E4FA6AFDC39A557928D65E6AFAD5504D26E0D658EB195A489BA2558D3B8510E3A7E588F338C0BB80C3130225ECB755DC6A34E8DCBCCFFB673A5FE5453EE9B6A7F77C8A8748D016CF643932103123C1C2CDAAEE66BD2670CC1679A4B22E319D44B492A40528241474BDE080BD100F5C986E1E5E36; ntustsecret=71675433314849634A6876546A674F6B652F6442385249654B41325279306258; ntustjwtsecret=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoiQjEwNzA3MTI4IiwiZXhwIjoxNjAwMTc4NjgyLCJuYmYiOjE2MDAwOTIyODJ9.SIneocslfq9qniQ-eQPS6uDMR6_u4NBMNn30_gjejhk',
    "referer": "https://querycourse.ntust.edu.tw/querycourse/"
}
resp = requests.post(url, data=payload.encode('utf-8'), headers=header)
print(resp.text)
json_file = json.loads(resp.text)
print(json_file)
numOfStudent = json_file[0]['ChooseStudent']
print(numOfStudent)
# if int(numOfStudent) < 3:  # int(json_file[0]['Restrict2']):
#     print('現在的選課人數為'+numOfStudent+'，請盡快加簽')
