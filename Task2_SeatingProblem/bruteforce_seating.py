import itertools

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

valid_arrangements = []
for perm in itertools.permutations(students):
    if is_valid(perm):
        valid_arrangements.append(perm)

print("Valid seating plans:")
for plan in valid_arrangements:
    print(plan)
