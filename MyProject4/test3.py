#FIzz Buzz
#В числовом диапозоне от 0 до 100:
#если число делиться на 3 без остатка, написать число + Fizz
#если число делиться на 5 без остатка, написать число + FizzBuzz
#если число делиться на 3 и на 5 без остатка, написать число + FizzBuzz

for num in range(0, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "FizzBuzz")
    elif num % 3 == 0:
        print(num, "Fizz")
    elif num % 5 == 0:
       print(num, "Buzz")
    
#x = 15
#print(bool(x % 3))
#print(bool(x % 3 == 0))

#x = 100
#if x == 50:
    #print("X is 50")
#elif x == 10:
    #print("X is 10")
#elif x > 100:
    #print("X is greater than 100")
#elif x <= 100:
   #print("X is smaller than 100")
