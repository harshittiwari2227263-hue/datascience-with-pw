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




































