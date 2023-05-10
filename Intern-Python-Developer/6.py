import itertools

string = input()
N = int(string[0])
k = int(string[2])

ls_in = input().split(' ')
ls_in = [int(ls_in[i]) for i in range(N)]
ls = list(itertools.combinations(ls_in, k))

count = 0
for elem in ls:
    if all(elem[i] > elem[i+1] for i in range(len(elem) - 1)):
        count += 1

print(count % (10 ** 9 + 7))
