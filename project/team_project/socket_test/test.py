import reqeusts
import os

cur_dir = os.path.dirname(os.path.realpath(__file__)) 

#보내고자하는 파일을 'rb'(바이너리 리드)방식 열고
files = open(cur_dir+'/test.png', 'rb')

# 파이썬 딕셔너리 형식으로 file 설정
upload = {'file':files}
print(upload)
# String 포맷
obj={"temperature":'23.5', "humidity":'54.5'}

# # request.post방식으로 파일전송.
# res = requests.post('http://127.0.0.1:8080/test', files = upload, data = obj}

