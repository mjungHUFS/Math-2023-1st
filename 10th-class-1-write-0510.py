
'''
=====================================
구글 drive 연동 & 현재 directory 설정
=====================================
'''
# colab에서 google drive와 연결

from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir("/content/drive/MyDrive/2023-Class-Codes/")


'''
=====================================
파일 생성하기 'w'
=====================================
'''

f= open('Newfile.txt', 'w') # write


#================================
#'r'은 읽기전용으로 파일을 오픈합니다. 읽기만 가능하고, 쓰기는 되지 않습니다.
#'w' 는 쓰기 모드인데, 파일을 새로 만듭니다. 즉, 동일한 이름의 파일이 있으면 지우고 새로 작성합니다.
#'a' 는 쓰기 모드인데, 'w' 와는 다르게 기존 파일에 내용을 이어서 작성합니다.
# ===============================

'''
=====================================
파일 읽기'r'
=====================================
'''
# readline 함수: 가장 첫번째 줄이 화면에 출력
f = open('Newfile.txt','r') # read


f = open('Newfile.txt','r')



# readlines 함수 :
# 파일 내용 전체를 가져와 리스트로 반환합니다. 각 줄은 문자열 형태로 리스트의 요소로 저장
f = open('Newfile.txt','r')

# read 함수: 한꺼번에 읽기
# 파일 내용 전체를 가져와 문자열로 반환/ 각각의 줄은 '\n' 문자로 구분
f = open('Newfile.txt','r')





'''
=====================================
파일 내용 추가 'a'
=====================================
'''
f = open('Newfile.txt','a') # 추가 모드

## Exercise
import random

f = open('lotto.txt', 'a')
num = input("횟수를 입력해주세요 :")


#=================================
# with 문 사용하기
f = open('Newfile3.txt', 'w')
f.write('life is beautiful.')
f.close()


#===================================

## Exercise: with 사용

    

#========================================================
# 예제: 랜덤하게 100명의 키와 몸무게 만들기
import random

hangle = list("가나다라마바사아자차카타파하")

with open("Newfile2.txt", "w") as file:

    
# 예제: 파일 한줄씩 읽기
with open("Newfile2.txt", "r") as file:

        

# Exercise ==========================



