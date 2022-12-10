signal_sum = 0
cycle = 1
x = 1

def check_signal():
    global signal_sum
    global cycle
    global x
    if (cycle - 20) % 40 == 0:
        print("x: ", x)
        signal_sum += x * cycle


with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]  
    for line in lines:
        # print("==========================")
        # print("line: ", line)
        if line[:4] == "noop":
            cycle += 1
            check_signal()
        if line[:4] == "addx":
            amount = int(line.split(" ")[1])
            cycle += 1
            check_signal()
            cycle += 1
            x += amount
            check_signal()
        # print("cycle: ", cycle)
        # print("x: ", x)
    print("signal_sum: ", signal_sum)
