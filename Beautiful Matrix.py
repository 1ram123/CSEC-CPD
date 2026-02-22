t = [[],[],[],[],[]]
for i in range(5):
     ls = list(map(int,input().split()))
     t[i] = ls
l =[]
for k in range(5):
     for j in range(5):
         if t[k][j] == 1:
             l = [k,j]
f = 2
d = 2

print(abs(f - l[0]) + abs(d - l[1]))