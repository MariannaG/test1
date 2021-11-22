salary = 1000
text = "Johns salary is {2}, {2}, {0}, some text {3}"
#variant 1

#print(text.format(salary)) .format konvertiruet stroku
print(text.format(salary, True, 123.23, 12312321))

#variant2

price_string = "This {product:} costs {price:.2f} eur"
print(price_string.format(product="Computer", price=1000))

#variant3

a = 1000
b = "john"
c = 2021
d = 1988
print(f"Hi, my name is {b.capitalize()}. I am {c-d} years old. My salary is {a} eur")
