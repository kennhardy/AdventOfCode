file1 = open("data.txt","r")

# with open("data.txt") as file:
#     while (line := file.readline().rstrip()):
#         print(line)

with open("data.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
# print(lines)

for number in lines:
    number = int(number)
    for number2 in lines:
        number2 = int(number2)
        try2 = number+number2
        if try2 == 2020:
            print("Numbers matching for answer 1: " + str(number) + " and " + str(number2))
            answer = number*number2
            print("Answer 1 is: " + str(answer))
        for number3 in lines:
            number3 = int(number3)
            try3 = number+number2+number3
            if try3 == 2020:
                print("Numbers matching for answer 2: " + str(number) + " and " + str(number2) + " and " + str(number3))
                answer = number*number2*number3
                print("Answer 2 is: " + str(answer))