import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4, 6, 8]) # 공부 시간
y = np.array([81, 93, 91, 97]) # 점수

plt.scatter(x,y)
plt.show()


# 기울기 a와 y절편 b 초기화
a = 0 
b = 0

lr = 0.03 # 학습률 정의

epochs = 2001

n = len(x)

for i in range(1, epochs) :

    y_pred = a * x + b # 예측값
    error = y - y_pred # 오차값

    a_diff = (2/n) * sum(-x*error) # 오차 함수를 a로 편미분한 값
    b_diff = (2/n) * sum(-(error)) # 오차 함수를 b로 편미분한 값

    a = a - lr * a_diff # 학습률을 곱해 기존의 a값을 업데이트
    b = b - lr * b_diff # 학습률을 곱해 기존의 b값을 업데이트

    if i % 100 == 0 : print("epoch = {},  기울기 : {},  절편 : {}".format(i, a, b))

y_pred = a * x + b # 최종 a, b값을 대입해 그래프를 그림

plt.scatter(x, y)
plt.plot(x, y_pred, 'r')
plt.show()