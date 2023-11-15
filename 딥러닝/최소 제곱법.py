import numpy as np

x = np.array([2, 4, 6, 8]) # 공부 시간
y = np.array([81, 93, 91, 97]) # 점수

x_mean = np.mean(x)
y_mean = np.mean(y)

print("X 평균 값 : {}".format(x_mean))
print("Y 평균 값 : {}".format(y_mean))

# 기울기의 분모
divisor = sum([(x_num - x_mean)**2 for x_num in x])

# 기울기의 분자

def top(x, mx, y, my) :
    d = 0
    for i in range(4) :
        d += (x[i] - mx) * (y[i] - my)
    return d
dividend = top(x, x_mean, y, y_mean)

print("분자 : {}".format(dividend))
print("분모 : {}".format(divisor))

a = dividend / divisor

print("기울기 : {}".format(a))

yv = y_mean - (x_mean * a)

print("y절편 : {}".format(yv))

