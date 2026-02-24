y, w = map(int, input().split())

m = max(y, w)
f = 6 - m + 1

if f == 6:
    print("1/1")
elif f == 5:
    print("5/6")
elif f == 4:
    print("2/3")
elif f == 3:
    print("1/2")
elif f == 2:
    print("1/3")
else:
    print("1/6")