import numpy as np

fake_a = 3
fake_b = 76

x = np.array([2, 4, 6, 8]) # 공부 시간
y = np.array([81, 93, 91, 97]) # 점수

def predict(x) :
    return fake_a * x + fake_b

predict_result = []

for i in range(4) :
    predict_result.append(predict(x[i]))
    print("공부 시간 : {},  실제 점수 : {},  예측 점수 : {}".format(x[i], y[i], predict_result[i]))

def mse() :
    mse_num = 0
    for i in range(4) :
        mse_num += (y[i] - predict_result[i]) ** 2
    
    return mse_num / 4

print("mse : {}".format(mse()))