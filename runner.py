import time
from tabulate import tabulate
from termcolor import colored

from day01.xico_solution import part1, part2

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
        
        for func in functions:
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

def generate_leaderboard(function_sets, labels, person_labels, readme_path):
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
    
day_one = [part1, part2]
day_two = [part2, part1]

function_labels = ["Day 01 - 1", "Day 01 - 2"]
person_labels = ["Xico", "Luis"]

generate_leaderboard(
    [day_one, day_two],
    function_labels,
    person_labels,
    "readme.md"
)

