'''
    2578번 "빙고" 실버 4
    
    구현 시물레이션
'''

import sys

bingo_board = []
call_number = []
for i in range(10):
    if i < 5:
        bingo_board.append(list(map(int,sys.stdin.readline().strip().split())))
    else:
        call_number.append(list(map(int,sys.stdin.readline().strip().split())))

    
# print(bingo_board)
# print(call_number)
check = [[0] * 5 for _ in range(5)]

def find(num):
    for i in range(5):
        for j in range(5):
            if bingo_board[i][j] == num:
                check[i][j] = 1
                break
            
    return

def bingo(check):
    cnt = 0
    
    # 가로
    for row in check:
        if sum(row) == 5:
            cnt += 1
    
    # 세로
    for i in range(5):
        col_cnt = 0
        for j in range(5):
            col_cnt += check[j][i]
            
        if col_cnt == 5:
            cnt += 1 
            
    # 대각선
    temp_cnt1 = 0
    for i in range(5):
        temp_cnt1 += check[i][i]
        
    if temp_cnt1 == 5:
        cnt += 1
        
    # 역대각선
    temp_cnt2 = 0
    for i in range(5):
        temp_cnt2 += check[i][4-i] 
        
    if temp_cnt2 == 5:
            cnt += 1  
                 
    return cnt

def temp() :
        
    bingo_cnt = 0    
    for row in call_number:
        for j in row:
            find(j)
            bingo_cnt += 1
            if bingo(check) >= 3:
                
                print(bingo_cnt)
                return
temp()