s = input()
j = input()

pos = 0

for i in range(len(j)):
    if pos < len(s) and j[i] == s[pos]:
        pos += 1

print(pos + 1)