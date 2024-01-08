n,m,s,A,B = map(int, input().split())
a_array = list(map(int, input().split()))
b_array = list(map(int, input().split()))
               
a_array.sort(reverse=True)
b_array.sort(reverse=True)
               
prefix_a = [0] * (n+1)
prefix_b = [0] * (m+1)
               
for i in range(1, n+1):
    prefix_a[i] = a_array[i-1] + prefix_a[i-1]
 
for i in range(1, m+1):
    prefix_b[i] = b_array[i-1] + prefix_b[i-1]
               
max_cost = 0
               
for i in range(n+1):
    remainder = (s - (i*A))
               
    if remainder < 0:
        break
                   
    items_B = min(remainder//B, m)
    current_cost = prefix_a[i] + prefix_b[items_B]           
    max_cost = max(max_cost, current_cost)
                      
print(max_cost)
