#funksii programirovanija(sozdajutsa s pomosju komandq def

def squares():
    x = 10
    print(x ** 2)
squares() #4tobq vqzvat funksiju nusno vvesti imono etu komandu

def squares2():
    x = 10
    print(x **2)

print(squares())
print(squares2())
#---------------------------------------------------------
lst = []
lst.append("Hello world")
#------------------------------------------------
def squares3(x):
    return x **2
result = squares3(5)
print(result)
#--------------------------------
def squares4(x):
    return x **2
y = 200
result = squares4(y)
print(result)
#-----------------------------------
def squares5(number):
    result = number ** 2
    return result
def no_argument():
    number = 25 ** 0.5
    return number
def sqrt(number):
    return number ** 0.5
def print_message(name, age, profession):
    return print(f"Hi my name is {name}, I am {age} years old. I work as a {profession}")

#print_messege("Jack Smith", "25", "Programmer")
emp_list = [("Jack Smith", 25, "Programmer"), ("Mary Gold", 18, "Teacher"), ("Bob Summers", 30, "Builder")]

for employee in emp_list:
    print_message(employee[0], employee[1],employee[2])
for x, y, z in emp_list:
    print(x, y, z)
user_name, user_age, user_profession = input("Enter name, age, profession: ").split(", ")
print_message(user_name, user_age, user_profession)
