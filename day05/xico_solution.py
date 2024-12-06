import time

def open_file(file):
    rules = {}
    updates = []
    allRules = False
    with open(file) as f:
        for line in f:
            if line == "\n":
                allRules = True
                continue

            if allRules:
                updates.append(line.strip().split(","))
            else:
                n1, n2 = line.strip().split("|")
                if n1 in rules:
                    rules[n1].append(n2)
                else: rules[n1] = [n2]
    return rules, updates

def part1():

    rules, updates = open_file("day05/input.txt")


    total_valid_updates = 0
    for update in updates:
        not_allowed = set({})
        valid = True
        for element in reversed(update):
            if element in not_allowed:
                valid = False
                break
            
            not_allowed.update(rules.get(element, []))

        if valid:
            total_valid_updates += int(update[len(update)//2])


    return total_valid_updates


def part2():
    rules, updates = open_file("day05/input.txt")
    
    total_valid_updates = 0
    for update in updates:
        valid = True
        element = len(update) - 1
        while element > 0:
            if update[element] not in rules: 
                element -= 1
                continue
            for rule_number in rules[update[element]]:
                if rule_number in update[:element]:
                    index = update[:element].index(rule_number)
                    update[element], update[index] = update[index], update[element]
                    valid = False
                    element += 1
                    break
            element -= 1
            
        if not valid:
            total_valid_updates += int(update[len(update)//2])
        
    return total_valid_updates



# print(part1())
# start_time = time.perf_counter()
# for i in range(1000):
#     part2()
print(part2())
# elapsed_time = (time.perf_counter() - start_time) * 1000
# print(f"Took {elapsed_time}ms")