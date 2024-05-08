import math

def calculate_speed_and_direction(x, y):
    # 벡터의 방향을 계산하고, 라디안에서 도 단위로 변환
    direction = math.degrees(math.atan2(y, x))
    
    # 벡터의 크기 계산
    speed = math.sqrt(x**2 + y**2)
    
    return direction, speed

# 주어진 벡터 값
x = -29.287765534821393
y = -6.526658063337438

# 방향과 속력 계산
direction, speed = calculate_speed_and_direction(x, y)

print("방향(도):", direction)
print("속력:", speed)