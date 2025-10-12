                            #Data Types and Structures Questions
# 1.What are data structures, and why are they important?
# Data structure is important because it helps to organize and store data in a correct way, so that it can be accessed and modified easily, and why they are important because they provide efficient ways to manage and manipulate data.

# 2.Explain the difference between mutable and immutable data types with examples?
# Mutable data types can be changed after they are created, such as lists and dictionaries. Immutable data types cannot be changed after they are created, such as strings and tuples.

# 3.What are the main differences between lists and tuples in Python?
# Lists are mutable, ordered collections that allow duplicate elements, while tuples are immutable, ordered collections that also allow duplicates.

# 4.Describe how dictionaries store data.
# Dictionaries store data in key-value pairs, where each key is unique and maps to a specific value. They are unordered and mutable, allowing for efficient data retrieval based on keys.

# 5.Why might you use a set instead of a list in Python?
# Sets are used instead of lists when you need to store unique elements and perform operations like union, intersection, and difference efficiently.

# 6.What is a string in Python, and how is it different from a list?
# A string in Python is a sequence of characters enclosed in quotes. It is different from a list in that strings are immutable, meaning they cannot be changed after creation, while lists are mutable and can be modified.

# 7.How do tuples ensure data integrity in Python?
# Tuples ensure data integrity by being immutable, which means once they are created, their elements cannot be changed, added, or removed. This makes tuples a reliable choice for storing fixed collections of items.

# 8.What is a hash table, and how does it relate to dictionaries in Python?
# A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values. In Python, dictionaries are implemented as hash tables, allowing for fast lookups, insertions, and deletions.

# 9.Can lists contain different data types in Python?
# Yes, lists in Python can contain elements of different data types, including integers, strings, and even other lists.

# 10.Explain why strings are immutable in Python.
# Strings are immutable in Python because once they are created, their contents cannot be changed. This is by design, as it allows for more efficient memory usage and performance optimizations.

# 11.What advantages do dictionaries offer over lists for certain tasks?
# Dictionaries offer faster lookups, insertions, and deletions compared to lists, especially when dealing with large datasets. They allow for efficient data retrieval based on unique keys.

# 12.How do sets handle duplicate values in Python?
# Sets automatically remove duplicate values, ensuring that all elements are unique. If you try to add a duplicate element to a set, it will not be added.

# 13.Describe a scenario where using a tuple would be preferable over a list.
# Using a tuple would be preferable when you need to store a collection of items that should not change, such as the days of the week or the RGB values of a color.

# 14.How does the “in” keyword work differently for lists and dictionaries?
# The “in” keyword checks for the presence of a value in a list, while in a dictionary, it checks for the presence of a key.

# 15.Can you modify the elements of a tuple? Explain why or why not.
# No, you cannot modify the elements of a tuple because tuples are immutable. Once a tuple is created, its contents cannot be changed, which ensures data integrity.

# 16.What is a nested dictionary, and give an example of its use case.
# A nested dictionary is a dictionary that contains another dictionary as a value. This is useful for representing complex data structures, such as a contact list where each contact has multiple attributes.
# Example:
# contacts = {
#     "John": {"phone": "123-456-7890", "email": "john@example.com"},
#     "Jane": {"phone": "987-654-3210", "email": "jane@example.com"}
# }

# 17.Describe the time complexity of accessing elements in a dictionary.
# The time complexity of accessing elements in a dictionary is O(1) on average, due to the underlying hash table implementation. This means that lookups, insertions, and deletions can be performed in constant time.

# 18.In what situations are lists preferred over dictionaries?
# Lists are preferred over dictionaries when the order of elements is important, or when you need to store multiple values without the need for key-value pairs. They are also more memory-efficient for small collections of items.

# 19.Why are dictionaries considered unordered, and how does that affect data retrieval?
# Dictionaries are considered unordered because they do not maintain the order of elements based on insertion. This means that when you iterate over a dictionary, the order of keys may not be the same as the order in which they were added. However, starting from Python 3.7, dictionaries maintain insertion order as an implementation detail, but this should not be relied upon for program logic. Data retrieval is still efficient due to the hash table structure, but the lack of guaranteed order can affect scenarios where order matters.

# 20.Explain the difference between a list and a dictionary in terms of data retrieval.
# The main difference between a list and a dictionary in terms of data retrieval is that lists use integer indices to access elements based on their position, while dictionaries use unique keys to access values. This allows for faster lookups in dictionaries when you know the key, whereas lists require searching through the elements to find a specific value.



                                                            # PRACTICAL QUESTIONS

#1 write a code to create a string with your name and print it .
string="harsh"
print(string)

#2 write a code to find a length of the string"hello world".
str1="Hello world"
a=len(str1)
print(a)

#3 write a code to slice 1st 3 character from string "Python Programming".
str2="Python Programming"
print(str2[0:3])

#4 write a program to convert a string "hello"to uppercase.
str3="hello"
str3.upper()

#5 write a code to replace the word "apple" with "orange" in a string 'I like apple'.
str4='I like apple'
str4.replace("apple","orange")

#6 write a code to create a list with numbers 1 to 5 amd print it.
list=[1,2,3,4,5]
print(list)

#7 write a code to append the no 10 in the list[1,2,3,4].
list2=[1,2,3,4]
list2.append(10)
print(list2)

#8 write a code to remove the the no 3 from the list[1,2,3,4,5].
list3=[1,2,3,4,5]
list3.remove(3)
print(list3)

#9 write a code access the 2nd element in the list['a','b','c','d'].
list4=['a','b','c','d']
print(list4[1])

#10 write a code to reverse the list[10,20,30,40,50].
list5=[10,20,30,40,50]
print(list5[::-1])

#11 writ e a code to create a tuple with elements 100,200,300 and pint it.
tuple=(100,200,300)
type(tuple)
print(tuple)

#12 write a code to access the 2 to last element of the tuple(red,green,blue,yellow).
tuple1=('red','green','blue','yellow')
print(tuple1[1: ])

#13 write a code to find the minimum no in the tuple(10,20,5,15).
tuple2=(10,20,5,15)
print(min(tuple2))

#14 write a code to find an index of an element'cat' in the tuple .
tuple3=('dog','cat','rabbit')
a=tuple3.index('cat')
print(a)

#15 write a code to create a tuple containing three different fruits and check if 'kiwi'is in it.
tuple4=('mango','kiwi','orange')
'kiwi' in tuple4

#16 write a code to create a set with the elements a,b,c and print it.
set={'a','b','c'}
print(set)

#17 write a code all element from the set{1,2,3,4,5}.
set={1,2,3,4,5}
s=set.clear
print(s)

#18 write a code to remove the element 4 from the set{1,2,3,4}.
set1={1,2,3,4}
set1.remove(4)
print(set1)

#19 write a code to find the union of a two sets{1,2,3} and {3,4,5}.
s1={1,2,3}
s2={3,4,5}
s=s1|s2
print(s)

#20 write a code to find the intersection of a two sets{1,2,3} and {2,3,4}.
s1={1,2,3}
s2={2,3,4,}
s3=s1&s2
print(s3)

#21 write a code to create a dictionary with the keys "name","age", and "city" and print it.
dict={"name":"harsh","age":22,"city":"ayodhya"}
print(dict)

#22 write a code to add new key value pair "country":"USA" to the dictionary.
dict1={'name':'john','age':'25'}
dict1['country']='USA'
print(dict1)

# another method
dict2={'name':'john','age':'25'}
dict2.update({'country':'USA'})
print(dict2)

#23 write a code to access to the value associated with the key "name" in the dictionary.
dictionary={'name':'alice','age':'30'}
print(dictionary['name'])

#24 write a code to remove a key "age" from the dictionary.
dict={'name':'bob','age':'22','city':'New york'}
value=dict.pop('age')
print(dict)

#25 write a code to check if the key"city" exists in the dictionary.
dictionary={'name':'alice','city':'paris'}
'city' in dictionary #True if present otherwise false

#26 write a code to create a list , tuple and dictionary and print them all.
list=[1,2,3,"harsh",1.2]
tuple=(1,2,3,"harsh",1.2)
dictionary={'name':'harsh','age':'21','city':'lucknow'}

print(list)
print(tuple)
print(dictionary)

#27 write a code to create a list of any 5 no's between 1 to 100,sort it in ascending order,and print the result.
list=[23,45,1,12,22]
list.sort()
print(list)

#if we want to arrange them in descending order so we use
list.sort(reverse=True)
print(list)

#28 write a code to create a list with strings and print the element at the third index.
fruits=["mango","orange","banana","apple","pineapple"]
print("this is third element of list:",fruits[2])

#29 write a code to combine two dictionary into one and print it.
dict1={'name':'alice','city':'paris'}
dict2={"b":"harsh","age":22,"c":"ayodhya"}
dict=dict1|dict2
print(dict)
#also use dict1.update(dict2)

#30 write a code to convert a list of string into a set.

my_list=["mango","orange","banana","apple","pineapple"]
my_set=set(my_list)
print(my_set)




































