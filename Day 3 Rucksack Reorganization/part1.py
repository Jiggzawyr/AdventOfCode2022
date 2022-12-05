def get_priority(char):
    o = ord(char)
    if o >= 65 and o <= 90: return o - 38
    if o >= 97 and o <= 122: return o - 96
    return 0

def get_common(first, second):
    res = []
    for f in first:
        if f in second: 
            res.append(f)
            break
    return res

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    sum_priorities = 0
    for line in lines:
        index = int(len(line)/2)
        first = list(line[:index])
        second = list(line[index:])
        common = get_common(first, second)
        for c in common:
            sum_priorities += get_priority(c)
    print("sum_priorities: ", sum_priorities)