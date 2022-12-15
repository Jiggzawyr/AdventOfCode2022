import re

X_MIN = 0
X_MAX = 4000000
Y_MIN = 0
y_MAX = 4000000

def scan(lines, y_target):  
    global map, x_min, x_max
    empty = []
    for line in lines: 
        m = re.match(r'Sensor at x=(?P<sx>.*), y=(?P<sy>.*): closest beacon is at x=(?P<bx>.*), y=(?P<by>.*)', line)
        sx = int(m.group('sx'))
        sy = int(m.group('sy'))
        bx = int(m.group('bx'))
        by = int(m.group('by'))
        distance = abs(sx - bx) + abs(sy - by)
        distance_on_target = distance - abs(sy - y_target)
        cnt = 0
        if distance_on_target >= 0:
            left = sx - distance_on_target if sx - distance_on_target >= X_MIN else X_MIN
            right = sx + distance_on_target if sx + distance_on_target <= X_MAX else X_MAX
            empty.append((left, right))
    empty.sort()
    limit = 0
    for left, right in empty:
        if left > limit + 1:
            print("FOUND: ", limit + 1, y_target)
            frequency = (limit + 1) * X_MAX + y_target
            print("frequency: ", frequency)
            return True
        else: 
            limit = max(limit, right)
    return False

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    for y_target in range(Y_MIN, y_MAX + 1):
        # print("y_target: ", y_target)
        if y_target % 50000 == 0: print("y_target: ", y_target)
        if scan(lines, y_target): break

