from typing import List

employees_happiness = input().split()
happiness_factor_improvement = int(input())
employees_happiness_to_int = list(map(lambda x: int(x) * happiness_factor_improvement,
                                      employees_happiness))

filtered = list(filter(lambda x: x >= (sum(employees_happiness_to_int) /
                                       len(employees_happiness_to_int)), employees_happiness_to_int))

if len(filtered) >= len(employees_happiness_to_int) / 2:
    print(f"Score: {len(filtered)}/{len(employees_happiness_to_int)}. Employees are happy!")
else:
    print(f'Score: {len(filtered)}/{len(employees_happiness_to_int)}. Employees are not happy!')