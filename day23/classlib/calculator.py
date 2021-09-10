#계산기 클래스
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value

# add() 함수에서 객체 변수가 100이상의 값을 가질수 없도록 제한하는 클래스
class MaxLimitClaculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
           self.value = 100
        return self.value




cal = MaxLimitClaculator()
cal.add(50)
cal.add(60)
#cal.minus(3)
print(cal.value)