import requests
import time 
import sys
import os
import hashlib
import hmac
import base64
import json
from datetime import datetime

"""
네이버 클라우드 플랫폼의 SMS API 이용
"""
cur_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

timestamp = int(time.time() * 1000)
timestamp = str(timestamp)
#print(f"타임스탬프 값: {timestamp}")

url = "https://sens.apigw.ntruss.com"
requestUrl = "/sms/v2/services/"
serviceId = "SMS서비스ID"
requestUrl2 = "/messages"
access_key = "허가된ACCesskey""
secret_key = "허가된ACCesskey와맵핑되는SecretKey"
uri = requestUrl + serviceId + requestUrl2
apiUrl = url+ uri


def make_signature(uri,timestamp,access_key,secret_key):
    secret_key = bytes(secret_key, 'UTF-8')

    method = "POST"

    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingKey


signature = make_signature(uri,timestamp,access_key,secret_key)
print(signature)

send_phonenum = '010123456'
recv_phonenum = '010123456'
msg = cur_time + "지하철 객실 내 응급환자 발생 확인 요망"

data = {
    "type":"SMS",
    "contentType":"COMM",
    "countryCode":"82",
    "from": send_phonenum,
    "content":"내용",
    "messages":[
        {
            "to": recv_phonenum,
            "content": msg
        }
    ]
}
data2 = json.dumps(data)
headers = {
  'Content-Type': 'application/json; charset=utf-8',
  'X-ncp-apigw-timestamp': timestamp,
  'x-ncp-iam-access-key': access_key,
  'x-ncp-apigw-signature-v2': signature
}

response = requests.post(apiUrl, headers=headers, data = data2)
#결과 확인
print("Send Message result : ",response.text.encode('utf8'))
