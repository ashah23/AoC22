filename = "Day6\\input.txt"

characters = []
with open(filename) as f:
    for line in f:
        characters = line

set_len = 0
index = 0
while set_len != 14:
    aset = set()
    small_list = characters[index:index+14]
    aset.update(small_list)
    set_len = len(aset)
    index += 1

print(str(index + 13))
