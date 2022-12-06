sum = 0
filename = "Day3\\input.txt"
lines = []

def calc_value(letter):
    if letter.lower() == letter:
        return ord(letter) - 96
    else:
        return ord(letter) - 38

with open(filename) as f:
    for line in f:
        lines.append(line)

i = 0

while i <= len(lines) - 2:
    elf1 = set(lines[i].strip())
    elf2 = set(lines[i+1].strip())
    elf3 = set(lines[i+2].strip())

    intersect = elf1.intersection(elf2).intersection(elf3)
    letter = list(intersect)[0]
    group_sum = calc_value(letter)
    sum += group_sum
    i += 3

print (sum)