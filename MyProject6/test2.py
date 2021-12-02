def double(x):
    y = x * 2
    #return f"Double from {x} is {y}"
    return y
def triple(x):
    if x % 2 == 0:
        print(f"{x} is even")
        return x *3

number = 6
print(triple(number))
#-------------------------

def print_message(emp_info):
    return f"Hello {emp_info[0]} {emp_info[1]}. You are {emp_info[2]} years old"
emp_list = ("Jack", "Smith", 25, 2500, "555-555-5555", "jack.smith@example.com")

def fizz_buzz(start_num, end_num):
    for num in range(0, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f'{num} FizzBuzz')
        elif num % 3 == 0:
            print(f'{num} Fizz')
        elif num % 5 == 0:
            print(f'{num} Buzz')
fizz_buzz(50,1000)



