from itertools import permutations

def get_largest_number(integers):
    integers = [str(x) for x in integers]
    all_permutations = ["".join(perm) for perm in permutations(integers)]
    return max(all_permutations)

print(get_largest_number([420, 42, 423]))