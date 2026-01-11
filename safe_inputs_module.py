"""
    Module Purpose: force users into entering a correct datatype input.
"""

def get_integer():
    usr_in = 0
    while True:
        try:
            usr_in = int(input("Enter value:"))
        except ValueError:
            print("Please Enter only an integer value")
        else:
            return usr_in

def get_float():
    usr_in = 0.0
    while True:
        try:
            usr_in = float(input("Enter value:"))
        except ValueError:
            print("Please Enter only an decimal value")
        else:
            return usr_in

def get_bool():
    usr_in = False
    while True:
        try:
            usr_in = bool(input("Enter state ( true or false ):"))
        except ValueError:
            print("Please Enter only an boolean state only")
        else:
            return usr_in
