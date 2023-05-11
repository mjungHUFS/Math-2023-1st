#
# CSV란, Comma-seperated values의 줄임말로, 쉼표로 정보가 구분되어져 있는 파일을 의미함.
# CSV는 정보가 콤마로 구분되어져 있다는 개념 뿐이고 실제로 CSV이지만 .csv가 아닌.txt로 저장되어 있는 경우도 종종 있음.
# 엑셀이 깔려져 있는 컴퓨터에서는 .csv파일들을 엑셀로 기본으로 보여줌
#

import csv

# 파일 쓰기 ============================
data = [
    ['id', 'name', 'price', 'amount'],
    ['1', 'apple', '5000', '5'],
    ['2', 'pencil', '500', '42'],
    ['3', 'pineapple', '8000', '5'],
    ['4', 'pen', '1500', '10']
]

f = open("data2.csv", "w")



# 파일 읽기 ==============================

#for문으로 reader를 읽어들이면 각 행을 콤마로 구분한 리스트로 불러옴
f = open("data.csv", "r")


# data 변수에는 2차원의 리스트로 저장
data = list(reader)


# 파일 추가 ==============================
f = open("data.csv", "a", newline = '')



##  dictionary 형태로 주어진 파일 쓰고 읽기 ==========================
'''
# 위 방법들의 단점은 각 행이 리스트로 표현되다 보니 각 행별로 뜯어서 보면 몇번째 항목이 무슨 항목을 의미하는 것인지 직관적으로 알 수 없다
# 만약, 데이터를 알기 쉽게 딕셔너리의 형태로 제공했다면?
[
    {'id': '1', 'name': 'apple', 'price': '5000', 'amount': '5'},
    {'id': '2', 'name': 'pencil', 'price': '500', 'amount': '42'},
    {'id': '3', 'name': 'pineapple', 'price': '8000', 'amount': '5'},
    {'id': '4', 'name': 'pen', 'price': '1500', 'amount': '10'}
]
'''
## ===================================================================


# 파일 쓰기 ======================================================
# 파일을 쓸 때에도, csv.writer를 쓸 때와 비슷하지만 fieldnames를 DictWriter를 불러올 때 인자로 같이 넘겨주어야 함
import csv

fieldnames = ['id', 'name', 'price', 'amount']
data = [
    {'id': '1', 'name': 'apple', 'price': '5000', 'amount': '5'},
    {'id': '2', 'name': 'pencil', 'price': '500', 'amount': '42'},
    {'id': '3', 'name': 'pineapple', 'price': '8000', 'amount': '5'},
    {'id': '4', 'name': 'pen', 'price': '1500', 'amount': '10'}
]

f = open("data2.csv", "w")


# 파일 읽기 =======================
f = open("data.csv", "r")


# 파일 추가  =======================
f = open("data2.csv", "a")
