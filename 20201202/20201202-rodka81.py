import re
with open("data.txt") as f:
    print(
        sum(
            int(min_freq) <= password.count(letter) <= int(max_freq)
            for min_freq, max_freq, letter, password in re.findall(
                r"(\d+)-(\d+)\s+(\w+):\s+(\w+)", f.read()
            )
        )
    )