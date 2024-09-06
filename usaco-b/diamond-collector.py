f = open("diamond.in", 'r')
info = f.readline().split()
N = int(info[0])
K = int(info[1])
diamondSize = []
for i in range(N):
	diamondSize.append(int(f.readline()))
f.close()

ans = 0
for i in range(N):
	amount = 0
	for j in range(N):
		if diamondSize[j] >= diamondSize[i] \
				and diamondSize[j] <= (diamondSize[i] + K):
			amount += 1
	if amount > ans:
		ans = amount

f = open("diamond.out", 'w')
f.write(str(ans) + "\n")
f.close()
