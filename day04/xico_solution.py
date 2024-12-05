import time

def open_file(file):
    grid = []
    with open(file) as f:
        for line in f:
            grid.append(line.strip())
    return grid

def part1():
    grid = open_file("day04/input.txt")
    
    total_found = 0
    directions = [[-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0]]
    gridL,lineL = len(grid) - 1, len(grid[0]) - 1

    for line in range(len(grid)):
        for char in range(len(grid[line])):
            if grid[line][char] != "X": continue
                
            for dx, dy in directions:
                limit_line = line + dx * 3
                limit_char = char + dy * 3
                
                if limit_line > gridL or limit_char > lineL or limit_line < 0 or limit_char < 0:
                    continue
                
                if (
                    grid[line + dx * 1][char + dy * 1] == "M" and
                    grid[line + dx * 2][char + dy * 2] == "A" and
                    grid[limit_line][limit_char] == "S"
                ): total_found += 1
                    
                  
    return total_found

def part2():
    grid = open_file("day04/input.txt")

    start_time = time.perf_counter()

    total_found = 0
    directions = [[-1,1], [1,1], [1,-1], [-1,-1]]
    gridL,lineL = len(grid) - 1, len(grid[0]) - 1

    for line in range(len(grid)):
        for char in range(len(grid[line])):
            if grid[line][char] != "A": continue
                
            results = []
            for dx, dy in directions:
                line_x = line + dx
                char_y = char + dy

                if line_x > gridL or char_y > lineL or line_x < 0 or char_y < 0:
                    continue
                
                if grid[line_x][char_y] != "M" and grid[line_x][char_y] != "S":
                    break

                results.append(grid[line_x][char_y])
            
            if len(results) == 4:
                if results[0] != results[2] and results[1] != results[3]:
                    total_found += 1

    elapsed_time = (time.perf_counter() - start_time) * 1000
    print(f"took {elapsed_time}ms")

    return total_found

# print(part1())
print(part2())
