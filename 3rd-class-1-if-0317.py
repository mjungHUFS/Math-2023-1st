'''
====================================
조건문: if 문
====================================
'''
# 예제 1 ======================================
money=True
if money:
    print("get a taxi")
else:
    print("take a walk")

# 비교연산자: # x<y, x==y, x!=y, x>=y
money=2000


# x or y, x and y, not x
money=2000; card = True;


# x in 리스트/튜플/문자열 / x not in 리스트/튜플/문자열 
pocket = ['paper','cellphone', 'money']


# pass (조건문에서 아무일도 하지 않게 설정)
pocket = ['paper','cellphone', 'money']
  

# elif 구문 
pocket = ['paper','cellphone']
card = True;


# elif 구문 
pocket = ['paper','cellphone']
card = True;


# 예제2 =====================================
import datetime # 모듈
now = datetime.datetime.now()

print(now.year,'년', now.month,'월', now.day, '일', now.hour, '시', now.minute, '분', now.second, '초')
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month, now.day, now.hour, now.minute, now.second))

if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
else:
     print("현재 시각은 {}시로 오후입니다!".format(now.hour))
     

## Exercise ================================



'''
====================================
반복문: while 문
====================================
'''
# 예제 1
treehit=0;
while treehit<10:
    treehit=treehit+1
    print('나무를 %d번 찍었습니다.' %treehit)
    if treehit==10:
        print("나무 넘어갑니다")

# 예제 2
prompt = '''
1. Add
2. Del
3. List
4. Quit

Enter number: '''

number=2
while number!=4:
    print(prompt)


# 예제 3 : break 사용하여 중지
coffee =10 # 커피갯수
money = 300 # 자판기에 넣을 돈
while money:
    print("돈을 받았으니 커피를 줍니다.")


# 예제 4
coffee = 1 #커피갯수 



#while True:
#    print('Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.')


# 예제 5: continue 사용


# Exercise ==============================





