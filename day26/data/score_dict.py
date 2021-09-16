# 학생 5명의 개인별 국어, 수학 점수 계산
score = [
    {'name':'이대한', 'korean':90, 'math':70, 'science' : 65},
    {'name':'장민국', 'korean':85, 'math':76, 'science' : 75},
    {'name':'오상식', 'korean':80, 'math':65, 'science' : 85},
    {'name':'천선란', 'korean':95, 'math':85, 'science' : 55},
    {'name':'김초엽', 'korean':85, 'math':70, 'science' : 35}
]
print('이름  총점  평균')
sum_v = 0
for s in score:
    sum_v = s['korean'] + s['math'] + s['science']
    avg = sum_v / 3
    print(s['name'], sum_v, avg)

# 과목별 국어 수학 점수 계산
total_kor = 0
total_math = 0
total_sci = 0
n = len(score)

for i in score:
    total_kor += i['korean']
    total_math += i['math']
    total_sci += i['science']

avg_kor = total_kor/n
avg_math = total_math/n
avg_sci = total_sci/n

print('국어 합계 : %d점' %total_kor)
print('수학 합계 : %d점' %total_math)
print('과학 합계 : %d점' %total_sci)
print('국어 평균 : %.1f점' %avg_kor)
print('수학 평균 : %.1f점' %avg_math)
print('과학 평균 : %.1f점' %avg_sci)
