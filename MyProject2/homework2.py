# Write a code to return "Hero" from given string
example_string1 = "Hello bro"
print(example_string1.replace("b" ,"he".capitalize()))

# Write a code to return "Jack is my name"
example_string2 = "jack Is My NAME"
print(example_string2.capitalize())

# Write a code to return "Get rid of stars please"
example_string3 = "*Get rid of stars please*"
print(example_string3.strip("*"))

# Write a code to return "Hello my name is Jack"
example_string4 = "hello my name is jack"


# Write a code to return formatted string "Hello, my name is Jack"
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print((var2.capitalize()) + " " + (var3.lower()) +" "+ (var1.capitalize()).capitalize())


# Write a code to return byte_string text value
byte_string = b"\316\273"
print(byte_string.decode('utf-16')) # не ясно

# Write a code to return True if cost is greater than 500$
example_string5 = "It cost me 1000.00$"
print(example_string5.replace("1000", "500"))