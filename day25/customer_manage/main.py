# Customer 클래스
from customer_class import Customer, GoldCustomer, VIPCustomer

# 객체 생성
c1 = Customer(101, '흥부')
c2 = Customer(102, '놀부')
gold1 = GoldCustomer(201,'콩쥐')
gold2 = GoldCustomer(202,'팥쥐')
vip = VIPCustomer(301, '심청', 777)

price = 10000
c1.calc_price(price)
c2.calc_price(price)
gold1.calc_price(price)
gold2.calc_price(price)
vip.calc_price(price)

# 고객정보 출력
c1.showInfo()
c2.showInfo()
gold1.showInfo()
gold2.showInfo()
vip.showInfo()