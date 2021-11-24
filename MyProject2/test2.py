#Метод трансформации строки и не только
string_sample1 = "Hello world world"
string_sample2 = "first letteR is loERcase"
string_sample3 = "extral whitespace string"
string_sample4 = "der Fluß"
simple_string = "hello"

#metod1
print("world" in string_sample1)

print("World" in string_sample1)#False tak kak u nas netu bolsoi W

#metod2
print(string_sample1.upper())#upper delaet text bolshimi bukvami

print(string_sample4.lower())#lower delaet text malenkimi bukvami
#lower ne trogaet bukvi u kotorqh net registra
#casefold bukvq konvertorujutsja v bolee ponatnqi jazqk
print(string_sample4.casefold())

#metod3
print(string_sample2.capitalize())#capitalize - sdelat pervuju bukvu boldoi, ostalnqe malenkie
user_imput = input("please enter your name: ").capitalize()
print(user_imput)

#metod4'
print(string_sample3.strip())#obrezaet probelq vo vsei stroke
#Mozet udalit tak ze opredelennqi simvol
print(string_sample3.strip(" e"))
#metod5
print(string_sample1.replace("world", "planet"))#pomenjat slovo
print(string_sample1.replace("world", "planet", 10))# koli4estvo raz skolko slov pomenjat
print(string_sample1.replace("world", "planet", 10).replace("p", "*"))
#metod6
print(string_sample1.split("w"))

a, b, c = string_sample1.split()
print(a, b, c)
#metod7
print(string_sample1.count("o", 5, 10)) #skolko bukv o vstre4aetsja v stroke
#metod8
print(string_sample1.find("world"))#naiti slovo v indexe


