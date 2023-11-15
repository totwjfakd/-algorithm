import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x = np.array([[2, 0], [4, 4], [6, 2], [8, 3]]) # 공부 시간
y = np.array([81, 93, 91, 97]) # 점수

model = Sequential()

# 출력 값, 입력 변수, 분석 방법에 맞게끔 모델을 설정
model.add(Dense(1, input_dim=2, activation='linear'))
#오차 수정을 위해 경사 하강법(sgd)을, 오차의 정도를 판단하기 위해 평균 제곱 오차(mse)를 사용
model.compile(optimizer='sgd', loss='mse')


model.fit(x, y, epochs=2000)


hour = 7
private_class = 4
prediction = model.predict([[hour, private_class]])

print("{}시간을 공부하고 {}번의 과외를 받을 경우 예상 점수는 {}점입니다.".format(hour, private_class, prediction[0][0]))
