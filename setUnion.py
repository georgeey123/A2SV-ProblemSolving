n = int(input())

english_subs = set(map(int, input().split()))

m = int(input())

french_subs = set(map(int, input().split()))

only_one_sub = english_subs.union(french_subs)

print(len(only_one_sub))
