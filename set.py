def perform_set_operations(set1, set2):
    
    union_set = set1.union(set2)
    print(f"Union of E and N is {union_set}")

    intersection_set = set1.intersection(set2)
    print(f"Intersection of E and N is {intersection_set}")

    difference_set1 = set1.difference(set2)
    print(f"Difference of E and N is {difference_set1}")

    symmetric_difference_set = set1.symmetric_difference(set2)
    print(f"Symmetric difference of E and N is {symmetric_difference_set}")

E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

perform_set_operations(E, N)
