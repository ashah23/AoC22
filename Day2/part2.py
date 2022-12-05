#########
# Guide:
# A = rock
# B = paper
# C = scissors
#########
# X = loss
# Y = draw
# Z = win

filename = "Day2\\input.txt"
total_score = 0

def calc_round_score(op_rps, result):
    score = 0
    ## LOSS
    if result == 'X':
        score += 0
        ## loss to rock = scissors
        if op_rps == 'A':
            score += 3
        ## loss to paper = rock
        elif op_rps == 'B':
            score += 1
        ## loss to scissors = paper
        elif op_rps == 'C':
            score += 2

    ## TIE
    if result == 'Y':
        score += 3
        ## rock 
        if op_rps == 'A':
            score += 1
        ## paper
        elif op_rps == 'B':
            score += 2
        ## scissors
        elif op_rps == 'C':
            score += 3

    ## WIN
    if result == 'Z':
        score += 6
        ## win v rock = paper
        if op_rps == 'A':
            score += 2
        ## win v paper = scissors
        elif op_rps == 'B':
            score += 3
        ## win v scissors = rock
        elif op_rps == 'C':
            score += 1
    
    return score

with open(filename) as f:
    for line in f:
        op_rps = line[0]
        result = line[2]
        round_score = calc_round_score(op_rps, result)
        total_score += round_score

print(str(total_score))
