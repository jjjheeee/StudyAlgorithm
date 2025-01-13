'''
    7568번 "덩치" 실버 5
    
    구현 시물레이션
'''
import sys

N = int(sys.stdin.readline().strip())

member_list = []
for i in range(N):
    member_list.append(list(map(int,sys.stdin.readline().strip().split())))

rank_list = []
for member in member_list:
    cnt = 0
    
    for mem in member_list:
        
        if mem == member:
            pass
        elif member[0] < mem[0] and member[1] < mem[1]:
            cnt += 1
    
    rank_list.append(cnt+1)
    
print(*rank_list)