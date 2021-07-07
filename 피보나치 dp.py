def fibonacci (n) : 
    if n == 0 : 
        return 0
    if n == 1 :
        return 1
    if dp[n] != -1 :
        return dp[n]
    dp[n] = fibonacci(n-2) + fibonacci(n-1)
    return dp[n]

num = int(input("n : "))
dp = []
for i in range(41) :
    dp.append(-1)


print ("n번째 피보나치 수열의 값 : {}".format(fibonacci(num)))
