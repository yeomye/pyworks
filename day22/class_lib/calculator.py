# Calculator 클래스 정의

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):     #외부에서 값을 입력하면 더하는 함수
        self.value += val
        return self.value

class UPgradeCalculator(Calculator):
    def minus(self,val):
        self.value -= val
        return self.value

cal = Calculator()
print(cal.add(10))

#UpgradeCalculator() 테스트
cal2 = UPgradeCalculator()
print(cal2.add(10))
print(cal2.minus(7))
print(cal2.value)

class Calcul:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

cal01 = Calcul()
print(cal01.add(5))

class Upgrade(Calcul):
    def minus(self,val):
        self.value -= val
        return self.value

cal02 = Upgrade()
print(cal02.add(5))
print(cal02.minus(2))
print(cal02.value)