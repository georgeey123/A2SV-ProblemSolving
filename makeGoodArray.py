sequence = [1]
while sequence[-1] < 10**18:
	sequence.append(sequence[-1]*2)

sequence.pop()

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))

	print(n)
	for i in range(n):
		print(i+1, min([j for j in sequence if a[i] <= j]) - a[i])
