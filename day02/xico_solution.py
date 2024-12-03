import time

def open_file():
    reports = []
    with open("day02/input.txt") as f:
        for line in f:
            reports.append([int(char) for char in line.strip().split(" ")])
    return reports

def isReportValid(report):
    old_state, new_state = 0, 0
    for i in range(1, len(report)):            
        curr_diff = report[i] - report[i - 1]

        if curr_diff < 0:
            new_state = -1
        elif curr_diff > 0:
            new_state = 1;
    
        if abs(curr_diff) > 3 or (i > 1 and (new_state != old_state or curr_diff == 0 )):
            return False
        
        old_state = new_state

    return True

def part1():
    reports = open_file()

    total_safe_reports = 0
    for report in reports:
        total_safe_reports += isReportValid(report)
    return total_safe_reports       


def part2():
    reports = open_file()

    total_safe_reports = 0
    for report in reports:
        if isReportValid(report):
            total_safe_reports += 1
        else:
            for i in range(0, len(report)):
                removed_element = report.pop(i)
                if isReportValid(report):
                    total_safe_reports += 1
                    break
                else:
                    report.insert(i, removed_element)

    return total_safe_reports       

#print(part1())
#print(part2())
# 463
# 514