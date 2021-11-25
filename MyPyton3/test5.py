#TUPLE
courses = ("Math", "Physics", "History", "Programming", "Literature")
numbers = [4, 5, 23, 1, 9, 84]

#print(courses.count(5))

#tuple1 = tuple()
#tuple2 = (1)
#print(type(tuple1))
#print(type(tuple2))

#SET nuzen dlja togo stobq izbavitsja ot dublikata
#set1 = set()
#print(type(set1))

#set1 = {1, 4, 2, 5, 5, 5, 5}# set ne dopuskaet dublizei
#print(set1)

#set1 = set(courses)
#print(set1.pop())

set1 = {"Art", "English", "Biology", "Physics"}
set2 = {"Programming", "Biology", "Art", "Math"}

#print(set1.intersection(set2)) # nahodit obsee
#print(set1.difference(set2)) #4em otli4aetsja(4to unikalnogo v set1 po sravneniju s set2

#print(set1.union(set2)) # delaet spisok setov obsim

#set1.add("Russia")#dobavit slovo
#print(set1)

set1.update(set2)