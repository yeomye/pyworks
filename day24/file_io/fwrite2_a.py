# a모드는 input() 코드에서 필수로 사용
f = open("c:/pyfile/number2.txt",'a')
f.write('%d\n'%(100/2))
f.write('%.2f\n'%7.34)
num = '%d\n' % 150000     # 변수로 저장
f.write(num)
f.write('%d\n' % 7)

f.close()