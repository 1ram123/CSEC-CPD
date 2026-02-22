t = int(input())
r = input()
a = 0
d = 0
for i in r:
     if i == "A":
         a += 1
     elif i == "D":
         d +=1
if a > d:
     print("Anton")
elif d>a:
     print("Danik")
else:
     print("Friendship")