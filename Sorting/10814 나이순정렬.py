'''
    10814번 "나이순 정렬" 실버 5
    
    2차원 정렬
'''

member_count = int(input())

members = []
for i in range(member_count):
    member_info = input().split()
    members.append([int(member_info[0]),member_info[1]])
    
members.sort(key=lambda member:member[0]) # 2차원에서 첫번쨰 인자를 기준으로 정렬 한다는 뜻

for i in members:
    print(*i)