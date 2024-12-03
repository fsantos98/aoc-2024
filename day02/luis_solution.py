def report_is_valid(report, report_type):
    if(report_type > 0):
        for i in range(len(report) - 1):
            if( (int(report[i + 1]) - int(report[i]) > 3) or (int(report[i + 1]) - int(report[i]) <= 0)):
                return 0
        return 1
    else:
        for i in range(len(report) - 1):
            if( (int(report[i + 1]) - int(report[i]) < -3)  or (int(report[i + 1]) - int(report[i]) >= 0)):
                return 0
        return 1


def part1():
    answer = 0
    with open('day02/input.txt', 'r') as f:
        line = f.readline().split()
        while line:
            report_type = int(line[1]) - int(line[0])
            answer = answer + report_is_valid(line, report_type)
            line = f.readline().split()
    f.close()
    return answer

def remove_index(lst, index):
    return lst[:index] + lst[index + 1:]

def report_is_valid_2(report, report_type, problem_dampener):
    if(report_type > 0):
        for i in range(len(report) - 1):
            if( (int(report[i + 1]) - int(report[i]) > 3) or (int(report[i + 1]) - int(report[i]) <= 0)):
                if(problem_dampener == 0):
                    return 0
                temp_list1 = remove_index(report, i+1)
                temp_list2 = remove_index(report, i)
                temp_list3 = remove_index(report, i-1)
                report_type1 = int(temp_list1[1]) - int(temp_list1[0])
                report_type2 = int(temp_list2[1]) - int(temp_list2[0])
                report_type3 = int(temp_list3[1]) - int(temp_list3[0])
                return ( report_is_valid_2(temp_list1, report_type1, 0) or report_is_valid_2(temp_list2, report_type2, 0) or report_is_valid_2(temp_list3, report_type3, 0))
        return 1
    else:
        for i in range(len(report) - 1):
            if( (int(report[i + 1]) - int(report[i]) < -3)  or (int(report[i + 1]) - int(report[i]) >= 0)):
                if(problem_dampener == 0):
                    return 0
                temp_list1 = remove_index(report, i+1)
                temp_list2 = remove_index(report, i)
                temp_list3 = remove_index(report, i-1)
                report_type1 = int(temp_list1[1]) - int(temp_list1[0])
                report_type2 = int(temp_list2[1]) - int(temp_list2[0])
                report_type3 = int(temp_list3[1]) - int(temp_list3[0])
                return ( report_is_valid_2(temp_list1, report_type1, 0) or report_is_valid_2(temp_list2, report_type2, 0) or report_is_valid_2(temp_list3, report_type3, 0))
        return 1
    
def part2():
    answer = 0
    with open('day02/input.txt', 'r') as f:
        line = f.readline().split()
        while line:
            report_type = int(line[1]) - int(line[0])
            answer = answer + report_is_valid_2(line, report_type, 1)
            line = f.readline().split()
    f.close()
    return answer
