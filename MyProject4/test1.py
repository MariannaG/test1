#Slovar - dictionary

x = {}
print(type(x))

x = 5
sample_lst = ["one", "two", "three"]

student = {"name":"John", "age": 30, "courses": ["Math", "Biology", "Art"], "none_type": None,
           1: "int_key", 0.2: "float_key", x: "variable", "var_key": x, True: "Hello world",
           False: "Hello world"}
print(student["name"])
print(student["var_key"])
print(student.get("job")) # tak kak net takogo klju4a, no vqzqvaet None
print(student.get("courses")[1])
print(student["courses"][1])
print(student.get("job", [1, 2, 3]))

student["age"] = 28
student["phone"] = "555-555-5555"
print(student)

student.update({"name": "Jack", "age": 25, "phone": "555-555-5555"}) # 4tobi pomenjat ili dobavit novqe zna4enija
print(student)

#del student["age"] #v slovare 4tobq udalit 4to to metod remove ne rabotaet, tolko del
#print(student)

#age = student.pop("age")
#print(student)
#print(age)

print(len(student))

print(student.keys()) #pere4isljaet vse klju4i

print(student.values()) #pere4isljaet vse zna4enija

print(list(student.items()))