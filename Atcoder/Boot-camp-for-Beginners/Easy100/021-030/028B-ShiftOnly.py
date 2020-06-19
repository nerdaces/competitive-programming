n = int(input())
a = list(map(int, input().split()))

cnt = 0
while True:
    for i in range(n):
        if a[i] % 2 != 0:
            print(cnt)
            exit()
        else:
            a[i] /= 2
    cnt += 1

# def how_many_times_divisible(n):
# 	ans = 0
# 	while n % 2 == 0:
# 		n /= 2
# 		ans += 1
# 	return ans
# 
# n = int(raw_input())
# a = map(int, raw_input().split())
# ans = min(map(how_many_times_divisible, a))
# 
# print ans