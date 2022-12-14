x_min = 500
x_max = 500
y_max = 0

width = 0
height = 0
map = []

SAND = [0,500]

def get_frame(lines):
    global x_min, x_max, y_max
    for line in lines:
        coords = line.split("->")
        for coord in coords:
            x,y = [int(coord) for coord in coord.strip().split(',')]  
            if int(x) < x_min: x_min = int(x)
            if int(x) > x_max: x_max = int(x)
            if int(y) > y_max: y_max = int(y)
    print("x_min: ", x_min)
    print("x_max: ", x_max)
    print("y_max: ", y_max)

def init_map():
    global map
    print("=================init_map=================")
    for h in range(height):
        row = []
        for w in range(width):
            row.append('.')
        map.append(row)

def draw_map():
    global map
    print("=================draw_map=================")
    for row in map:
        print(''.join(row))

def fill_map(lines):
    global map, x_min
    print("=================fill_map=================")
    for line in lines:
        print("line: ", line)
        coords = line.split("->")
        x_prev, y_prev = [int(coord) for coord in coords[0].strip().split(',')] 
        for i in range(1,len(coords)):
            # print("x_prev: ", x_prev)
            # print("y_prev: ", y_prev)
            x_curr, y_curr = [int(coord) for coord in coords[i].strip().split(',')] 
            # print("x_curr: ", x_curr)
            # print("y_curr: ", y_curr)
            if x_prev == x_curr: # vertical line
                print("vertical line")
                step = 1 if y_prev < y_curr else -1
                for y_iter in range(y_prev, y_curr + step, step):
                    map[y_iter][x_prev - x_min] = '#'
            if y_prev == y_curr: # horizontal line
                print("horizontal line")
                step = 1 if x_prev < x_curr else -1
                for x_iter in range(x_prev, x_curr + step, step):
                    map[y_prev][x_iter - x_min] = '#'
            x_prev = x_curr
            y_prev = y_curr
    map[SAND[0]][SAND[1] - x_min] = '+'

def fall_sand():
    global map, x_min, x_max
    print("=================fall_sand=================")
    cnt = 0
    end = False
    while not end:
        falling = True
        sand_x = SAND[1]
        sand_y = SAND[0]
        while falling:
            #print("sand_x: ", sand_x)
            #print("sand_y: ", sand_y)
            #print(map[sand_x-x_min][sand_y+1])
            if map[sand_y+1][sand_x-x_min] == '.':
                #print("FALLING DOWN")
                sand_y += 1
            elif sand_x-1 >= x_min and map[sand_y+1][sand_x-1-x_min] == '.':
                #print("FALLING DOWN LEFT")
                sand_x -= 1
                sand_y += 1
            elif sand_x+1 <= x_max and map[sand_y+1][sand_x+1-x_min] == '.':
                #print("FALLING DOWN RIGHT")
                sand_x += 1
                sand_y += 1
            elif sand_x - 1 < x_min or sand_x + 1 > x_max:
                #print("FALLING OUT OF FRAME 1")
                end = True
                break
            else:               
                falling = False
                map[sand_y][sand_x-x_min] = '0'
                print("cnt: ", cnt)
                #draw_map()
            if sand_y >= y_max:
                #print("FALLING OUT OF FRAME 2")
                end = True
                break
        if not end: cnt += 1
    print("cnt: ", cnt)


with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    get_frame(lines)
    width = x_max - x_min + 1
    height = y_max + 1
    init_map()
    fill_map(lines)
    draw_map()
    fall_sand()