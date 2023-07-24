def count_good_pairs(n, a, b):
    differences = [ai - bi for ai, bi in zip(a, b)]
 
    differences.sort(reverse=True)
 
    ans = 0
 
    for i in range(n):
        if differences[i] > 0:
            v = -differences[i]
            l, r = 0, n
 
            while l < r - 1:
                mid = (l + r) // 2
                if differences[mid] <= v:
                    r = mid
                else:
                    l = mid
 
            ans += l - i
 
    return ans
