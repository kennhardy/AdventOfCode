
with open("data.txt") as file:
    lines = file.readlines()
    values = [line.rstrip() for line in lines]

values = (list(map(int, values))) # Make all values in list integers

offsets = values, values[1:], values[2:] + [0] # (previous, current, next)

groupvalues = []
for offset in list(zip(*offsets)):
    group = (offset[0] + offset[1] +offset[2])
    groupvalues.append(group)
    # print(offset)
# print()
print(groupvalues)

offsetsa1 = [0] + groupvalues[:-1], groupvalues, groupvalues[1:] + [0] # (previous, current, next)

counter = 0
for value in list(zip(*offsetsa1)):

    if (int(value[1]) < int(value[2])):
        counter = counter + 1
print(counter)


# counter2 = 0
# number0 = 0
# number1 = 1
# number2 = 2
# firstnumber = values[0] + values[1] + values[2]
# for value in values:

#     if (int(value[1]) < int(value[2])):
#         counter2 = counter2 + 1
# print(firstnumber)
# print(counter2)