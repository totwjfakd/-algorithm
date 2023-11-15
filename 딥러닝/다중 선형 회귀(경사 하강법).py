import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([2, 4, 6, 8]) # 공부 시간
x2 = np.array([0, 4, 2, 3]) # 과외 횟수
y = np.array([81, 93, 91, 97]) # 점수

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(x1, x2, y)
plt.show()


# 기울기 a와 y절편 b 초기화
a1 = 0
a2 = 0 
b = 0

lr = 0.01 # 학습률 정의

epochs = 3001

n = len(x1)

for i in range(epochs) :

    y_pred = a1 * x1 + a2 * x2 + b # 예측값
    error = y - y_pred # 오차값

    a1_diff = (2/n) * sum(-x1*error) # 오차 함수를 a1로 편미분한 값
    a2_diff = (2/n) * sum(-x2*error) # 오차 함수를 a1로 편미분한 값
    b_diff = (2/n) * sum(-(error)) # 오차 함수를 b로 편미분한 값

    a1 = a1 - lr * a1_diff # 학습률을 곱해 기존의 a1값을 업데이트
    a2 = a2 - lr * a2_diff # 학습률을 곱해 기존의 a1값을 업데이트
    b = b - lr * b_diff # 학습률을 곱해 기존의 b값을 업데이트

    if i % 100 == 0 : print("epoch = {},  기울기1 : {},  기울기2 : {},  절편 : {}".format(i, a1, a2, b))

y_pred = a1 * x1 + a2 * x2 + b # 최종 a, b값을 대입해 그래프를 그림
print("실제 점수 : ", y)
print("예측 점수 : ", y_pred)
ax.scatter3D(x1, x2, y)
plt.show()