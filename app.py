import os
os.system("clear")

my_name =  "Machiko Kimura" 
my_number = 10

my_name = 54

# print(my_name)


# Arrays
# List (mutable, indexed, iterable)


my_list = list()
my_list = []
my_list = [1,2,3,5,6]


my_list[2] = 'hello'

print(my_list[2])
print(my_list[2:4])


#my_list.remove[3]





if 4 in my_list:
    print('4 is in the list')
else:
    print('4 is not in the list')


print(my_list)

for fish in my_list:
    print(fish)


print(len(my_list))



# Tuple (It's not mutable - nothing added or deleted)
# memory management

my_tuple = tuple()

my_tuple = ()

my_tuple = (1,2,3)


# card game card variable'
card1 = (3, "hearts")
card2 = (4, "spades")



if card1[0] < card2[0]:
    print('win!')



print(my_tuple[1:3])

my_new_tuple = my_tuple + (4,5,6)

print(my_new_tuple)

a, b, c = my_tuple

print(a,b,c)


print(len(my_tuple))

if 3 in my_tuple:
    print('yey')

#my_tuple[1] = 6

# Sets mutable, unordered collection iterable

set1 = {1, 2, 3}
set2 = {3, 4, 5}



set1.add(4)

set1.remove(1)


if 2 in set1:
    print("yey")

print(set1)

for item in set1:
    print(item)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))


#Dictionaries keys not mutable, values mutable 

student = {
    "name"   : "Mark",
    "age"    : 21,
    "gender" : "male"
}

print(student['name'])


student['age'] = 61


print(student['age'])


student['grade'] = 90

print(student)



del student["name"]


print(student)


for key, val in student.items():
    print(key, val)


if "name" in student:
    print("yey")

print(len(student)) #key value pairs









