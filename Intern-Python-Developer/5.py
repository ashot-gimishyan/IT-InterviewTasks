import itertools

string = input()
N = int(string[0])
k = int(string[2])

good_ls = list()
for i in range(1, N+1):
    good_ls.append(i)

peres_ls = list(set(itertools.permutations(good_ls)))

count = 0
summ = 0

for peres in peres_ls:
    for i in range(1, N+1):
        summ += i * peres[i-1]
    if summ % k == 0:
        count += 1
    summ = 0

print(count)
