'''
    5635번 "생일" 실버 5
    
    2차원 정렬 
    
    문제
        어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.

    입력
        첫째 줄에 반에 있는 학생의 수 n이 주어진다. (1 ≤ n ≤ 100)

        다음 n개 줄에는 각 학생의 이름과 생일이 "이름 dd mm yyyy"와 같은 형식으로 주어진다. 
        이름은 그 학생의 이름이며, 최대 15글자로 이루어져 있다. dd mm yyyy는 생일 일, 월, 연도이다. 
        (1990 ≤ yyyy ≤ 2010, 1 ≤ mm ≤ 12, 1 ≤ dd ≤ 31) 주어지는 생일은 올바른 날짜이며, 연, 월 일은 0으로 시작하지 않는다.

        이름이 같거나, 생일이 같은 사람은 없다.

    출력
        첫째 줄에 가장 나이가 적은 사람의 이름, 둘째 줄에 가장 나이가 많은 사람 이름을 출력한다.
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