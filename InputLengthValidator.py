#task 1
def check_name_length():

    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    if len(first_name) < 2:
        print("Error: Please enter a first name at least 2 characters long.")
    elif len(last_name) < 2:
        print("Error: Please enter a last name at least 2 characters long.")
    else:
        print(f"Hello {first_name} {last_name} your inputs are valid!")

check_name_length()
