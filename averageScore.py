n, x = input().split(' ')

subject = []
for i in range(int(x)):
    subject = subject + [map(float, input().split(' '))]
    
print( *[sum(x)/len(x) for x in zip(*subject)], sep = '\n')
