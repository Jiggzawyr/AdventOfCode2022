import re

Y_TARGET = 2000000

empty = set()
beacons = set()

def scan(lines):  
    for line in lines: 
        # print("line: ", line)
        m = re.match(r'Sensor at x=(?P<sx>.*), y=(?P<sy>.*): closest beacon is at x=(?P<bx>.*), y=(?P<by>.*)', line)
        sx = int(m.group('sx'))
        sy = int(m.group('sy'))
        bx = int(m.group('bx'))
        by = int(m.group('by'))
        distance = abs(sx - bx) + abs(sy - by)
        # print("distance: ", distance)
        distance_on_target = distance - abs(sy - Y_TARGET)
        # print("distance_on_target: ", distance_on_target)
        cnt = 0
        while distance_on_target >= 0:
            empty.add(sx - cnt)
            empty.add(sx + cnt)
            distance_on_target -= 1
            cnt += 1
        if by == Y_TARGET: beacons.add(bx)

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    scan(lines)
    blocked_positions = len(empty) - len(beacons)
    print("blocked_positions: ", blocked_positions)