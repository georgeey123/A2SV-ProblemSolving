t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    
    orbits = list(map(int, input().split()))
    
    planet_counts = {}
    for orbit in orbits:
        if orbit in planet_counts:
            planet_counts[orbit] += 1
        else:
            planet_counts[orbit] = 1

    total_cost = 0
    for count in planet_counts.values():
        if count > c:
            total_cost += c
        else:
            total_cost += count

    print(total_cost)
