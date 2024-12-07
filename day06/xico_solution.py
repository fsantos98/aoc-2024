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

def part2():
    grid, curr_point = open_file("day06/input_example.txt")

    DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    directions_i = 0

    grid_width = len(grid[0])
    grid_height = len(grid)
    total = 0
    changes_dir = []
    while(curr_point[0] > -1 and curr_point[0] < grid_width and curr_point[1] > -1 and curr_point[1] < grid_height):
        
        if grid[curr_point[0]][curr_point[1]] == "#":
            changes_dir.append([curr_point[0],curr_point[1]])
            print("found: ", curr_point[0], curr_point[1])
            total += 1
            curr_point[0] -= DIRECTIONS[directions_i][0]
            curr_point[1] -= DIRECTIONS[directions_i][1]
            directions_i += 1
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
            print(f"Square is possible {changes_dir}:")
            for i in changes_dir:
                print(i)

        print("\n")
        print_grid(grid)
        print()
        input()

    return total


# print(part1())
# start_time = time.perf_counter()
# # for i in range(4000):
# #     part1()
# print(part2())
# elapsed_time = (time.perf_counter() - start_time) * 1000
# print(f"Took {elapsed_time}ms")






def getLeftRect(coords):
    print(f"Current input: {coords}")
    x = []
    for c in coords:
        x.append(c[0])
    print(f"x: {x}")


    if x[0] - x[1] > x[0] - x[2] + 1:
        return [x[0], x[1], x[2] + 1]
    else: return [x[1], x[2], x[0] - 1]

a = [[1, 7], [2, 6], [3, 1]]
print(getLeftRect(a))






