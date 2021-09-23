# map()함수와 합께 사용
#list([리스트])->리스트로 변환(출력

def times2(a):
    a2=[]
    for i in a:
        a2.append(i*3)
    return a2

v=[1, 2, 3, 4]
print(times2(v))

times = lambda x:x*3
print(list(map(times,v)))