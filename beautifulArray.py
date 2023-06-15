n = int(input())
array = list(map(int, input().split()))
 
def split_array(array):
    neg_set = []
    pos_set = []
    zero_set = []
 
    for number in array:
        if number < 0:
            neg_set.append(number)
        elif number > 0:
            pos_set.append(number)
        else:
            zero_set.append(number)
 
    if len(neg_set) % 2 == 0:
        zero_set.append(neg_set.pop())
    
    if len(pos_set) == 0:
        if len(neg_set) % 2 == 1:
            pos_set.extend(neg_set[:2])
            del neg_set[:2]
            
    
    
    print(len(neg_set), *neg_set)
    print(len(pos_set), *pos_set)
    print(len(zero_set), *zero_set)
 
split_array(array)
