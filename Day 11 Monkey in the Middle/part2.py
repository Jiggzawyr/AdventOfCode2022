class Monkey:
    def __init__(self, name=0, items=[], operation=[], test = 0, if_true = 0, if_false = 0, inspect_count = 0):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_count = inspect_count
    def __str__ (self):
        return f'Monkey({self.name},{self.items},{self.operation},{self.test},{self.if_true},{self.if_false},{self.inspect_count})'

ROUNDS = 10000 

monkeys = []

modules = []
module = 1

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]  
    for line in lines:
        l = line.split(" ")
        if l[0] == "Monkey": # name
            name = l[1][0:-1]
        if len(l) > 2 and l[2] == "Starting": # items
            cnt = 4
            items = []
            while cnt < len(l):
                items.append(int(l[cnt].replace(',', '')))
                cnt += 1
        if len(l) > 2 and l[2] == "Operation:": # operation
            cnt = 5
            operation = []
            while cnt < len(l):
                operation.append(l[cnt])
                cnt += 1
        if len(l) > 2 and l[2] == "Test:": # test
            test = int(int(l[5]))
            modules.append(int(int(l[5])))
        if len(l) > 4 and l[4] == "If" and l[5] == "true:": # if_true
            if_true = l[9]
        if len(l) > 4 and l[4] == "If" and l[5] == "false:": # if_false
            if_false = l[9]
        if l[0] == "" and len(l) == 1: # end
            m = Monkey(name,items,operation,test,if_true,if_false)
            monkeys.append(m)
    m = Monkey(name,items,operation,test,if_true,if_false)
    monkeys.append(m)

    for m in modules:
        module *= m
    print("module: ", module)

    for i in range(ROUNDS):
        print("ROUND: ", i + 1)
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.pop(0)
                monkey.inspect_count += 1
                ope_1 = int(item) if monkey.operation[0] == "old" else int(monkey.operation[0])
                ope_2 = int(item) if monkey.operation[2] == "old" else int(monkey.operation[2])
                if monkey.operation[1] == "+":
                    new_item = ope_1 + ope_2
                if monkey.operation[1] == "*":
                    new_item = ope_1 * ope_2
                new_item = new_item % module
                if new_item % monkey.test == 0:
                    new_monkey = monkey.if_true
                else:
                    new_monkey = monkey.if_false 
                for m in monkeys:
                    if m.name == new_monkey:
                        m.items.append(new_item)

    inspect_counts = []
    for monkey in monkeys:
        inspect_counts.append(monkey.inspect_count)
    inspect_counts.sort()
    print("inspect_counts: ", inspect_counts)
    monkey_business = inspect_counts.pop() * inspect_counts.pop()
    print("monkey_business:", monkey_business)