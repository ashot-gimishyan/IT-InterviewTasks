N = int(input())

while(N % 10 == 0):
    N //= 10

count = 0
while(N != 0):
    if N % 10 == 0:
        count += 1
    N//= 10

print(count)
