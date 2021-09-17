# with ~ as 읽어오기
# kbo2021.txt

try:
    with open('C:/pyfile/kbo2021.txt', 'r') as f:
        #data = f.read()    # 전체 읽기
        #print(data)

        line=f.readline()   # 한줄 읽기
        print(line)

        lines = f.readlines()
        print(lines)    # 리스트로 반환
        '''
        while True:
            line = f.readline()     # 줄단위로 읽어오기
            if not line:
                break
            print(line)
        '''
except FileNotFoundError:
    print('파일을 찾을 수 없습니다.')