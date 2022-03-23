A = int(input())
B = int(input())
N = int(input())

A = A // N + int(A % N != 0)
B = B // N + int(B % N != 0)

print("Yes") if A > B else print("No")
