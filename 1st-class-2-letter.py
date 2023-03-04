"""
===================
(2) 문자열 자료형
===================
"""
print("hello world")
print('Python is fun')
print("""life is short, you need python""")
print('''life is short, you need python''')
print()

# 이스케이프 문자: 역슬래쉬(\)를 사용해 문자열 내부에 특정한 문자를 포함시킴
# 참고: \t (문자열 사이에 탭 간격), \\ (문자\를 그래도 표현하고 싶을때)
# \n (줄바꿈), w' ('출력) \" (" 출력) \\ (\ 출력)

# 문자열 안에 작은따옴표/큰따옴표 있는 경우
A = "Python's favorite food is perl"
print(A)
B = '"Python is very easy." he says.'
print(B)
# 백슬러쉬 사용 \' ('출력)
A2 = 'Python\'s favorite food is perl'
print(A2)
#  \" (" 출력)
B2 = "\"Python is very easy.\" he says."
print(B2)
print()

# 여러 줄인 문자열: \n (줄바꿈)
A = "life is too short \n you need python" # \n삽입
print(A)
B = '''
life is too short
you need python
'''
print(B)

# \t (문자열 사이에 탭 간격), \\ (문자\를 그래도 표현하고 싶을때)
print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("\\\\\\ 역슬래쉬 세개 출력")
print("\n\t\"\\를 그래돌 출력") # 	"\를 그래돌 출력 
print(r"\n\t\"\\를 그래돌 출력") # print(r""): 이스케이프 문자를 그대로 출력해줌

# print() 함수 
num=3;
text = "I eat %d apples." %num
print(text)
day = 'three'
text2 = "I ate %d apples, so I was sick for %s days." %(num, day)
print(text2)
text3 = "I ate {0} apples, so I was sick for {1} days.".format(num, day)
print(text3)
text4 = "I ate {0} apples, so I was sick for {day} days.".format(num, day=3)
print(text4)

print("%10s" % "hi") #         hi
print("%-10sjane" % "hi") #hi 포함한  공간이 10개: hi        jane

# 문자 정렬 
"{0:<10}".format('hi') # 왼쪽 정렬 'hi        '
"{0:>10}".format('hi') # 오른쪽정렬 '        hi'
"{0:^10}".format('hi') # 가운데정렬
"{0:=^10}".format('hi') # 가운데정렬&공백=로채우기 '    hi    '
"{0:!<10}".format('hi') # 왼쪽정렬&공백!로채우기
"{0:!>10}".format('hi') # 오른쪽정렬 & 공백!로 채우기 

# f 문자열 포맷팅
f'{"hi":<10}' #'hi        '
f'{"hi":>10}' #'        hi'
f'{"hi":^10}' # '    hi    '
f'{"hi":=^10}' # '====hi===='
f'{"hi":!<10}' # 'hi!!!!!!!!'
y = 3.42134234;
f'{y:0.4f}' # '3.4213' (문자열)
f'{y:10.4f}' #'    3.4213'  (문자열)

name= '홍길동';age = '24';
f'나의 이름은 {name}입니다. 나이는 {age}입니다'


# 문자열 연산
a= "python"; b=" is fun";
print(a+b)
print(a*2) # pythonpython
print("="*50)
print("my program")
print("="*50)


# 문자열 크기
a='life is beautiful, enjoy it'
len(a)
# 문자열 인덱스:0,1,2,
a[0]
a[2]
a[-1] #제일 마지막
b=a[0]+a[1]+a[2]+a[3]
a[0:4] # 'life'
a[0:3] # 'lif'
a[0:5] # 'life '
a[19:] # 'enjoy it' (19번째 포함)
a[:19] # 19번째 포함하지 않음 
a[:17]
a[:]
a[19:-3] # 19번째부터 끝에서 3번째까지 

# 문자열 바꾸기
a="pithon"
#a[1]='y' # error
a = a[:1]+'y'+a[2:]
print(a)


# 문자열 관련 함수
a ="Python is the best choice"
a.count('t') # 갯수
a.find('b') # index
a.find('k') # -1: 존재하지 않음
a.index('t') # t가 처음나온 위치
a.upper() #대문자
a.lower() #소문자
a.replace("Python", "C++")
a.split() #공백을 기준으로 나누기 => ['Python', 'is', 'the', 'best', 'choice'] 리스트 
b= "a:b:c:d"
b.split(':') # ['a', 'b', 'c', 'd']

# 문자열 삽입(join)
",".join('abcd') # 'a,b,c,d'
",".join(['a','b','c','d']) # 'a,b,c,d'
" ".join(['a','b','c', 'd']) # 'a b c d'

# 문자열 공백 없애기 
a = " hi "
a.lstrip() #왼쪽공백 'hi '
a.rstrip() #오른쪽공백' hi'
a.strip() #양쪽 'hi'


## ========= Exercise ===========
# 1. 국어 a, 영어 b, 수학 c점일 때 홍길동 씨의 평균 점수는? (점수를 input으로 받기/소숫점까지 고려)
# 2. 자연수 n이 홀수인지 짝수인지 판별하는 방법은? 
# 3. 홍길동씨의 주민등록번호는 881212-1068234이다. 
#   (1) 연월일 부부과 그 뒤의 숫사 부분으로 나누어 출력해보자.
#   (2) 주민등록번호에서 성별을 나타내는 숫자를 출력해보자
# 5. 문자열 "Python:is:the:best"를 "Python#is#the#best"로 바꿔서 출려해보자.


