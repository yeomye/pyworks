# 이차원 리스트 - 리스트 내부에 또 리스트가 있음
"""
d2 = [[10,20],
      [30,40]]

# 인덱싱
print(d2[0][0])     # 10
print(d2[0][1])     # 20
print(d2[1][0])     # 30
print(d2[1][1])     # 40

# 요소 값 전체 출력
for x, y in d2:
    print(x,y)
"""

# 1차원 리스트

d1 = [10, 20, 30]
print(d1)

# 요소 출력
for i in d1:
    print(i)

# 추가 - append
d1.append(40)
print(d1)

# 삭제 - remove
d1.remove(20)
print(d1)

print(len(d1))

sum_v = 0
for i in d1:
    sum_v += i
avg = sum_v/len(d1)
print('합계 :',sum_v)
print('평균 :%.2f'% avg)