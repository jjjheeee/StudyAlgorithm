'''
    2748번 "피보나치 수 2" 브론즈 1
    
    DP
'''

import sys


n = int(sys.stdin.readline().strip())

temp_list = [0,1]

for i in range(1,n+1):
    
    temp_list.append(temp_list[i]+temp_list[i-1])
    
print(temp_list[n])