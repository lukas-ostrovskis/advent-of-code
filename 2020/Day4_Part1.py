def check(passport):
    keywords = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

    return all(x in passport for x in keywords)

file = open("input.txt", "r")

lines = file.readlines()
valid = 0

passport = ""
for i in range(len(lines)):
    if(lines[i] != "\n"):
        passport = passport + lines[i]
    else:
        if check(passport):
            valid = valid + 1
        passport = ""

if check(passport):
    valid = valid+1

print(valid)