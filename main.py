from find_smallest import find_two_smallest
from lists_module import lists_of_integers
results = []

for integers in lists_of_integers:
    smallest_values = find_two_smallest(integers)
    results.append(smallest_values)

with open('result.txt', 'w') as f:
    for result in results:
        f.write(f"{result}\n")