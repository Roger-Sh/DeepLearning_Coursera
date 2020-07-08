import numpy as np
import time

a = np.array([1,2,3,4])
print(a)


# vectorized time demo

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print("Vectorized version time: " + str(1000*(toc-tic)) + "ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()
print("For loop time: " + str(1000*(toc-tic)) + "ms")

# broadcasting
A = np.array([[56.0, 0, 4.4, 68.0],
             [1.2, 104.0, 52.0, 8.0],
             [1.8, 135.0, 99.0, 0.9]])
print(A)

cal = A.sum(axis=0) # cal now is array, not matrix
print(cal)
print(cal.reshape(1,4)) # use reshape to turn cal into 1x4 matrix

percentage = 100*A/cal.reshape(1,4)
print(percentage)

# note for python
a = np.random.randn(5)
print(a)
print(a.shape)
print(a.T)
print(np.dot(a, a.T))
a = np.random.randn(5,1)
print(a)
print(a.T)
print(np.dot(a, a.T))

a = np.random.randn(3,3)
b = np.random.randn(3,1)
c = a*b
print(c)

w = np.zeros((2,1))


A = np.random.randn(4,3)
print("A: ", A)
B = np.sum(A, axis = 1, keepdims = True)
print("B: ", B)
print("B shape", B.shape)
print("B shape", B.shape[0])
print("B shape", B.shape[1])

L = len(A) # //2
print(L)

for i in range(1, 3):
    print(i)

a = np.random.randn(2,2)
print(a)