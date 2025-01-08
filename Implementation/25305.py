'''
    25305번 "커트라인" 브론즈 2
    
    구현 시물레이션
'''

import sys

N,k = map(int,sys.stdin.readline().strip().split())

list_ = list(map(int,sys.stdin.readline().strip().split()))

def find_num(arr):
    if len(arr) <= 1:
        return arr
    
    default_num = arr[0] 
    left, equal, right = [], [], []
    
    for i in arr:
        
        if i > default_num:
            left.append(i)
        elif i < default_num:
            right.append(i)
        else:
            equal.append(i)
    return find_num(left) + equal + find_num(right)

sorted_list = find_num(list_)


print(sorted_list[k-1])