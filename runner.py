import sys
sys.dont_write_bytecode = True

import time
from tabulate import tabulate
from termcolor import colored

from day01.xico_solution     import part1 as day01_part1, part2 as day01_part2
from day01.xico_solution_opt import part1 as day01_part1_opt, part2 as day01_part2_opt

def calculate_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = (time.perf_counter() - start_time) * 1000
        return result, elapsed_time
    return wrapper

def compare_functions_multirow(function_sets, labels, person_labels, return_structured=False):
    table = []
    structured_data = []

    for label, functions in zip(labels, function_sets):
        runtimes = []
        
        for func in functions[1:]:
            _, runtime = calculate_runtime(func)()
            runtimes.append(runtime)

        best_runtime = min(runtimes)
        worst_runtime = max(runtimes)

        row = [label]  # Start with the row label
        row_data = {"label": label, "runtimes": []}  # For structured output
        for runtime in runtimes:
            diff_percentage = ((runtime - best_runtime) / best_runtime) * 100
            formatted_runtime = f"{runtime:.4f} ms ({diff_percentage:+.2f}%)" if runtime != best_runtime else f"{runtime:.4f} ms"
            if runtime == best_runtime:
                row.append(colored(formatted_runtime, "green"))
                row_data["runtimes"].append({"runtime": runtime, "formatted": formatted_runtime, "color": "green"})
            elif runtime == worst_runtime:
                row.append(colored(formatted_runtime, "red"))
                row_data["runtimes"].append({"runtime": runtime, "formatted": formatted_runtime, "color": "red"})
            else:
                row.append(formatted_runtime)
                row_data["runtimes"].append({"runtime": runtime, "formatted": formatted_runtime, "color": None})
        table.append(row)
        structured_data.append(row_data)

    headers = ["Function"] + person_labels
    print(tabulate(table, headers=headers, tablefmt="grid"))
    if return_structured:
        return structured_data

def generate_leaderboard(function_sets, person_labels, readme_path):
    # Use the first argument in each function set to determine labels
    labels = [functions[0] for functions in function_sets]

    structured_data = compare_functions_multirow(function_sets, labels, person_labels, return_structured=True)
    leaderboard_lines = []
    leaderboard_lines.append("# Leaderboard\n\n")

    for entry in structured_data:
        label = entry["label"]
        leaderboard_lines.append(f"### {label}\n")
        leaderboard_lines.append("| Person | Runtime (ms) |\n")
        leaderboard_lines.append("|--------|--------------|\n")
        
        # Combine person_labels and runtime_data for sorting
        combined_data = [
            (person_label, runtime_data["runtime"], runtime_data["formatted"], runtime_data["color"])
            for person_label, runtime_data in zip(person_labels, entry["runtimes"])
        ]
        # Sort by runtime (second item in the tuple)
        combined_data.sort(key=lambda x: x[1])
        
        for person_label, _, formatted_runtime, color in combined_data:
            color_indicator = f"**{formatted_runtime}**" if color == "green" else formatted_runtime
            leaderboard_lines.append(f"| {person_label} | {color_indicator} |\n")
        leaderboard_lines.append("\n")

    with open(readme_path, "w") as readme_file:
        readme_file.writelines(leaderboard_lines)

# Function sets
day_one_part1 = ["Day 1.1", day01_part1, day01_part1_opt]
day_one_part2 = ["Day 1.2", day01_part2, day01_part2_opt]

# Person labels
person_labels = ["Xico", "Xico Opt"]

# Generate leaderboard using first argument as the line label
generate_leaderboard(
    [day_one_part1, day_one_part2],
    person_labels,
    "readme.md"
)
