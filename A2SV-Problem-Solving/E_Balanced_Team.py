students = int(input())
skills = list(map(int, input().split()))

skills.sort()
max_students = 0
l = 0

for r in range(students):
    while skills[r] - skills[l] > 5:
        l += 1

    max_students = max(max_students, r - l + 1)

print(max_students)
