ABC = {
    "A" : 1, # Rock
    "B" : 2, # Paper
    "C" : 3, # Scissors
}

XYZ = {
    "X" : 1, # Rock
    "Y" : 2, # Paper
    "Z" : 3, # Scissors
}

def game(me, opp):
    if me == "X" and opp == "C" or me == "Y" and opp == "A" or me == "Z" and opp == "B" : return 6 # won
    if me == "X" and opp == "A" or me == "Y" and opp == "B" or me == "Z" and opp == "C" : return 3 # draw
    if me == "X" and opp == "B" or me == "Y" and opp == "C" or me == "Z" and opp == "A" : return 0 # lost

with open("input.txt") as file:
    lines = [line.rstrip() for line in file]
    score = 0
    for line in lines:
        c = line.split()
        score += XYZ[c[1]]
        score += game(c[1],c[0])
    print(score)