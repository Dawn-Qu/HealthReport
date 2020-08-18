import requests
import json
import logging
import requests.packages.urllib3
import time


def report_health(user_sessionID):
    requests.packages.urllib3.disable_warnings()
    sessionID = user_sessionID
    # url1p = 'https://zhxg.whut.edu.cn/yqtjwx/api/login/checkBind'
    url2p = 'https://zhxg.whut.edu.cn/yqtjwx/monitorRegister'
    # headers1p = {
    #     'Host': 'zhxg.whut.edu.cn',
    #     'Connection': 'keep-alive',
    #     'Content-Length': '100',
    #     'Cookie': 'JSESSIONID=103c57d4-5fe3-43d2-a5b3-bfc153680996',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    #     'X-Tag': 'flyio',
    #     'content-type': 'application/json',
    #     'Referer': 'https://servicewechat.com/wxa0738e54aae84423/5/page-frame.html',
    #     'Accept-Encoding': 'gzip, deflate, br'
    # }
    headers2p = {
        'Host': 'zhxg.whut.edu.cn',
        'Connection': 'keep-alive',
        'Content-Length': '304',
        'Cookie': 'JSESSIONID=4c8fc664-7d54-4a36-8779-7ce31b9548e5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'X-Tag': 'flyio',
        'content-type': 'application/json',
        'Referer': 'https://servicewechat.com/wxa0738e54aae84423/5/page-frame.html',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    # post_data1 = {'code': '003qKf0w3PqXMU2I164w3Jz6Us1qKf0A', 'sn': 'null', 'idCard': 'null', 'avatarurl': 'null',
    #               'nickname': 'null'}
    post_data2 = {"diagnosisName": "", "relationWithOwn": "", "currentAddress": "湖北省孝感市孝南区书院街8号", "remark": "",
                  "healthInfo": "正常", "isDiagnosis": 0, "isFever": 0, "isInSchool": 0, "isLeaveChengdu": 1,
                  "isSymptom": "0", "temperature": "36°C以下", "province": "湖北省", "city": "孝感市", "county": "孝南区"}
    # try:
    #     r1p = requests.post(url1p, headers=headers1p, data=json.dumps(post_data1))
    #     if r1p.status_code == 200:
    #         r1p_json = r1p.json()
    #         print(r1p_json)
    #         if r1p_json['status'] == 'True':
    #             sessionID = r1p_json['data']['sessionID']
    headers2p['Cookie'] = 'JSESSIONID=' + sessionID
    r2p = requests.post(url2p, headers=headers2p, data=json.dumps(post_data2), verify=False)
    r2p_json = r2p.json()
    print(r2p_json)
    logging.info(str(r2p_json))
    if r2p_json['status'] == 'True':
        print('报送成功')
        logging.info('报送成功')
    # except:
    #     pass


logging.basicConfig(filename='health_report.log',level=logging.INFO)
while True:
    sessionID=''
    report_health(sessionID)
    time.sleep(3600)
