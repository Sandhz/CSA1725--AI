def water_jug_problem(capacity_a, capacity_b, target):
    for a in range(capacity_a + 1):
        for b in range(capacity_b + 1):
            if a + b == target:
                return a, b
            if a + b > target and a <= capacity_b and b <= capacity_a:
                return a, b
    return None
capacity_a = 4
capacity_b = 3
target = 2
result = water_jug_problem(capacity_a, capacity_b, target)
if result:
    print(f"Solution found: Jug A = {result[0]}, Jug B = {result[1]}")
else:
    print("Solution not possible.")
