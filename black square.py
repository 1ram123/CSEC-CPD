cal = list(map(int, input().split()))
steps = input()

total = 0

for s in steps:
    total += cal[int(s) - 1]

print(total)