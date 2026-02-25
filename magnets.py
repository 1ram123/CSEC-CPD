# Read the number of magnets
n = int(input())

# Read the first magnet
prev = input().strip()

# Initialize group count to 1 (first magnet starts a group)
groups = 1

# Process remaining magnets
for i in range(1, n):
    current = input().strip()
    
    # If current magnet is different from previous, it starts a new group
    if current != prev:
        groups += 1
        prev = current

# Output the result
print(groups)