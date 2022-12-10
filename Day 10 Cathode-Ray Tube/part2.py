cycle = 0
x = 1

crt = []

def draw():
    global cycle
    global x
    global crt
    # print("cycle: ", cycle)
    # print("x: ", x)
    pos = (cycle - 1) % 40
    if (pos) == (x - 1) or (pos) == x or (pos) == (x + 1):
        crt.append("#")
    else:
        crt.append(".")
    # print("crt: ", crt)

def print_crt():
    global crt
    row = []
    while(len(crt)>0):
        for i in range(40):
            row.append(crt.pop(0))
            if(len(crt)==0): break
        print("".join(row))
        row = []

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]  
    for line in lines:
        # print("==========================")
        # print("line: ", line)
        if line[:4] == "noop":
            cycle += 1
            draw()
        if line[:4] == "addx":
            amount = int(line.split(" ")[1])
            cycle += 1
            draw()
            cycle += 1
            draw()
            x += amount
    print_crt()