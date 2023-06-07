n = int(input())

english_subs = set(map(int, input().split()))

m = int(input())

french_subs = set(map(int, input().split()))

english_only_subs = english_subs.difference(french_subs)

print(len(english_only_subs))
