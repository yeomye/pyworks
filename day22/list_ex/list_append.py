# 리스트 예제
# li2에 li 요소에 3을 곱하여 저장
li = [1, 2, 3, 4]
li2 = []
# 저장
for i in li:
    li2.append(i*3)
# 출력
print(li2)

#합계와 평균

total = 0
for i in li:
    total += i

avg = total/len(li)

print("개수 :", len(li))
print('합계 :',total)
print('평균 :', avg)

il = [1, 2, 3, 4]
il2 = []
tal = 0

for i in il:
    tal += i

print(tal)
print(tal/len(il))