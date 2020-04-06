def course_selection(course_list):
    # 코드를 작성하세요.
    result = []
    start_c = 0
    end_c = 0
    for i in range(len(course_list)):
        if i == 0 :
            


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
