k, r = map(int, input().split())

count = 1
while True:
    total = k * count
    last_digit = total % 10
    
    if last_digit == 0 or last_digit == r:
        print(count)
        break
    
    count += 1