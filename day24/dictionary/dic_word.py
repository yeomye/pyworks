"""
# 용어 사전 만들기
- 단어를 정의 : dictionary 자료 만들기
- 단어를 검색해서 단어가 있으면면 정의가 출력되고,
  없으면 '찾는 단어가 없습니다.' 출력
"""
dict = {
    '이진수' : '2진법으로 나타낸 숫자, 0과 1로 구성됨.',
    '버그' : '프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각.',
    'html' : '하이퍼텍스트 마크업 언어로 웹 페이지를 구성하는 언어이다.',
    'css' : '웹 페이지를 구성하는 요소로 디자인을 담당하는 웹 기술이다.',
    '함수' : '재사용 가능한 코드 조각, function이라고 한다.'
}

print('♣용어사전♣')
try:

    word = input('정의되어 있는 단어를 입력하세요 :')
    definition = dict[word]     # 용어의 뜻
    print(definition)
except:
    print('찾는 단어가 없습니다.')
