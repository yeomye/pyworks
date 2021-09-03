# if ~ elif ~ else 문
# 놀이공원 입장료 계산하기
print('♣ 놀이공원 입장료 ♣')
age = input('나이를 입력하세요 : ')
age1 = int(age)
charge = 0

if age1 < 8:
    print('미취학 아동입니다.')
    charge = 1000
elif age1 >= 8 and age1 < 14:
    print('초등학생입니다.')
    charge = 2000
elif age1 >= 14 and age1 < 20:
    print('중.고등학생입니다.')
    charge = 2500
else:
    print('일반인입니다.')
    charge = 3000

#print('입장료는 ' + str(charge) + '원입니다.')
print('입장료는 ' + format(charge,',d') + '원입니다.')
# format(value, '서식문자') - 천단위 구분기호 표시
# d - 정수형, s - 문자형
