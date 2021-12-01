with open("data.txt") as file:
    lines = file.readlines()
    values = [line.rstrip() for line in lines]

values = (list(map(int, values))) # Make all values in list integers

offsetsa1 = [0] + values[:-1], values, values[1:] + [0] # (previous, current, next)

counter = 0
for value in list(zip(*offsetsa1)):

    if (int(value[1]) < int(value[2])):
        counter = counter + 1
print(counter)

