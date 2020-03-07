#해당 코드는 https://supervise.ly/ 에서 작업한 이미지들을 detection 기반으로 작업한 json 양식에 대해 yolo txt형식으로 바꿔주는 코드임


import json
import os

path = "fainting_people_101-4-aug/fainting_people/ann/" #실제 json 파일들이 있는 경로
file_list = os.listdir(path)
file_list_json = [file for file in file_list if file.endswith(".json")]

#print ("file_list_py: {}".format(file_list_json))
for file in file_list_json:
    cov2txt_name = os.path.splitext(file)[0] #파일명과 확장자를 튜플 형식으로 분리 후 파일명만 변수로 저장
    #print(cov2txt_name)
    
    with open(path+file) as json_file:
        json_data = json.load(json_file)
        #print(type(json_data))
        #print((json_data))
        
        try:
            #위치가 바뀐경우
            if json_data['objects'][0]['points']['exterior'][0][0] > json_data['objects'][0]['points']['exterior'][1][0]:
                #print(json_data['objects'][0]['points']['exterior'])
                print("YOLO 포멧형식에 따라 꼭지점 변경됨")
                data = "fainting_people "
                for txt in json_data['objects'][0]['points']['exterior'][1]:
                    data += str(txt)+" "
                for txt in json_data['objects'][0]['points']['exterior'][0]:
                    data += str(txt)+" "
                #print(data)
                f = open("result/"+cov2txt_name+".txt", 'w')
                f.write(data)
                f.close()

            #위치가 바뀌지 않는 경우        
            else:
                #print(json_data['objects'][0]['points']['exterior'])
                data = "fainting_people "
                for txt in json_data['objects'][0]['points']['exterior'][0]:
                    data += str(txt)+" "
                for txt in json_data['objects'][0]['points']['exterior'][1]:
                    data += str(txt)+" "
                #print(data)
                f = open("result/"+cov2txt_name+".txt", 'w')
                f.write(data)
                f.close()

            #print(json_data['objects'][0]['points']['exterior'][0])
        except IndexError as i:
            print('이미지 속 객체가 없음')
            pass
        
        