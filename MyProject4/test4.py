#while бесконечный цикл повторения
#while True:
   # print("I can\"t stop")

#condition = True
#while condition:
    #print("Hello")
    #condition = False

#x = 0
#while x < 100:
    #print(x)
    #x += 1

#user_imput = input("Enter id: ")
#if len(user_imput) != 11:
   #print("Wrong number")
#else:
    #condition = False
    #print(user_imput)

distance_to_target = input("Please enter distance in meters: ")
curent_position = 0
step = 0.5

cnt = 0
while curent_position < int(distance_to_target):
    cnt += 1
    curent_position += step

print("Done")
print(f"{cnt} steps")