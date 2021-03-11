def check_text(a):
    if a == 'b':
        return 'd'
    elif a == 'p':
        return 'q'
    elif a == 's':
        return 'z'
    if a == 'd':
        return 'b'
    elif a == 'q':
        return 'p'
    elif a == 'z':
        return 's'
    else:
        return a

n = int(input())


for i in range(n):
    a = input()
    ori_a = list(a).copy()
    count = 0
    for j in range(len(ori_a)):
        ori_a[j] = check_text(a[j])

    reulst = ''.join(ori_a)[::-1]
    print(a,reulst )
    if a == reulst:
        print('Mirror')
    else:
        print('Normal')

