from libs.myclass import Car, Student

car1 = Car('소나타', 'white', 2500)
car2 = Car('BMW', 'black', 3000)

print('\t 모델명 \t 색상 \t 배기량')
print('차량 1' + car1.model + '\t' + car1.color + '\t' + str(car1.cc))
print('차량 2' + car2.model + '\t' + car2.color + '\t' + str(car2.cc))

s1 = Student('콩쥐', 3)
print(s1)