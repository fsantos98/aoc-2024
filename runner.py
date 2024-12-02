import time
from tabulate import tabulate
from termcolor import colored

from day01.solution import part1, part2

def calculate_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = (time.perf_counter() - start_time) * 1000
        return result, elapsed_time
    return wrapper

def compare_functions_multirow(function_sets, labels, person_labels):
    table = []

    for label, functions in zip(labels, function_sets):
        runtimes = []
        
        for func in functions:
            _, runtime = calculate_runtime(func)()
            runtimes.append(runtime)

        best_runtime = min(runtimes)
        worst_runtime = max(runtimes)

        row = [label]  # Start with the row label
        for runtime in runtimes:
            diff_percentage = ((runtime - best_runtime) / best_runtime) * 100
            formatted_runtime = f"{runtime:.4f} ms ({diff_percentage:+.2f}%)" if runtime != best_runtime else f"{runtime:.4f} ms"
            if runtime == best_runtime:
                row.append(colored(formatted_runtime, "green"))
            elif runtime == worst_runtime:
                row.append(colored(formatted_runtime, "red"))
            else:
                row.append(formatted_runtime)
        table.append(row)

    headers = ["Function"] + person_labels
    return tabulate(table, headers=headers, tablefmt="grid")

day_one = [part1, part2]
day_two = [part2, part1]

function_labels = ["Day 01 - 1", "Day 01 - 2"]
person_labels = ["Xico", "Luís"]

print(compare_functions_multirow(
    [day_one, day_two],
    function_labels,
    person_labels
))