import sys
import os
import hashlib
import hmac
import base64
import requests
import time, json

timestamp = int(time.time() * 1000)
timestamp = str(timestamp)
url = "https://sens.apigw.ntruss.com"
requestUrl = "/sms/v2/services/"
serviceId = "작성하시오"
requestUrl2 = "/messages"
access_key = "작성하시오"				# access key id (from portal or sub account)



def	make_signature(uri):
    access_key = "작성하시오"				# access key id (from portal or sub account)
    secret_key = "작성하시오"				# secret key (from portal or sub account)
    secret_key = bytes(secret_key, 'UTF-8')

    method = "POST"

    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingKey

uri = requestUrl + serviceId + requestUrl2
apiUrl = url+ uri
print(make_signature(uri))

body = {
    "type":"SMS",
    "contentType":"COMM",
    "countryCode":"82",
    "from":"작성하시오",
    "subject":"string",
    "content":"내용 테스트",
    "messages":[
        {
            "to":"작성하시오",
        }
    ],
}

body2 = json.dumps(body)

headers = {'Content-Type': 'application/json; charset=utf-8', 'X-ncp-apigw-timestamp': timestamp, 'x-ncp-iam-access-key': access_key, 'x-ncp-apigw-signature-v2': make_signature(uri)}
cookies = {'session_id': 'sorryidontcare'}
res = requests.post(apiUrl, headers=headers, data=body2)


print(res.json()) # json response일 경우 딕셔너리 타입으로 바로 변환
