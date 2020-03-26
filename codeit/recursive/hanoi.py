def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    if num_disks <= 0 :
        return 1
    for i in range(num_disks):
        if i != num_disks-1:
            mid_peg = end_peg-start_peg
            move_disk(i+1, start_peg, end_peg)
            hanoi(i , mid_peg , start_peg+1)
        else: # 마지막일 떄 처음에서 끝으로 옮겨줌
            move_disk(i+1, start_peg, end_peg)
            hanoi(num_disks-1 , start_peg+1 , end_peg)
    

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)