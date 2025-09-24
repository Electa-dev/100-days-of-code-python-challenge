def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Enter valid input"
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

output = is_leap_year(int(input("Enter year here: ")))
print(f"This is {output}")
