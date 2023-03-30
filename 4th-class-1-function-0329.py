'''
=====================================
함수 
=====================================
'''
#===함수생성========
def add(a,b):
    
#===================

# 함수실행
a = 3
b = 4
c = add(a, b)
print(c)

print(add(3,4))

c = add(a=3, b=4)
print(c)

# 입력값이 없는 함수
def say():
    

a = say()
print(a)

# 결과값이 없는 함수 (return이 없음) 
def add(a,b):
    

add(3,4)
print(add(3,4)) #none값이 나옴

## Exercise 1. ======================================

## Exercise 2. =========================================



# 두 개의 값을 return ==================================
def add_and_mul(a,b):
    

result = add_and_mul(3,4)
print(result)

result1, result2 = add_and_mul(3,4)
print(result1, result2)

# return을 만나는 순간 함수를 빠져나감
def say_nick(nick):
    

    
say_nick('야호')
say_nick('바보')


#=== 가변매개변수를 받는 함수===============
def add_many(*args):


    return result
#===========================================

result= add_many(1,2,3)
print(result)
result2 = add_many(1,2,3,4,5,6,7,8,9)
print(result2)

## Exercise 1.================================================


## Exercise 2.================================================


#=== 여러 개의 입력값(가변매개변수포함)을 받는 함수==========
def add_mul(choice, *args):

            
    return result
#===========================================================
result= add_mul('add',1,2,3)
print(result)
result= add_mul('mul',1,2,3,4,5)
print(result)

# 예제1:
def print_n_times(n, *values):

    
print_n_times(3, 'hi', 'enjoy', 'python') 

# 예제2:  
def print_n_times(*values, n):

            
print_n_times('hi','enjoy','python', 3)



#======================================================
# 매개변수에 초깃값 미리 설정 (제일 마지막에 위치해야함)
def say_myself(name, age, man=True): 
    print('나의 이름은 %s입니다.' %name)
    print('나이는 %d살입니다.' %age)


#=====================================================

say_myself('홍길동', 27)
say_myself('홍길동', 27, True)
say_myself('홍길순', 25, False)


# 예제:
def test(a, b=10, c=100):

    
test(10,20,30)
test(a=10, b=100, c=200)
test(c=10,a=100, b=200)
test(10, c=200)

# 예제3:  
def print_n_times(*values, n=2):

            
print_n_times('hi','enjoy','python', 3)
print_n_times('hi','enjoy','python', n=3)


## Exercise 1. 오타가 발생하는 코드 찾기:===================

## Exercise 2. =============================================


#===========================================================    
## 함수 안에서 선언한 변수의 효력 범위 
a=1
def var_test(a):
    a = a+1
    return a

var_test(a) 
print(a) 

a = var_test(a)
print(a) 

## global 명령어*******
a=1


var_test() 
print(a)
#=========================================================== 

#==============================================
## lambda 사용하여 함수 만들기 (=def)
add = lambda a, b: a+b
result = add(3,4)
print(result)
#==============================================

## Exercise ======================================


