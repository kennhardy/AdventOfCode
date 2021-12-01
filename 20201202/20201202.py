import re

with open("data.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

list = []

for password in lines:
    patternnumberextract = re.match('\d*-\d*[:]*', password)
    patternnumbers = patternnumberextract.group(0)
    patternnumbersreplaced = patternnumbers.replace("-", ",")


    patternletterextract = re.match('(.*?):', password)
    patternletters = patternletterextract.group(1)
    patternletterscut = patternletters[-1]

    remove = patternnumbers + " " + patternletterscut + ": "
    result = re.sub(remove, "", password, 1)

    createstring = ".*" + patternletterscut + "{" + patternnumbersreplaced + "}" + ".*"
    # print(createstring)

    print(patternnumbersreplaced)
    
    if re.match(createstring, result):
        list.append(re.match(createstring, result).group(0))

# print(list)
# print(len(list))