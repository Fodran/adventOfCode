def importData():
    f = open("../input", "r")

    data = f.read()
    
    f.close()

    return data



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
        tmp = field.split(":")
        name = tmp[0]
        #value = tmp[1]

        #if(str(value) != ""):
        fieldValidation[name] = True

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
        if(validatePassport(passport)):
            counter += 1

    print(counter)
    return 0



if __name__ == "__main__":
    main()
