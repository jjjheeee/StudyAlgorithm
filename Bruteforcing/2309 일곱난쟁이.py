'''
    2309번 "일곱 난쟁이" 브론즈 1
    
    브루트포스 알고리즘 (완전 탐색)
    정렬
    
'''

dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

dwarfs.sort()
dwarf_sum = sum(dwarfs)
fined_num = dwarf_sum - 100

for num in dwarfs:
    the_rest = fined_num - num
    if the_rest != num and the_rest in dwarfs:
        
        dwarfs.remove(the_rest)
        dwarfs.remove(num)
        
        break
        
for i in dwarfs:
    print(i)