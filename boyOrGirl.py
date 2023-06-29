username = input()

unique_char = set(username)

if len(unique_char) % 2 != 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")