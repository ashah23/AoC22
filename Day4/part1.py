filename = "Day4\\input.txt"
sum = 0

with open(filename) as f:
    for line in f:
        ranges = (line.strip().split(','))
        first = ranges[0].split('-')
        second = ranges[1].split('-')
        low1 = int(first[0])
        hi1 = int(first[1])
        low2 = int(second[0])
        hi2 = int(second[1])
        
        if low1 >= low2 and hi1 <= hi2:
            sum += 1
            print(line.strip())
        elif low2 >= low1 and hi2 <= hi1:
            sum += 1
            print(line.strip())
print(sum)


