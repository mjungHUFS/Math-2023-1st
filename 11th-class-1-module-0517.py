'''
=====================================================
Module (모듈): 함수, 변수, 클래스를 모아 놓은 파일
====================================================
'''
# module: math =====================================================
import math


# round는 정수가 홀수일때 내리고, 정수부분이 짝수일때 올림.
# round는 반올림함수가 아님=> 사용할 일이 거의 없음



# from 모듈이름 import 가져오고 싶은 함수 또는 변수
from math import sin, cos, tan, floor, ceil


# from 모듈이름import * (모듈 내부의 모든 것을 가져
#=> 식별자 이름에서 충돌 발생할 수 있음
#=> 최대한 필요한 것만 가져와서 사용하는 것이 좋음


# import 모듈이름 as 사용하고 싶은 식별자
import math as m


# module: random ======================================================
import random

# random(): 0<=x<1 사이의 float을 리턴

# uniform(min, max): 지정한 범위 사이의 float을 리턴

# randrange(): 지정한 범위의 int를 리턴

# choice(list): 리스트 내부 요소를 랜덤하게 선택

# shuffle(list): 리스트 내부 요소를 랜덤하게 섞음

# sample(list, k=숫자): 리스트 요소 중에서 k개를 뽑음


from random import random, uniform, randrange, choice, shuffle, sample

# module: os ============================================================
# colab에서 google drive와 연결
from google.colab import drive
drive.mount('/content/drive')

import os
os.chdir("/content/drive/MyDrive/2023-Class-Codes/") #디렉토리 위치 변경 

#현재 운영제체 (포직스, 이식형 운영체계 인터페이스)
#현재 폴더
#현재 폴더 내부요소/ listdir(path)

# 폴더 제거하고 만들기


# 파일을 생성하고 파일 이름을 변경


# 파일 제거하기

#어느 것을 사용해도 무방함


# 현재 디렉터리를 읽어들이고 파일인지 디렉터리(폴더)인지 구분하기


#폴더의 요소읽어들이기


# module: urllib 모듈 =======================================================
from urllib import request

# urlopen()함수로 링크 열기
target = request.urlopen('https://google.com')


# BeautifluSoup ==========================================
## Beautiful Soup is a Python library for pulling data
## out of HTML and XML files.

from urllib import request


# urlopen() 함수로 기상청의 전국날씨 읽기
target = request.urlopen('https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')
# BeautifulSoup을 사용해 웹 페이지를 분석 (parser: 문장의 구조 분석·오류 점검 프로그램)


# location 태그를 찾음/ select() 함수는 여러개를 선택/ select_one() 함수는 원하는 값을 추출

      
# Exercise: csv 파일로 저정해보기       
