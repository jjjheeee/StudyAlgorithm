'''
    11650번 "좌표 정렬하기" 실버 5
    
    2차원 정렬 (추가 문제)
'''

num = int(input())
coordinates = []

for i in range(num):
    x,y = input().split()
    coordinates.append([int(x),int(y)])

coordinates.sort(key=lambda coord:(coord[0],coord[1]))

for i in coordinates:
    print(*i)