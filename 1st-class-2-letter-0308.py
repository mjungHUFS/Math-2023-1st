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

# 문자열 연산
a= "python"; b=" is fun";
print(a+b)
print(a*2) # pythonpython
print("="*50)
print("my program")
print("="*50)

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
"{0:!>10}".format('hi') # 오른쪽정렬 & 공백!로 채우기    '

# Exercise
# 위 문장을 변경하고 format을 이용하여 다음 결과가 나오도록 출력코드를 작성하여라:
# I ate 5!!!!!!!!! apples, so I was sick for ==two=== days.


# f'문자열' 문자열 포맷팅 (따옴표 사용 주의!!!)
f'hi'
f'{"hi"}'
# f'{'hi'}' # error (따옴표 혼용해서 쓰면 안됨)
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

# Exercise
# 위 문장을 변경하고 f'을 이용하여 다음 결과가 나오도록 출력코드를 작성하여라:
# I ate 5!!!!!!!!! apples, so I was sick for ==two=== days.


# 문자열 크기
a='life is beautiful, enjoy it'
 

# 문자열 바꾸기
a="pithon"



# 문자열 관련 함수
a ="Python is the best choice"


# 문자열 삽입(join): 따옴표 상관없음


# 문자열 공백 없애기 
a = " hi "



## ========= Exercise ===========



