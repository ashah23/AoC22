instructions = []
filename = "Day10\\input.txt"
with open(filename) as f:
    for line in f:
        instructions.append(line.strip().split(' '))

cycle = 0
X = 1
sum = 0

for inst in instructions:
    cycle += 1
    if cycle % 40 == 20:
        this_sum = cycle * X
        # print("Cycle: " + str(cycle) + "\tX: " + str(X))
        # print(str(this_sum))
        sum += this_sum

    if inst[0] == "addx":
        ## increment the cycle
        amt = int(inst[1])
        cycle += 1
        if cycle % 40 == 20:
            this_sum = cycle * X
            # print("Cycle: " + str(cycle) + "\tX: " + str(X))
            # print(str(this_sum))
            sum += this_sum
        X += amt
        
cycle += 1
if cycle % 40 == 20:
    this_sum = cycle * X
    print(str(this_sum))
    sum += this_sum

print(str(sum))