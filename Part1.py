def readFile():
    file = open("InputData.txt", "r")
    return file


def checkVisibility(grid, x, y):
    value = grid[x][y]
    bleft = True
    bright = True
    bup = True
    bdown = True
    left = (x-1)
    right = (x+1)
    up = (y-1)
    down = (y+1)
    while(True):
        if (not bleft and not bright and not bup and not bdown):
            return 0
        if(right >= len(grid) or down >= len(grid) or left <= -1 or up <= -1):
            return 1
        if(value > grid[left][y] and bleft):
            left -= 1
        else:
            bleft = False
        if(value > grid[right][y] and bright):
            right += 1
        else:
            bright = False
        if(value > grid[x][up] and bup):
            up -= 1
        else:
            bup = False
        if(value > grid[x][down] and bdown):
            down += 1
        else:
            bdown = False


def main():
    file = readFile()
    grid = []
    total = 0
    for line in file:
        line = (" ".join(line)).strip()
        array = line.split(" ")
        array = [int(string) for string in array]
        grid.append(array)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            total += checkVisibility(grid, x, y)
    print(f"Total: {total}")


if (__name__ == "__main__"):
    main()
