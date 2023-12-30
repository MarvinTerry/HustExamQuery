import requests
from requests_hustauth import HustAuth

def get_exam_info(Uname:str,Upass:str,xqh:str=None) -> dict: 
    # login with proj:HustAuth see more info on https://github.com/MarvinTerry/HustAuth
    session = requests.Session()
    hust_auth = HustAuth(Uname,Upass)
    
    # initial login
    url_UserKs = 'http://mhub.hust.edu.cn/cas/login?redirectUrl=/ksapController/urlUserKs'
    session.get(url_UserKs, auth=hust_auth)

    # get xqh
    if(xqh == None):
        url_xqOpthions = 'https://mhub.hust.edu.cn/CommonController/xqOpthions'
        resp = session.get(url_xqOpthions, auth=hust_auth)
        xqh = resp.json()["xqOptions"]["XQH"]

    # fetch exam info
    data = {'pageIndex': 1, 'pageSize': 100, 'kslx': "1", 'kcmc':None, 'xqh': xqh}
    headers = {'Content-Type': 'application/json'} # essential for POST request below
    url_getStuKsxx = 'http://mhub.hust.edu.cn/ksapController/getStuKsxx'
    resp = session.post(url_getStuKsxx ,auth=hust_auth, json=data, headers=headers)
    
    exam_list = resp.json()["list"]
    return exam_list



