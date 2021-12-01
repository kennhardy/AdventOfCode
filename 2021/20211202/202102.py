with open("data.txt") as file:
    lines = file.readlines()
    values = [line.rstrip() for line in lines]
values = (list(map(int, values))) # Make all values in list integers
