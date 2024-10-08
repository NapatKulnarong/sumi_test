n = int(input())
if 1 <= n <= 10000:
    sum_n = 0
    for i in range(n):
        sum_n += (i+1)
    print(sum_n)