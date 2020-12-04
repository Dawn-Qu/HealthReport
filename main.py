import requests
import json
import logging
import requests.packages.urllib3
import time


def report_health(user_sessionID):
    requests.packages.urllib3.disable_warnings()
    sessionID = user_sessionID
    url2p = 'https://zhxg.whut.edu.cn/yqtjwx/monitorRegister'
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
    post_data2 = {"diagnosisName": "", "relationWithOwn": "", "currentAddress": "湖北省武汉市江岸区沿江大道188号", "remark": "",
                  "healthInfo": "正常", "isDiagnosis": 0, "isFever": 0, "isInSchool": 1, "isLeaveChengdu": 0,
                  "isSymptom": "0", "temperature": "36°C以下", "province": "湖北省", "city": "武汉市", "county": "江岸区"}
    headers2p['Cookie'] = 'JSESSIONID=' + sessionID
    r2p = requests.post(url2p, headers=headers2p, data=json.dumps(post_data2), verify=False)
    r2p_json = r2p.json()
    print(r2p_json)
    logging.info(str(r2p_json))
    if r2p_json['status'] == 'True':
        print('报送成功')
        logging.info('报送成功')


logging.basicConfig(filename='health_report.log',level=logging.INFO)
while True:
    sessionID=''
    report_health(sessionID)
    time.sleep(3600)
