# 지역변수 사용하기

def one_up():
    x = 1   # x는 지역변수 : 호출할떄마다 초기화됨
    x += 1
    return x

print(one_up())
print(one_up())
