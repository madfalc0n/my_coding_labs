import urllib.request as req
import json

def reurl(url):
    data = req.urlopen(url).read()
    text = data.decode('utf-8')
    jsontext = json.loads(text)
    # print(jsontext)
    userinfo = jsontext['data']
    result = ''
    for d in userinfo:
        result += d['about']
    
    return result

def reurl2(url):
    data = req.urlopen(url).read()
    text = data.decode('utf-8')
    jsontext = json.loads(text)
    # print(jsontext)
    count = jsontext['total_pages']
    datainfo = jsontext['data']
    result = ''
    tmp_cnt = 0
    for data in datainfo:
        # print(data)
        if tmp_cnt == count:
            break
        if len(data['title']) is not None:
            result += data['title']
            result += '\n'
            tmp_cnt += 1
            
        else:
            if len(data['story_title']) is not None:
                result += data['story_title']
                result += '\n'
                tmp_cnt += 1
    if len(result) != 0:
        result = result[:-1]
    
    return result
    
def getAuthorHistory(author):
    # Write your code here
    url = https://jsonmock.hackerrank.com/api/articles?author=epaga&page=<pageNumber>
    url2 = 
    
    result1 = reurl(url)
    result2 = reurl2(url2)
    result = result1 + result2
    # print(result)
    return result

print(getAuthorHistory('epaga'))
print('-----------------')
print(getAuthorHistory('panny'))
print('-----------------')
print(getAuthorHistory('saintamh'))