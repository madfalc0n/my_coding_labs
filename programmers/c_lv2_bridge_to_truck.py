def queue_process_in(truck_weights, queue, queue_cnt,tr_cnt): #트럭들을 다리(큐)에 넣는 과정, 큐 카운트에도 추가
    #queue_cnt[truck_weights[0]] = queue_cnt.get(truck_weights[0],0)+1
    queue_cnt[tr_cnt] = queue_cnt.get(tr_cnt,0)+1
    queue.append(truck_weights.pop(0))
    tr_cnt += 1
    return truck_weights, queue, queue_cnt, tr_cnt

def queue_full_check(bridge_length, weight, truck_weights, queue): #다리(큐)에 트럭이 올라올 수 있는지 여부, 올라오는 트럭의 무게와 현재 다리에 있는 트럭들의 무게를 체크한다.
    print("큐 풀 체크")
    if bridge_length == len(queue):#브릿지 길이와 큐 길이가 같을 때
        return 0 
    if truck_weights[0] + sum(queue) < weight: #큐의 길이와 브릿지 길이
        return 1
    else:  # , weight 보다 더 클때 
        return 0

import copy

def queue_move(queue_cnt):
    print("큐의 움직임")
    print(queue_cnt)
    for i in queue_cnt.keys():
        queue_cnt[i] += 1
    print(queue_cnt)
    return queue_cnt

def queue_process_out(complete_truck,queue ):#다리(큐)에있는 트럭들을 빼는 과정
    complete_truck.append(queue.pop(0))
    return complete_truck

def queue_cnt_full_check(queue_cnt,bridge_length): # 큐카운트에서 다리를 다 건넌 놈들 있는지 여부
    if len([x for x,j in queue_cnt.items() if j >= bridge_length]) !=0:
        return 1
    else:
        return 0


def solution(bridge_length, weight, truck_weights):
    print("시작을 알림")
    init_tr_len = len(truck_weights)
    init_tr = copy.deepcopy(truck_weights)
    print("init_tr ", init_tr)
    tr_cnt = 0
    queue = []
    queue_cnt = {}
    queue_v_cnt = 0
    cnt = 0
    complete_truck = []
    
    print(f"시작 전 경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {queue_cnt}") 
    
    while True:
    #for _ in range(20):
        tr_cnt = tr_cnt%init_tr_len
        if len(complete_truck) == 0 and len(truck_weights) == init_tr_len: # 맨처음 시작
            truck_weights, queue, queue_cnt,tr_cnt = queue_process_in(truck_weights, queue, queue_cnt,tr_cnt) #큐에 트럭 올리기
            cnt += 1
            print(f"시작 맨 처음 경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {queue_cnt}") 


        if queue_cnt_full_check(queue_cnt,bridge_length): #다리(큐)에서 다 건넌 애들 있나?
            #있다면? 큐랑 큐카운트에서 제거하고 컴플리트 트럭에 추가 하고 올라올 수 있는 애들 있는지? 확인
            print("다리에서 다 건넌 애들 있고 다시 다리에서 올라올 수 있는 애들 있다")
            print(init_tr)
            print(queue[0])
            print(init_tr.index(queue[0]))
            #del queue_cnt[init_tr.index(queue[0])]
            del queue_cnt[queue_v_cnt]
            queue_v_cnt += 1
            complete_truck = queue_process_out(complete_truck,queue)
            queue_cnt = queue_move(queue_cnt)
            cnt += 1
            if len(truck_weights) != 0 and truck_weights[0] + sum(queue) <= weight: # 큐에 올라올 수 있는 애들 있나?
                # 있다면
                truck_weights, queue, queue_cnt,tr_cnt = queue_process_in(truck_weights, queue, queue_cnt,tr_cnt)
            print(f"2 처음 경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {queue_cnt}")

        else:# 큐에서 다 건넌 애들이 없다면? 큐에 애들 있는지 보고 1씩 움직이자
            if len(queue_cnt) != 0:
                print("다리에서 다 건넌 애들이 없고 애들이 있다면?")
                #큐에 애들 있으면 움직이도록 하자
                queue_cnt = queue_move(queue_cnt)
                if len(truck_weights) != 0 and truck_weights[0] + sum(queue) <= weight: # 움직이고 큐에 올라올 수 있는 애들 있나? 
                    #있다면
                    truck_weights, queue, queue_cnt,tr_cnt = queue_process_in(truck_weights, queue, queue_cnt,tr_cnt)
            cnt += 1
            print(f"3 처음 경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {queue_cnt}")


        if len(complete_truck) == init_tr_len and len(truck_weights) == 0: #트럭들이 다리 다 건넜나?
            print(f"마지막 최종 경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {queue_cnt}")
            #있따면 끝내
            return cnt





        # if queue_cnt_full_check(queue_cnt,bridge_length): #다리(큐)에서 다 건넌 애들 있으면 큐에서 제거하고 +1
        #     print(f"{queue[0]}번 트럭 큐에서 제거 됨")
        #     del queue_cnt[queue[0]]
        #     complete_truck = queue_process_out(complete_truck,queue)
        #     if len(truck_weights) != 0: # 다리 지나야 할 트럭이 남아 있는 경우
        #         if queue_full_check(bridge_length, weight, truck_weights, queue): #트럭 올라올 수 있을 경우, 1일 경우
        #             truck_weights, queue, queue_cnt = queue_process_in(truck_weights, queue, queue_cnt)
        #         else: #올라올 수 없을 경우
        #             queue_cnt = queue_move(queue_cnt) #다리(큐) 위에서 트럭 들 움직임
            
        #     cnt += 1
        #     print(f"3경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {queue_cnt}") 

        # if len(truck_weights) != 0: # 다리 지나야 할 트럭이 남아 있는 경우
        #     if queue_full_check(bridge_length, weight, truck_weights, queue): #트럭 올라올 수 있을 경우, 1일 경우
        #         print("큐에 트럭 넣기 전")
        #         if len(queue_cnt) != 0:
        #             #큐에 넣는다.
        #             queue_cnt = queue_move(queue_cnt)
        #         truck_weights, queue, queue_cnt = queue_process_in(truck_weights, queue, queue_cnt)
        #         cnt += 1
        #         print(f"1경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {queue_cnt}") 
        #         continue
                
        #     else: # 트럭이 올라올 수 없을 경우
        #         print("다리 지나야 할 트력이 남아 있지만 올라올 수 없음")
        #         queue_cnt = queue_move(queue_cnt) #다리(큐) 위에서 트럭 들 움직임
        #         if queue_cnt_full_check(queue_cnt,bridge_length):
        #             print(f"{queue[0]}번 트럭 큐에서 제거 됨")
        #             del queue_cnt[queue[0]]
        #             complete_truck = queue_process_out(complete_truck,queue)
        #             continue
            
        #     cnt += 1
        #     print(f"2경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {queue_cnt}") 

        # if len(complete_truck) == init_tr_len and len(truck_weights) == 0:
        #     return cnt

    


bridge_length =100 #다리 길이
weight = 100 #다리 최대 견딜 수 있는 무게
#truck_weights = [10] #각 트럭의 무게
truck_weights =[10,10,10,10,10,10,10,10,10,10]
# bridge_length =2 #다리 길이
# weight = 10 #다리 최대 견딜 수 있는 무게
# truck_weights = [7,4,5,6] #각 트럭의 무게

print(solution(bridge_length, weight, truck_weights))


















# def solution(bridge_length, weight, truck_weights):
#     len_truck = len(truck_weights)
#     cnt = 0
#     list_cnt = 0
#     queue = []
#     q_cnt = {}
#     complete_truck = []
#     print('시작!!!!')
#     print(f"1경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {q_cnt}") 
#     for i in range(bridge_length*len(truck_weights)): # 트럭 수 * 브릿지 길이
#         if len(complete_truck) == len_truck:
#             return cnt
#         q_cnt_v = [x for x,j in q_cnt.items() if j >= bridge_length]# 다리 다 지난놈 찾기
#         print(" 다리 다 지난놈들의 큐", q_cnt_v)
#         if len(q_cnt_v) == 0: # 처음 단계이거나 다 끝났거나? 
#             print("처음 단계이거나 다 끝났거나 중간에 도달점에 미치지 못했을 경우")
#             if len(truck_weights) == 0 and len(q_cnt) != 0 : # 다리 올라올 트럭이 없고 큐카운트가 있을 때
#                 for x in q_cnt.keys():
#                     q_cnt[x] += 1
#                 cnt += 1
#                 print(f"1경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {q_cnt}") 
#                 q_cnt_v = [x for x,j in q_cnt.items() if j >= bridge_length]
#                 if len(q_cnt_v) != 0:
#                     print("다리 다 지난놈은 큐 카운트 에서 삭제 됩니다.")
#                     print(f"삭제전 큐 카운트: {q_cnt}")
#                     del q_cnt[queue[0]]
#                     print(f"삭제후 큐 카운트: {q_cnt}")
#                     complete_truck.append(queue.pop(0))
#                     cnt +=1
#                     print(f"마지막으로 경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {q_cnt}") 
#                 continue
#             if len(truck_weights) == 0 and q_cnt_v[0] == bridge_length: #트럭이 다리 위로 올라갔을 때
#                 print("마지막스테이지")
#                 cnt += 1
#                 print(f"2경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {q_cnt}")  
#                 q_cnt[queue[0]] = q_cnt.get(queue[0],0)+1
#                 print("다리 다 지난놈은 큐 카운트 에서 삭제 됩니다.")
#                 print(f"삭제전 큐 카운트: {q_cnt}")
#                 del q_cnt[queue[0]]
#                 print(f"삭제후 큐 카운트: {q_cnt}")
#                 complete_truck.append(queue.pop(0))
#                 cnt +=1
#                 break


#             if truck_weights[0]+sum(queue) <= weight:
#                 print(f"다리에 더 올라올 수 있으므로 {truck_weights[0]}을 올려 보낸다")
#                 for x in q_cnt.keys():
#                     q_cnt[x] += 1
#                 q_cnt[truck_weights[0]] = 1
#                 queue.append(truck_weights.pop(0))
#                 cnt += 1
#                 print(f"3경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {q_cnt}")  
#                 continue


#             q_cnt[queue[0]] = q_cnt.get(queue[0],0)+1 # 기존 key가 존재하면 그 키 값에 +1 , 또는 key가 존재하지 않는다면 값 0으로 설정 후 +1
#             cnt += 1
#             print(f"4경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {q_cnt}")  

#         else:
#             print("다리 다 지난놈은 큐 카운트 에서 삭제 됩니다.")
#             print(f"삭제전 큐 카운트: {q_cnt}")
#             del q_cnt[q_cnt_v[0]]
#             print(f"삭제후 큐 카운트: {q_cnt}")
#             if len(q_cnt) != 0:
#                 for x in q_cnt.keys():
#                         q_cnt[x] += 1
#             complete_truck.append(queue.pop(0))   #다 지난놈 추가하기
#             if len(truck_weights) != 0 and truck_weights[0]+sum(queue) <= weight: #아직 다리를 건너야 할 놈들이 남아있다면
#                 print(f"다리를 건너야 할 트럭들이 있습니다. {truck_weights[0]}번 트럭이 다리 위로 올라 옵니다.")
#                 queue.append(truck_weights.pop(0))
#                 q_cnt[queue[0]] = q_cnt.get(queue[0],0)+1
#             cnt += 1
#             print(f"5경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}     큐카운트 : {q_cnt}")   
    

#     return cnt

    


# #bridge_length =100 #다리 길이
# #weight = 100 #다리 최대 견딜 수 있는 무게
# #truck_weights = [10] #각 트럭의 무게
# #truck_weights =[10,10,10,10,10,10,10,10,10,10]
# bridge_length =2 #다리 길이
# weight = 10 #다리 최대 견딜 수 있는 무게
# truck_weights = [7,4,5,6] #각 트럭의 무게

# print(solution(bridge_length, weight, truck_weights))

# a = {5:1 , 2:3 , 4:6}











# def bridge_complete():




# def solution(bridge_length, weight, truck_weights):
#     cnt = 0
#     queue = []
#     q_cnt = {}
#     complete_truck = []
#     for _ in range(len(truck_weights)):
#         q_cnt_v = [x for x,j in q_cnt.items() if j >= bridge_length]# 다리 다 지난놈 찾기
#         if len(q_cnt_v) != 0:
#             print(f"{queue[0]}번 트럭 다리 다 지나고 내려와서 큐에서 빠짐")
#             print("해당 항목 지워짐 ",q_cnt[q_cnt_v[0]], q_cnt_v)
#             del q_cnt[q_cnt_v[0]]
            
#             print(f"{truck_weights[0]}번 트럭 다리에 올라왔음")
#             q_cnt[truck_weights[0]] = 1
#             queue.append(truck_weights.pop(0))
#             complete_truck.append(queue.pop(0))
#             print(q_cnt)
#             print(queue)
            
#             cnt += 1
#             print(f"경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}")

#         else:
#             print("시작!!!")
        

#         for _ in range(bridge_length): # 큐 타는중
#             if len(truck_weights) != 0: # 다리 건너야 할 트럭이 있을 경우
#                 if truck_weights[0] + sum(queue) <= weight: #처음이거나, 다리에 올라갈 수 있을 경우(다리가 무너지지 않을 무게 이거나) 큐에 추가
#                     print(f"{truck_weights[0]}번 트럭 다리에 올라왔음")
#                     if len(q_cnt) != 0 :
#                         q_cnt[queue[0]] += 1
#                     q_cnt[truck_weights[0]] = 1 
#                     queue.append(truck_weights.pop(0))
#                     cnt += 1
#                     print(f"경과된 시간 : {cnt}        다리를 지난 트럭: {complete_truck}    다리를 건너고 있는 트럭: {queue}         대기 트럭: {truck_weights}")

#                 else: # 무게 제한으로 올라가지 못할 경우
#                     print(f"{truck_weights[0]}번 트럭은 무게 문제 때문에 다리에 올라올 수 없음")
#                     print(f"{queue[0]}번 다리 지나는중")
#                     q_cnt[queue[0]] += 1 
#                     cnt += 1
#                 print("q_cnt " ,q_cnt)
            
#             print(cnt , queue)


        
#     if len(queue) != 0:#다리를 다 지난 트럭이 있을 때 내려왓다고 간주
#         print('마지막')
#         print(f"{queue[0]}번 트럭 다리 다 지나고 내려와서 큐에서 빠짐")
#         complete_truck.append(queue.pop(0))
#         cnt += 1
#         print(cnt , queue)
    
#     print(cnt)
#     print(complete_truck)


#     return cnt

# # bridge_length =100 #다리 길이
# # weight = 100 #다리 최대 견딜 수 있는 무게
# # truck_weights = [10] #각 트럭의 무게
# bridge_length =2 #다리 길이
# weight = 10 #다리 최대 견딜 수 있는 무게
# truck_weights = [7,4,5,6] #각 트럭의 무게

# print(solution(bridge_length, weight, truck_weights))


# a = {5:1 , 2:3 , 4:6}
#b , c= [x for x,j in a.items() if j == 1]
#b=  [ a[x]+=1 for x,j in a.keys()]
#print(b)

#print(a.values.get(2,0) )
























# def solution(bridge_length, weight, truck_weights):
#     cnt = 0
#     queue = []
#     for _ in range(len(truck_weights)):
#         for i in range(bridge_length): # 브릿지 타는중
#             print(f"현재 다리에 올라와 있는 트럭들 {queue}")
#             if len(truck_weights) != 0 :
#                 if sum(queue) <= 10:
#                     print(f"truck {truck_weights[0]}번 올라 타려고 함")
#                     if len(queue) == 0: # 큐에 아무도 없을 때
#                         print(f"truck {truck_weights[0]}번 올라 타서 {i+1}번 째 다리 지나는 중")
#                         queue.append(truck_weights.pop(0))
#                         cnt += 1
#                         print(f"현재 시간 {cnt}초 경과")
#                         continue
                        
#                     if len(queue) != 0 and truck_weights[0]+sum(queue) > 10: # 큐에 있고 , 큐와 들어오려는 트력의 무게 합이 10이 넘을 때
#                         print(f"truck {truck_weights[0]}번 다리가 무너질 까봐 올라 타지 못함 {queue}번의 트럭들도 있음")
#                         print(f"truck {queue}번  {i+1}번 째 다리 지나는 중")
#                         cnt += 1 
#                         print(f"현재 시간 {cnt}초 경과")

#                     else:
#                         print(f"truck {truck_weights[0]}번 올라 탔음 {queue}번의 트럭들도 있음")
#                         queue.append(truck_weights.pop(0))
#                         cnt += 1 
#                         print(f"현재 시간 {cnt}초 경과")
#             else:
#                 print(f"truck {queue}번  {i+1}번 째 다리 지나는 중")
#                 cnt += 1 
#                 print(f"현재 시간 {cnt}초 경과")
        
#         print(f"truck {queue[0]}번 내려옴")
#         cnt += 1
#         queue.pop(0) # 브릿지 타고 꺼내줌
#         print(f"현재 시간 {cnt}초 경과")
#     return cnt

# bridge_length =2 #다리 길이
# weight = 10 #다리 최대 견딜 수 있는 무게
# truck_weights = [7,4,5,6] #각 트럭의 무게


# print(solution(bridge_length, weight, truck_weights))