import string

def byr(x):
    return len(x[4:]) == 4 and x[4:].isdigit() and int(x[4:]) >= 1920 and int(x[4:]) <= 2002

def iyr(x):
    return len(x[4:]) == 4 and x[4:].isdigit() and int(x[4:]) >= 2010 and int(x[4:]) <= 2020

def eyr(x):
    return len(x[4:]) == 4 and x[4:].isdigit() and int(x[4:]) >= 2020 and int(x[4:]) <= 2030

def hgt(x):
    if "cm" in x:
        return x[4:-2].isdigit() and int(x[4:-2]) >= 150 and int(x[4:-2]) <= 193
    elif "in" in x:
        return x[4:-2].isdigit() and int(x[4:-2]) >= 59 and int(x[4:-2]) <= 76
    else:
        return 0

def ecl(x):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return any(i in x for i in colors) and len(x[4:]) == 3

def hcl(x):
    return x[4] == '#' and len(x[5:]) == 6 and all(i in string.hexdigits for i in x[5:])

def pid(x):
    return len(x[4:]) == 9 and x[4:].isdigit()

def check(passport):
    passport = passport[:-1]
    arr = passport.split(' ')


    keywords = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

    if not all(x in passport for x in keywords):
        return False

    cnt = 0
    for x in arr:
        if("byr:" in x): cnt = cnt + byr(x)
        elif("iyr:" in x): cnt = cnt + iyr(x)
        elif("eyr:" in x): cnt = cnt + eyr(x)
        elif("hgt:" in x): cnt = cnt + hgt(x)
        elif("hcl:" in x): cnt = cnt + hcl(x)
        elif("ecl:" in x): cnt = cnt + ecl(x)
        elif("pid:" in x): cnt = cnt + pid(x)
    if cnt == 7:
        return True
    return False

file = open("input.txt", "r")

lines = file.readlines()
valid = 0

passport = ""
for i in range(len(lines)):
    if(lines[i] != "\n"):
        passport = passport + lines[i][:-1] + " "
    else:
        if check(passport):
            valid = valid + 1
        passport = ""

if check(passport):
    valid = valid+1

print(valid)