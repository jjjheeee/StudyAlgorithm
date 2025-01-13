'''
    5635번 "생일" 실버 5
    
    2차원 정렬 
'''
import sys

N = int(input())

student_list = [input().strip().split() for _ in range(N)]

student_list.sort(key=lambda student:(int(student[-1]),int(student[-2]),int(student[-3])))

temp_list = [student_list[-1][0],student_list[0][0]]

print(*temp_list, sep='\n')

# import sys

# N = int(sys.stdin.readline())

# student_list = [sys.stdin.readline().strip().split() for _ in range(N)]

# student_list.sort(key=lambda student:(int(student[-1]),int(student[-2]),int(student[-3])))

# temp_list = [student_list[-1][0],student_list[0][0]]

# print(*temp_list, sep='\n')