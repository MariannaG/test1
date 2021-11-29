#Konstrukcia IF

x = 5
print(x)
print(x == 5)
print(x == 6)

print(x != 6) #x ne raven 6 i eto True

x = 100

if x != 100:
    print("x is not equal to 100")
elif x == 100:
    print("X is egual to 100")
elif x > 50:
    print("X is greater than 50")

else:
    print(x)
