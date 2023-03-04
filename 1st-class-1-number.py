"""
Author: miyoun jung
date: 2023-03-03

"""
"""
=======================================================
1. 자료형: 숫자, 문자열 등 자료 형태로 나타내는 모든 것
=======================================================
"""
"""
=================
(1) 숫자형 자료형
=================

"""
# 숫자형
a=4.24e-4
b=4.24E4 #=4.24e4
print(a)
print(b)
print() # 공백

a=1.234
b=12
print(type(a)) 
print(type(b))

# 덧셈 
a = 50
b = 100
c = a+b
print(a,'+', b,'=', c)
print('a','+', 'b','=', c)
print() 

# input (문자로 인식) 
a = input("첫번째 숫자를 입력하세요:") 
b = input("두번째 숫자를 입력하세요:")
c = a + b
print(a,'+', b,'=', c)
print()
## int(input()) 사용
a1 = int(input("첫번째 숫자를 입력하세요:"))
b1 = int(input("두번째 숫자를 입력하세요:"))
c1 = a1 + b1
print(a1,'+', b1,'=', c1)
print() 

print('a1*b1=', a1*b1)
# print('a*b=', a*b) # error  

# 곱셈, 제곱
a = 4; b=3;
c = a*b
d = a**b
print('a=', a, 'b=', b)
print('a*b', '=', c)
print('a**b', '=', d)
print()

# 나눗셈 
print('b/a=', b/a)
print('a/b=', a/b)
# 나눗셈 후 몫 반환
print('b//a=', b//a)
print('a//b=', a//b)
# 나눗셈 후 나머지 반환
print('b%a=',b%a)
print('a%b=',a%b)
print()

# 복합 연산 
a = 10
a +=5; print(a)
a -=5; print(a)
a *=5; print(a) 
a /=5; print(a)
a //=5; print(a)
a %=5; print(a)
a **=5; print(a)
print()


## print() 함수 사용: %d, %f, %s, .format 이용 
print("100")
print(100)
print("100+100");
print("%d" %(100+100))
#print("%d" %(100,100)) # error
#print("%d %d" % (100)) # error
print("%d %d" %(100, 200))
print("%d/%d=%d" %(100, 200, 0.5))
print("%d/%d=%f" %(100, 200, 0.5)) #소수 여섯짜리까지 (default)
print("%d" %123)
print("%5d" %123)
print("%05d" %123)
print("%f" %123.45)
print("%7.1f" %123.45) #소숫점둘째자리반올림
print("%7.3f" %123.45)
print("%s" % "Python")
print("%10s" % "Python")
print("{0:d} {1:5d} {2:05d}".format(123, 123, 123))
print("%d %5d %05d" % (123, 123, 123))
print("Error is %d%%" %98)

