
def calc_value(letter):
    if letter.lower() == letter:
        return ord(letter) - 96
    else:
        return ord(letter) - 38

sum = 0
filename = "Day3\\input.txt"
with open(filename) as f:
    for line in f:
        if len(line) > 2:
            mid = int(len(line) / 2 - .5)
            first_set = set(line[:mid])
            second_set = set(line[mid:])
            intersection = first_set.intersection(second_set)
            letter = list(intersection)[0]
            this_sum = calc_value(letter)
            sum += this_sum
print (sum)