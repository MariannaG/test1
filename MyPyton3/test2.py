id_code = input("Please enter ID: ")

if len(id_code) == 11:
    print("Id code is correct")
elif len(id_code) > 11:
    print("ID_code is too long")
else:
    print("ID code us too short")




