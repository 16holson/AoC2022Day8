
def readFile():
    file = open("InputData.txt", "r")
    return file


def checkVisibility(grid, x, y, topView):
    value = grid[x][y]
    bleft = True
    bright = True
    bup = True
    bdown = True
    leftT = 0
    rightT = 0
    upT = 0
    downT = 0
    left = (x - 1)
    right = (x + 1)
    up = (y - 1)
    down = (y + 1)
    while (True):
        if(left <= -1):
            bleft = False
        if(up <= -1):
            bup = False
        if(right >= len(grid)):
            bright = False
        if(down >= len(grid)):
            bdown = False

        if (not bleft and not bright and not bup and not bdown):
            total = leftT * rightT * upT * downT
            if(total > topView):
                topView = total
            return topView
        if (bleft):
            if(value > grid[left][y]):
                left -= 1
            else:
                bleft = False
            leftT += 1
        if (bright):
            if(value > grid[right][y]):
                right += 1
            else:
                bright = False
            rightT += 1
        if (bup):
            if(value > grid[x][up]):
                up -= 1
            else:
                bup = False
            upT += 1
        if (bdown):
            if(value > grid[x][down]):
                down += 1
            else:
                bdown = False
            downT += 1



def main():
    file = readFile()
    grid = []
    topView = 0
    for line in file:
        line = (" ".join(line)).strip()
        array = line.split(" ")
        array = [int(string) for string in array]
        grid.append(array)
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            topView = checkVisibility(grid, x, y, topView)
    print(f"Top Visibility: {topView}")


if (__name__ == "__main__"):
    main()