import sys
sys.dont_write_bytecode = True

import time
import os
from tabulate import tabulate
from termcolor import colored

from day01.xico_solution        import part1 as day01_part1, part2 as day01_part2
from day01.xico_solution_opt    import part1 as day01_part1_opt, part2 as day01_part2_opt

from day02.xico_solution        import part1 as day02_part1, part2 as day02_part2
from day02.luis_solution        import part1 as luis_day02_part1, part2 as luis_day02_part2

from day03.xico_solution        import part1 as day03_part1, part2 as day03_part2, part3 as day03_part3

def zero():
    pass

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

def generate_leaderboard(function_sets, person_labels, output_folder):
    # Use the first argument in each function set to determine labels
    labels = [functions[0] for functions in function_sets]
    structured_data = compare_functions_multirow(function_sets, labels, person_labels, return_structured=True)
    
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Write to separate Markdown files based on day and part
    file_content = {}
    
    for entry in structured_data:
        label = entry["label"]  # e.g., "Day 1.1"
        day, part = label.split(".")  # Separate "Day 1.1" into "Day 1" and "1.1"

        # Extract and format day number (e.g., "Day 1" -> "day01")
        day_number = day.split(" ")[1]
        filename = f"day{int(day_number):02}.md"  # Ensure zero-padded day numbers (e.g., "day01.md")
        part_title = f"## {part}\n\n"

        if filename not in file_content:
            file_content[filename] = [f"# Leaderboard for {day}\n\n"]

        leaderboard_section = []
        leaderboard_section.append(part_title)
        leaderboard_section.append("| Person | Runtime (ms) |\n")
        leaderboard_section.append("|--------|--------------|\n")
        
        # Combine person_labels and runtime_data for sorting
        combined_data = [
            (person_label, runtime_data["runtime"], runtime_data["formatted"], runtime_data["color"])
            for person_label, runtime_data in zip(person_labels, entry["runtimes"])
        ]
        # Sort by runtime (second item in the tuple)
        combined_data.sort(key=lambda x: x[1])
        
        for person_label, _, formatted_runtime, color in combined_data:
            color_indicator = f"**{formatted_runtime}**" if color == "green" else formatted_runtime
            leaderboard_section.append(f"| {person_label} | {color_indicator} |\n")
        leaderboard_section.append("\n")

        file_content[filename].extend(leaderboard_section)

    # Write to each file
    for filename, content in file_content.items():
        output_path = os.path.join(output_folder, filename)
        with open(output_path, "w") as output_file:
            output_file.writelines(content)

# Function sets
day_one_part1 = ["Day 1.1", day01_part1, zero]
day_one_part2 = ["Day 1.2", day01_part2_opt, zero]

day_two_part1 = ["Day 2.1", day02_part1, luis_day02_part1]
day_two_part2 = ["Day 2.2", day02_part2, luis_day02_part2]

day_three_part1 = ["Day 3.1", day03_part1]
day_three_part2 = ["Day 3.2", day03_part2, day03_part3]

# Person labels
person_labels = ["Xico", "Luis"]

output_folder = "leaderboards"

# Generate leaderboard using first argument as the line label
generate_leaderboard(
    [day_one_part1,     day_one_part2,
     day_two_part1,     day_two_part2,
     day_three_part1,   day_three_part2
     ],
    person_labels,
    output_folder
)
