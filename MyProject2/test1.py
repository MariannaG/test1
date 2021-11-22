#Stroka
# ß - сдвоенная буква с


string_sample1 = "Hello world world"
string_sample2 = "first letteR is loERcase"
string_sample3 = " extral whitespace string"
string_sample4 = "der Fluß"
simple_string = "hello"

print(len(string_sample1))
print(len("123456789"))
#esli nuzen index s 1-5 to pisem s 1-4.Ots4et idjot s 0.0 eto pervaja bukva

print(string_sample1[0])
print(simple_string[1:10])
print(string_sample1[1:10])

#[start:stop_index:step]
print(string_sample1[6:16:2]) #berem kazdqi 2 sag
#Если я хочу указать шаг, то надо два раза ::

#        "-5-4-3-2-1"C право на лево можно писать
print(string_sample1[::-1])

print(string_sample1[6:11])

sliced_string = (string_sample1[6:11])#srezq slov
print(sliced_string)
print("hello world"[2:10])








