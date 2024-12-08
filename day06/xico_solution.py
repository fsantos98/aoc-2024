import time
import pprint
pp = pprint.PrettyPrinter(depth=4)
from collections import defaultdict

def open_file(file):
    start_point, grid = [], []

    with open(file) as f:
        for x, line in enumerate(f):
            row = list(line.strip())
            for y, char in enumerate(row):
                if char == "^": 
                    start_point = [x, y]
            grid.append(row)

    return grid, start_point

def print_grid(grid):
    for l in grid:
        for c in l:
            print(c, end="")
        print("")

def part1():
    grid, curr_point = open_file("day06/input.txt")

    DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    directions_i = 0

    grid_width = len(grid[0])
    grid_height = len(grid)
    total = 0
    while(curr_point[0] > -1 and curr_point[0] < grid_width and curr_point[1] > -1 and curr_point[1] < grid_height):
        
        if grid[curr_point[0]][curr_point[1]] == "#":
            curr_point[0] -= DIRECTIONS[directions_i][0]
            curr_point[1] -= DIRECTIONS[directions_i][1]
            directions_i += 1
            if directions_i > 3:
                directions_i = 0
        else:
            if grid[curr_point[0]][curr_point[1]] != "X":
                total += 1
            grid[curr_point[0]][curr_point[1]] = "X"

        next_point_x = curr_point[0] + DIRECTIONS[directions_i][0]
        next_point_y = curr_point[1] + DIRECTIONS[directions_i][1]


        curr_point = [next_point_x, next_point_y]

    return total

def getNextCornerRect(coords):
    print(f"Current input: {coords}")
    coord_1 = coords[0]
    coord_2 = coords[1]
    coord_3 = coords[2]
    
    dist_x = coord_1[0] + coord_3[0] - coord_2[0]
    dist_y = coord_1[1] + coord_3[1] - coord_2[1]

    return [dist_x, dist_y]

def part2():
    grid, curr_point = open_file("day06/input_example.txt")

    DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    directions_i = 0

    grid_width = len(grid[0])
    grid_height = len(grid)
    total = 0
    changes_dir = []
    objective = [-1,-1, -1]
    while(curr_point[0] > -1 and curr_point[0] < grid_width and curr_point[1] > -1 and curr_point[1] < grid_height):
        print(f"Objective: {objective}")
        print(f"Curr: {curr_point}")
        print(f"Direction: {directions_i}")
        if objective[0] == curr_point[0] and objective[1] == curr_point[1] and directions_i:
            print(f"we got there: {curr_point}")
            total += 1

        else:
            print("not here")
        print(f"total: {total}")


        if grid[curr_point[0]][curr_point[1]] == "#":
            
            changes_dir.append([curr_point[0],curr_point[1]])
            print("found: ", curr_point[0], curr_point[1])
            curr_point[0] -= DIRECTIONS[directions_i][0]
            curr_point[1] -= DIRECTIONS[directions_i][1]
            directions_i += 1
            objective = [-1,-1,-1]
            if directions_i > 3:
                directions_i = 0
        else:
            if grid[curr_point[0]][curr_point[1]] != "X":
                total += 0
            grid[curr_point[0]][curr_point[1]] = "X"

        next_point_x = curr_point[0] + DIRECTIONS[directions_i][0]
        next_point_y = curr_point[1] + DIRECTIONS[directions_i][1]


        curr_point = [next_point_x, next_point_y]


        if len(changes_dir) > 2:
            a = getNextCornerRect(changes_dir[-3:])
            a.append(directions_i)
            objective = a

            print(f"Trying to check this corner: {objective}")
        print("\n")
        print_grid(grid)
        print()
        input()

    return total


# print(part1())
# start_time = time.perf_counter()
# # for i in range(4000):
# #     part1()
print(part2())
# elapsed_time = (time.perf_counter() - start_time) * 1000
# print(f"Took {elapsed_time}ms")






