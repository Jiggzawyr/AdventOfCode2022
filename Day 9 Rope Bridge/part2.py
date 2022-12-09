def move_tail(h,t):
    if h[0] == t[0]: # same column
        diff = h[1] - t[1]
        if diff >= 2:
            t[1] += 1
        if diff <= -2:
            t[1] -= 1
    if h[1] == t[1]: # same row
        diff = h[0] - t[0]
        if diff >= 2:
            t[0] += 1
        if diff <= -2:
            t[0] -= 1
    if h[0] != t[0] and h[1] != t[1]: # differnet row and column
        h_diff = h[0] - t[0]
        v_diff = h[1] - t[1]
        if h_diff >= 2:
            t[0] += 1
            t[1] += 1 if v_diff > 0 else -1
        if h_diff <= -2:
            t[0] -= 1
            t[1] += 1 if v_diff > 0 else -1
        h_diff = h[0] - t[0]
        v_diff = h[1] - t[1]
        if v_diff >= 2:
            t[1] += 1
            t[0] += 1 if h_diff > 0 else -1
        if v_diff <= -2:
            t[1] -= 1
            t[0] += 1 if h_diff > 0 else -1
    return t

KNOTS_COUNT = 10

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    knots = []
    for i in range(KNOTS_COUNT):
        knots.append([0,0])
    positions = set()
    positions.add((knots[KNOTS_COUNT-1][0],knots[KNOTS_COUNT-1][1]))
    for line in lines:
        dir, amount = line.split(" ")
        for i in range(int(amount)):
            # move head
            if dir == "R":
                knots[0][0] += 1
            elif dir == "D":
                knots[0][1] -= 1
            elif dir == "L":
                knots[0][0] -= 1
            elif dir == "U":
                knots[0][1] += 1
            # move tails
            for j in range(1,len(knots)):
                knots[j] = move_tail(knots[j-1],knots[j])
            positions.add((knots[KNOTS_COUNT-1][0],knots[KNOTS_COUNT-1][1]))
    print(len(positions))

