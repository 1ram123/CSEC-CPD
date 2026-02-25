n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1
sereja = 0
dima = 0
turn = True  # True = Sereja, False = Dima

while left <= right:
    if cards[left] > cards[right]:
        pick = cards[left]
        left += 1
    else:
        pick = cards[right]
        right -= 1

    if turn:
        sereja += pick
    else:
        dima += pick

    turn = not turn

print(sereja, dima)