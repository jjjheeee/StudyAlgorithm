'''
    2947번 "나무 조각" 브론즈 1
    
    구현 시물레이션
'''

import sys

num = list(map(int,sys.stdin.readline().strip().split()))

def mix_list(num_list):
    for i in range(4):
        if num_list[i] > num_list[i+1]:
            num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
        
            print(*num_list)
    return num_list

while True:
    temp_list = mix_list(num)
    
    if temp_list == [1,2,3,4,5]:
        break