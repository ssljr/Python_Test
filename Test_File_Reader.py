with open('/Users/eric/Documents/pi_digital.txt') as pi_file:
    contents = pi_file.readlines()

    pi_string = ''
    for line in contents:
        pi_string += line.rstrip()

    birthday = input("Input your birthday(yymmdd):")
    if birthday in pi_string:
        print("Your birthday appeared!")
    else:
        print("Your birthday is not appear!")


