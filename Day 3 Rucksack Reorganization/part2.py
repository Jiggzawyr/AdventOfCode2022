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

def get_common_in_three(first, second, third):
    res = []
    for f in first:
        if f in second: 
            if f in third: return f
    return ''

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    sum_priorities = 0
    cnt = 0
    while(cnt < len(lines)):
        first = lines[cnt]
        second = lines[cnt+1]
        third = lines[cnt+2]
        common = get_common_in_three(first,second,third)
        sum_priorities += get_priority(common)
        cnt += 3
    print("sum_priorities: ", sum_priorities)