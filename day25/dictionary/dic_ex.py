# 딕셔너리 예제

dic = {1:'A', 2:'B', 3:'C'}

# 추가
dic[4] = '0'
print(dic)

# 수정
dic[4] = 'D'
print(dic)

# 삭제
dic.pop(2)
print(dic)

# dic 요소 출력

for key in dic:
    print(key)
    print(dic[key])
