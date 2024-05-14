            if zero > one:
                else:
                    one += 1
            for j in range(n):
                if grid[j][i] == 0:
                    zero += 1
            zero = 0
                for t in range(n):
                    if grid[t][i] == 0:
                        grid[t][i] = 1
                    else:
                        grid[t][i] = 0
        ans = 0
        print(grid)
        for i in range(n):
            temp = ''
[
