import time

def open_file():
    reports = []
    with open("day02/input.txt") as f:
        for line in f:
            reports.append([int(char) for char in line.strip().split(" ")])
    return reports

def part1():
    reports = open_file()

    total_safe_reports = 0
    for report in reports:
        valid = True
        old_state, new_state = 0, 0
        for i in range(1, len(report)):            
            if not valid:
                continue
            curr_diff = report[i] - report[i - 1]

            if curr_diff < 0:
                new_state = -1
            elif curr_diff > 0:
                new_state = 1;
        
            if abs(curr_diff) > 3 or (i > 1 and (new_state != old_state or curr_diff == 0 )):
                valid = False
            
            old_state = new_state

        if valid:
            total_safe_reports += 1  
        
    return total_safe_reports       

def part2():
    reports = open_file()

    total_safe_reports = 0
    for report in reports:
        valid = True
        old_state, new_state = 0, 0
        ignore_index = -1
        for i in range(0, len(report) - 1):
            if not valid:
                continue

            curr_diff = report[i] - report[i + 1]

            if curr_diff < 0:
                new_state = -1
            elif curr_diff > 0:
                new_state = 1;
        
            if abs(curr_diff) > 3 or (i > 0 and (new_state != old_state or curr_diff == 0 )):
                valid = False
            
            old_state = new_state

        if valid:
            total_safe_reports += 1  
        
    return total_safe_reports  

print(part1())
print(part2())