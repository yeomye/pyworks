import random as r

# 로또복권(1~45) - 6개
lotto = []

# while문 로또 만들기
while len(lotto) < 6:       # len(lotto) : 0 ~ 5
    rnd = r.randint(1, 45)
    if rnd not in lotto:
        lotto.append(rnd)

'''
# for문 로또 만들기 - 개수의 문제가 해결되지 않음
for i in range(6):
    rnd = r.randint(1, 45)      #랜덤 수
    if rnd not in lotto:    # rnd(난수)가 lotto 리스트에 없을때
        lotto.append(rnd)
'''

print(lotto)