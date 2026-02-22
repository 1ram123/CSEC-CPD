t = input()
a = 0
b = 0
for i in t:
     if i.islower():
         a +=1
     else:
         b +=1
if a >= b:
     print(t.lower())
else:
     print(t.upper())