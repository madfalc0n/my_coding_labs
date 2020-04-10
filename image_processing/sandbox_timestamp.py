import requests
import time 
import sys
import os
import hashlib
import hmac
import base64
import json

timestamp = int(time.time() * 1000)
timestamp = str(timestamp)
print(f"타임스탬프 값: {timestamp}")

url = "https://sens.apigw.ntruss.com"
requestUrl = "/sms/v2/services/"
serviceId = "SMS서비스ID"
requestUrl2 = "/messages"
access_key = "허가된ACCesskey""
secret_key = "허가된ACCesskey와맵핑되는SecretKey"
uri = requestUrl + serviceId + requestUrl2
apiUrl = url+ uri


def	make_signature(uri,timestamp,access_key,secret_key):
	secret_key = bytes(secret_key, 'UTF-8')

	method = "POST"

	message = method + " " + uri + "\n" + timestamp + "\n" + access_key
	message = bytes(message, 'UTF-8')
	signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
	return signingKey


signature = make_signature(uri,timestamp,access_key,secret_key)
print(signature)

data = {
    "type":"SMS",
    "contentType":"COMM",
    "countryCode":"82",
    "from":"허가받은번호",
    "content":"내용",
    "messages":[
        {
            "to":"송신할번호",
            "content":"위의 content와 별도로 해당 번호로만 보내는 내용(optional)"
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
print(response.text.encode('utf8'))
