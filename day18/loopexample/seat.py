x = input('입장객 수 : ')
customer = int(x)
y = input('열 수 : ')
col_num = int(y)

if customer % col_num == 0:
    row_num = int(customer/col_num) 
else:
    row_num = int(customer/col_num)+1

#print(str(row_num) + '개의 줄이 필요합니다.')

for i in range(0, row_num):
    for j in range(1, col_num+1):
        seat_num = i*col_num+j
        if seat_num <= customer:
            print(seat_num, end='')
        else:
            break
        
    print()
