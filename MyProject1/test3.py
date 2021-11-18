#Konvertasii

int_var = 500
float_var = 50.9

string_var_text = "Hello world"
string_var_num = "123.2"
bool_var = True

print(string_var_text + str(int_var)) #4tobq stroku s 4islov sovmestit nado vperedi zna4enie texsta(str)

print(type(int_var))

print(string_var_text + str(float_var))
print(string_var_text + str(bool_var))

print(int_var)
print(float(int_var))

print(float_var)
print(int(float_var))

print(float(string_var_num))

print(type(int(float(string_var_num))))

print(bool(int_var))
print(bool(string_var_text))

#Variantq probela
print(string_var_text + " " + str(int_var))
print(string_var_text, int_var, True, None, 10000.212525)
