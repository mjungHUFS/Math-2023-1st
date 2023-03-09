'''
================================
딕셔너리  자료형: key:value 형식
================================
'''
# 딕서녀리 구성 key: value 
dic = {'name':'pey', 'phone':'01012341234', 'birth':'1212'}
print(dic['name'])
print(dic['birth'])
print(dic.keys()) # key
print(list(dic.keys())) # 리스트
print(dic.values()) # value
print(list(dic.values())) # 리스트 
print(dic.items()) # (key, value) 쌍 
dic.clear() # 모두 삭제 
print(dic)
print("="*20)

## dic.get(), key in dic
dic = {'name':'pey', 'phone':'01012341234', 'birth':'1212'}
#print(dic['nokey']) # error



# 추가/ 삭제 


# 주의사항


'''
================================
집합  자료형: 중복 불허용, 순서가 없음 
================================
'''
# 리스트, 문자열 => 집합
s1 = set([1,2,3])
print(s1)
s2 = set('hello')
print(s2)

# set => 리스트/튜플
l1= list(s1)
print(l1)
t1 = tuple(s1)
print(t1)

# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6,7])
s2 = set([4,5,6,7,8,9])
print(s1&s2) # 교집합
print(s1.intersection(s2))

print(s1| s2) #합집합
print(s1.union(s2))

print(s1-s2) #차집합
print(s2-s1)
print(s1.difference(s2))
print(s2.difference(s1))

# 추가/제거


## Exercise===================
# 1. a={'A':90, 'B':80, 'C':70}에서 'B'에 해당하는 값 추출하기
# 2. a=[1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]에서 중복 숫자 제거하고 출력하기


'''
================================
불  자료형: 참(true), 거짓(false) 
================================
'''
print(1==1)
print(2>1)
print(2<1)




'''
================================
변수를 만드는 여러가지 방법
================================
'''
a, b =('python', 'life')

