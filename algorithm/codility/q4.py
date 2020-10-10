# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(blocks):
    # where start?
    if len(blocks) <= 2:
        return len(blocks)

    result = 0
    start, end = 0, 0
    upcnt, downcnt = 0,0
    last_point = len(blocks) - 1
    # mode , True - Upmode(default) , False - Downmode
    mode = True
    cur_mode = True
    index = 0
    cnt_list = []
    result = 0
    for i in range(len(blocks)):
        start, end = i, i
        if i == 0:
            while True:
                cur = end
                end += 1
                if end == last_point:
                    break
                #upstare
                if blocks[cur] <= blocks[end]:
                    cur_mode = True
                    upcnt += 1
                else:
                    result = max(end-i+1, result)
                    break
        elif i == last_point:
            while True:
                cur = end
                end -= 1
                if end == 0:
                    break
                #upstare
                if blocks[cur] <= blocks[end]:
                    cur_mode = True
                    upcnt += 1
                else:
                    result = max(i-end+1, result)
                    break
        elif 0 < i < last_point:
            while True:
                cur = end
                end -= 1
                if end == 0:
                    break
                #upstare
                if blocks[cur] <= blocks[end]:
                    cur_mode = True
                    upcnt += 1
                else:
                    result = max(i-start+1, result)
                    break
            end = i
            while True:
                cur = end
                end += 1
                if end == last_point:
                    break
                #upstare
                if blocks[cur] <= blocks[end]:
                    cur_mode = True
                    upcnt += 1
                else:
                    result = max(start-i+1, result)
                    break
    return result
    