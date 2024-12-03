def open_file():
    string = ""
    with open("day03/input.txt") as f:
        for line in f:
            string += line
    return string

def part1():
    fileString = open_file()
    
    total = 0
    i, fileStringLen = 0, len(fileString)
    while(i < fileStringLen):
        if fileString[i:i+4] != "mul(":
            i += 1
            continue
        
        # Go to the char in front of "mul("
        i += 4

        arguments = ["", ""]
        foundVirgula = False
        while(fileString[i] != ")" and len(arguments[0]) < 4 and len(arguments[1]) < 3 and i < fileStringLen):
            if not foundVirgula and fileString[i] == ",":
                foundVirgula = True
                i += 1
                continue

            if fileString[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                i += 1
                break

            if foundVirgula: arguments[1] += fileString[i]
            else: arguments[0] += fileString[i]
            
            i += 1
        
        if fileString[i] == ")" and foundVirgula:
            # print(f"arguments: {arguments}")
            total += int(arguments[0]) * (int(arguments[1]))
    return total

def part2():
    fileString = open_file()
    
    total = 0
    i, fileStringLen = 0, len(fileString)
    do = True
    while(i < fileStringLen):
        if fileString[i] == "d":
            if fileString[i:i+4] == "do()":
                do = True
                i += 4
                continue
            elif fileString[i:i+7] == "don't()":
                do = False
                i += 7
                continue

        if fileString[i] != "m" or fileString[i:i+4] != "mul(":
            i += 1
            continue 
    
        i += 4

        arguments = ["", ""]
        foundVirgula = False
        while(fileString[i] != ")" and len(arguments[0]) < 4 and len(arguments[1]) < 3 and i < fileStringLen):
            if not foundVirgula and fileString[i] == ",":
                foundVirgula = True
                i += 1
                continue

            if not (47 < ord(fileString[i]) < 58):
                i += 1
                break

            if foundVirgula: arguments[1] += fileString[i]
            else: arguments[0] += fileString[i]
            
            i += 1
        
        if fileString[i] == ')' and foundVirgula:
            if do:
                total += int(arguments[0]) * int(arguments[1])

    return total

#print(part1())
print(part2())
# 190604937
# 82857512
def part3():
    fileString = open_file()
    import re

    exp = r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))"
    total_sum = 0
    matches = re.findall(exp, fileString)
    state = True
    for j in matches:
        if j[2] == "do()":
            state = True
        elif j[3] == "don't()":
            state = False
        elif state:
            total_sum += int(j[0]) * int(j[1])
    return total_sum

#print(part3())