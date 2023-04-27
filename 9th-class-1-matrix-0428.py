# 행렬 ============================================
A = [[2,7], [3,4], [6,1]]
print(len(A))
print(len(A[0]))


# 행렬의 원소곱/ 행렬곱
A = [[2,7], [3,4], [6,1]]
B = [[1,4], [4,-1], [2,5]]

def element_product(A,B):


C = element_product(A,B)
print(C)

## 행렬곱
A = [[2,7], [3,4], [6,1]]
B = [[3,-3,5],[-1,2,-1]]
print(len(A))
print(len(A[0]))
print(len(B[0]))

def matrix_mul(A,B):



C=matrix_mul(A,B)
print(C)

#=================================================
# Ax=b 풀기 
#=================================================

A = [[1, -1, 2, 1],
     [5, 8, 6, 3],
     [4, 2, 5, 3],
     [3, 2, 1, 4]]
b = [2, 10, 3, 1]
x = list(range(0,4))

# forward elimination (upper triangular matrix)



print(A)
print(b)
print('='*20)

# Back substitution


print('x=', x)

## Exercise: Ax=b 푸는 함수 만들기 ============================
def solve(A,b):



A = [[1, -1, 2],
    [5, 8, 6],
    [4, 2, 5]]
b = [2, 10, 3]
x = solve(A,b)



## np.array 이용하여 행렬 계산하기 ===============================
import numpy as np

A = np.array([[2,7], [3,4], [6,1]])
B = np.array([[1,4], [4,-1], [2,5]])

# 행렬 덧셈, 뺄셈, 곱셈, 스칼라곱, 원소곱, 행렬곱
print(A+B)
print(A-B)
print(2*A)


B = np.array([[3,-3,5],[-1,2,-1]])



# transpose A^T
A = np.array([[3,-3,5],[-1,2,-1],[2, 4, 5]])


# diagonal matrix


# identity matrix

# Upper/lower trianglur matrix


# determinant/ inverse / x=A^-1*b
A = np.array([[1.0, -1.0, 2.0],
     [5.0, 8.0, 6.0],
     [4.0, 2.0, 5.0]])



