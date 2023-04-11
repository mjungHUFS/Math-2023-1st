## 반복문으로 팩토리얼 구하기
def factorial(n):


n = 5
print('%d!=%d'%(n, factorial(n)))

#================================================================
#  재귀함수: 자기 자신을 호출하는 것
#================================================================


#================================================================
# (예제) 팩토리얼 구하기 factorial(0)=1, factorial(n)=n*factorial(n-1) :
def factorial2(n):


n = 5
print('%d!=%d'%(n, factorial2(n)))
print('='*20)

#================================================================
## (예제) 독일 수학자 콜라츠(Collatz -> L.) 추측: 주어진 숫자가 짝수면 2로 나눈다.
# 주어진 숫자가 홀수면 3배한 후 1을 더한다.
def collatz(num):
    


collatz(7)
print()
collatz(128)
print()
##collatz(129)
#print()


def collatz_count(num):


print(collatz_count(7), "회") 
print(collatz_count(128), "회") 
print(collatz_count(129), "회") 
print()


#================================================================
# (예제) 피보나치 수열: 1, 1, n=(n-1)+(n-2)
def fibonacci(n):


n=10
print('fibonaci(%d)=%d'%(n, fibonacci(n)))
print('='*20)

# n=50일때 1시간 넘게 걸림!!

counter = 0
def fibonacci2(n):



n=10
fibonacci2(n)

print('fibonacci({}) 계산에 활용된 덧셈 횟수는 {}번입니다.'.format(n,counter))
print('='*20)
# fibonacci(10) 계산에 활용된 덧셈 횟수는 109번입니다.
# => 같은 값을 구하는 연산을반복하고 있기 때문에 발생!!!

#================================================================
## 메모화: 같은 값을 한번만 계산하도록 코드를 수정하기!
#================================================================

dict
def fibonacci_memo(n):


n=50
print('fibonaci(%d)=%d'%(n, fibonacci_memo(n))) # 엄청빠름!!
print()

# Exercise (facotiral 메모화) ==========================================
dict
def factorial_memo(n):


n=10
print(factorial_memo(n))
print('='*20)


