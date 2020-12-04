def importData():
    f = open("input", "r")

    data = f.read()
    
    f.close()

    return data



validValues = {"byr": [str(x) for x in range(1920, 2003)], "iyr": [str(x) for x in range(2010, 2021)], "eyr": [str(x) for x in range(2020, 2031)], "hgt": [str(x) + "cm" for x in range(150, 194)] + [str(x) + "in" for x in range(59, 77)], "hcl":"0123456789abcdef", "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], "pid": "0123456789"}



def validateField(name, value):
    if name in  validValues:
        if name == "hcl":
            if value[0] == "#" and len(value) == 7:
                for char in value[1:]:
                    if not (char in validValues["hcl"]):
                        return False
                return True
            else:
                return False
        
        if name == "pid":
            if len(value) == 9:
                for char in value:
                    if not (char in validValues["pid"]):
                            return False
                return True
            return False

        if value in validValues[name]:
            return True
        else :
            return False
    return True



def validatePassport(passport):
    fieldValidation = {}
    isValid = True

    x = "byr"
    fieldValidation[x] = False
    
    x = "iyr"
    fieldValidation[x] = False

    x = "eyr"
    fieldValidation[x] = False
    
    x = "hgt"
    fieldValidation[x] = False
    
    x = "hcl"
    fieldValidation[x] = False
    
    x = "ecl"
    fieldValidation[x] = False
    
    x = "pid"
    fieldValidation[x] = False

    for field in passport:
        if field == "":
            continue
        tmp = field.split(":")
        name = tmp[0]
        value = tmp[1]
        
        fieldValidation[name] = validateField(name, value)
        if(not fieldValidation[name]):
            return False

    for field in fieldValidation:
        isValid = isValid and fieldValidation[field]
    
    return isValid



def dataToPassports(data):
    passports = []
    tmp = data.split("\n\n")
    
    for data in tmp:
        passport = data.replace("\n", " ").split(" ")
        passports.append(passport)

    return passports



def main():
    passports = dataToPassports(importData())
    counter = 0

    for passport in passports:
        #print(passport, validatePassport(passport))
        if(validatePassport(passport)):
            counter += 1
        #input("stop")

    print(counter)
    return 0



if __name__ == "__main__":
    main()
