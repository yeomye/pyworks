# return이 있는 함수

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

total = add(10,11)  # 지역변수여서 소멸했다.
minus = sub(10,11)
print("두 수의 합 = [0]".format(total))
print("두 수의 차 = [0]".format(minus))
