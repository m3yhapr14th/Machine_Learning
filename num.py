import numpy as np

# 넘파이 1차원 배열 (1x1)
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 3.0, 4.0])

print(x + y) # 같은 위치에 있는 원소들끼리의 합
print(x * y) # 같은 위치에 있는 원소들끼리의 곱
print(x / y)
print(x * 2.0) # x의 각 위치에 있는 원소들에 2.0(스칼라값)을 곱함

# N차원 배열
# 2차원 배열
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [2, 3]])
c = np.array([[2, 4], [3, 2], [7, 8]]) # 3 x 2 행렬

print(a)
print(b)
print(c)
print(a.shape) # 행렬 형상 (2x2)
print(c.shape) # 3x2
print(a.dtype) # 원소의 자료형 dtype

# 원소의 배열(형상)이 다르므로 오류
# d = a * c
# print(d)

print("-------------")

# 원소 접근
print(a[0])
print(a[0][0])
print(a[0][1])
print(a[1])
print(a[1][0])


# 평탄화
print(a)
X = a.flatten()
print(X)
# 평탄화된 원소들의 인덱스 값으로 값 찾기
print(X[np.array([0,2,3])])

# 특정 조건을 만족하는 원소 값 추출 가능
# X > 2 이상 값을 얻고 싶을 때
print(X > 2) # type(bool) 값으로 표출(True or False)
print(X[X>2])