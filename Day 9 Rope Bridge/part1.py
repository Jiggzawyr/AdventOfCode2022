with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    h = [0, 0]
    t = [0, 0]
    positions = set()
    for line in lines:
        dir, amount = line.split(" ")
        print("===============")
        for i in range(int(amount)):
            # move head
            if dir == "R":
                h[0] += 1
            elif dir == "D":
                h[1] -= 1
            elif dir == "L":
                h[0] -= 1
            elif dir == "U":
                h[1] += 1
            # move tail
            if h[0] == t[0]: # same column
                print("SAME COLUMN")
                diff = h[1] - t[1]
                if diff >= 2:
                    t[1] += 1
                if diff <= -2:
                    t[1] -= 1
            if h[1] == t[1]: # same row
                print("SAME ROW")
                diff = h[0] - t[0]
                if diff >= 2:
                    t[0] += 1
                if diff <= -2:
                    t[0] -= 1
            if h[0] != t[0] and h[1] != t[1]: # differnet row and column
                print("DIFFERENT ROW AND COLUMN")
                h_diff = h[0] - t[0]
                v_diff = h[1] - t[1]
                if h_diff >= 2:
                    t[0] += 1
                    t[1] += 1 if v_diff > 0 else -1
                if h_diff <= -2:
                    t[0] -= 1
                    t[1] += 1 if v_diff > 0 else -1
                if v_diff >= 2:
                    t[1] += 1
                    t[0] += 1 if h_diff > 0 else -1
                if v_diff <= -2:
                    t[1] -= 1
                    t[0] += 1 if h_diff > 0 else -1
            positions.add((t[0],t[1]))
    print(len(positions))

