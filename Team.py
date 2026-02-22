t = int(input())
f = 0
for _ in range(t):
     a = list(map(int,input().split()))
     s = sum(a)
     if s >= 2:
         f += 1
print(f)