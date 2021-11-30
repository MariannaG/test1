#for letter in "Python":
#    if letter == "h":
#        print("Found it")
#        continue
#    print(f"Current letter - {letter}")
#----------------------------------------------------------------
#----------------------------------------------------------------
condition = True
while condition:
    try:
        user_input = input("Please enter ID code: ")
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning
    except ValueError:
        print("Your code is not numeric.")
        continue
    except UserWarning:
        if len(user_input) > 11:
            print("Id code is too long")
        elif len(user_input) < 11:
            print("Id code is too short")
            continue
    else:
        break
print(user_input)
    #finally: #Vqpolnjaetsja ne smotrja ni na 4to
       # print("Good Bye")
    #MENU
condition = True
while condition:
    user_choice = input("Please choose:\n1:Get data ID\n2.Validate\n0.Exit ")
    if user_choice == "1":
        pass
    elif user_choice == "2":
        id_code = user_input

        chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
        chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

        cnt = 0
        result = 0
        for num in chk1:
            result += num * int(id_code[cnt])
            cnt += 1
        check_num = result % 11

        if int(id_code[-1]) == check_num:
            print(f"Your id is {id_code}")
            print("Id is valid")
        elif check_num == 10:
            cnt = 0
            result = 0
            for num in chk2:
                result += num * int(id_code[cnt])
                cnt += 1
            check_num = result % 11
            if check_num == int(id_code[-1]):
                print(f"Your id is {id_code}")
                print("Id is valid")
            else:
                print("Your ID is invalid.")
        else:
            print("Your ID is invalid.")
    elif user_choice == "0":
        break
    else:
        print("Choice is out of range")


