pattern = """***
* *
***"""

def recur(num):
    st_num = num//3
    
    print(pattern,end='')
    print(pattern,end='')
        

    return st_num



print(recur(9))