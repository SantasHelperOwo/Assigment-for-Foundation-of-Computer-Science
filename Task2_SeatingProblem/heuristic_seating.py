students = ["A", "B", "C", "D"]
friends = [("A", "B")]
same_city = [("C", "D")]

def is_valid(arrangement):
    for i in range(len(arrangement) - 1):
        pair = (arrangement[i], arrangement[i+1])
        if pair in friends or pair[::-1] in friends:
            return False
        if pair in same_city or pair[::-1] in same_city:
            return False
    return True

arrangement = []
remaining = students.copy()

while remaining:
    candidate = remaining.pop(0)
    if not arrangement:
        arrangement.append(candidate)
    else:
        placed = False
        for i in range(len(arrangement)+1):
            test = arrangement[:i] + [candidate] + arrangement[i:]
            if is_valid(test):
                arrangement = test
                placed = True
                break
        if not placed:
            arrangement.append(candidate)

print("Heuristic seating plan:")
print(arrangement)
