'''
    2775번 "부녀회장이 될테야" 브론즈 1
    
    DP
'''

import sys


T = int(sys.stdin.readline().strip())

for _ in range(T):
    K = int(sys.stdin.readline().strip()) # k층
    N = int(sys.stdin.readline().strip()) # n호

    # 1층의 사람들
    DP = [i for i in range(1,N+1)]
    
    for _ in range(K): # k층까지 반복
        for n in range(1, N): # 1부터 n-1호까지 반복
            DP[n] += DP[n-1]
            
    print(DP[-1])