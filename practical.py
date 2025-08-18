
#PYTHON BASIC QUESTIONS
"""
1. What is Python, why is it popular?
ANS-Python is a high level and interpreted language, it is popular because of widely use in industry and it also have many libraries ,easy to learn many other ways because of that it is popular .

2. What is an interpreter in Python?
ANS- In Python , an interpreter is a program that executes Python code line by line and it translates high level python code into machine level language .

3. What are pre-defined keywords in Python?
ANS- There are many pre-defined keywords like type, length, index, Print  and other.

4. Can keywords be used as variable names?
ANS- No Will not built keywords as variable names.

5. What is mutability in Python?
Ans- Mutability means you will change the values after creation.

6. Why are list mutable, but tuples are non mutable?
Ans-list is mutable because size of list is not fix , but in tuples size will be fixed after creation.

7. What is the difference between"==" and "is" Operators in Python?
Ans-  #"==" means to different objects and variables are equal.
    #"is" means that item will present in this item.

8. What are logical operators in python?
Ans- LogicalAND, logicalOR and logicalNOT these are logical operators in python.

9. What is typecasting in Python?
Ans-Typecasting means changing one datatype to other datatype.

10. What is the difference between implicit and explicit typecasting?
Ans-Implicit-it will automatically change.
    Explicit-user will change the datatype according to the condition.

11. What is the purpose of conditional statement in python?
Ans- the purpose of conditional statement is that to code you decision with some condition if it is valid then yes if it is not valid then false What does the LM statement work to complete decision.

12. How does the "elif" statement work ?
Ans-"elif" statement work like if "if" statement will false then we come on to the "elif"
then we check the condition of "elif" if condition is true then print "elif" otherwise it will automatically print "else" statement.

13. What is the difference between for and while loop?
Ans-"for" loop will check for every particular statement and "while" loop will run whether the condition is true.

14. Describe a scenario where a while loop is more suitable than a for loop?
Ans-In while loop if condition is true then the further loop will not execute , but in for loop every condition will be execute."""

# practical question


#1
print("hello, world!")

#2
name=input("enter your name : ")
age= int (input("enter your age: "))
print(name)
print(age)

#3
import keyword
print("list of python keywords:")
for i in keyword.kwlist:
    print(i)

#4
import keyword
n=input(" enter any keyword:")
if keyword.iskeyword(n):
    print(" it is a python keyword")
else:
    print(" not a python keyword")

#5
t = (10, 20, 30, 40)
t1=[1,2,3,4,5]
t1.append(45)
temp = list(t)#it tuples we can't append or add any value so if we want to add any value so first we want to convert tuple ito a list and then tuple .

temp[1] = 200
temp.append(50)
t = tuple(temp)
print(t)
print(t1)

#6 write a func to demonstrate the behavior of mutability and immutability arguments.
#immutable argument
def modify_value(x):
    x = x + 10
    print("Inside function:", x)
num = 5
modify_value(num)
print("Outside function:", num)

#mutable argument
def modify_list(lst):
    lst.append(4)
    print("Inside function:", lst)
my_list = [1, 2, 3]
modify_list(my_list)
print("Outside function:", my_list)

#7write a program that perform a basic arithmetic operation by taking users input.
a = int(input("enter your 1st no :"))
b = int(input("enter your 2st no :"))
add=a+b
sub=a-b
multiply=a*b
print(add)
print(sub)
print(multiply)

#8 write a program to demonstrate the use of logical operator>
# use of AND
name="harshit"
age=22

if name=="harshit" and age==22:
    print("user")
else:
    print("not a user")
#in and both the condition will true then true if any condition is false then false.

# use of or
# in or if any of the condition is  true then true otherwise false.
num = 150
if num < 0 or num > 100:
    print("Number is out of range")
else:
    print("Number is within range")

# NOT
is_raining=True
if not is_raining:
    print("go without umbrella")
else:
    print("go with umbrella")


#9 covert the users string into int,float and boolean types.

value = input("Enter any value: ")
try:
    a = int(value)
except ValueError:
    a = "Cannot convert to int"
try:
    b = float(value)
except ValueError:
    b = "Cannot convert to float"
c = bool(value)

print("Original (string):", value)
print("As Integer:", a)
print("As Float:", b)
print("As Boolean:", c)

#10 write a code to demonstrate type casting with list elements.
list=[1,2,3,"harsh",15.0,True]
list[4]=int(list[4])
list[1]=float(list[1])
print(list)

#11 write a program that check the no is positive , negative and zero
number= int(input("enter any no:"))
if number<0:
    print("negative")
elif number>0:
    print("positive")
else:
    print("zero")

#12 write a for loop to print number from 1 to 10.
for i in range (1,11):
    print(i)

#13 write a program to find the sum of even no between 1 to 50.
Total=0
for i  in range (1,51):
    if i%2==0:
        Total+=i
print("the sum of even no between 1 to 50:",Total)

#14 write a program to reverse a string using while loop.
string="harshit"
reversed_string=""
i=len(string)-1
while i >=0:
    reversed_string+= string[i]
    i-=1
print(reversed_string)

#15 factorial of any no using while loop:
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial of", n, "is:", fact)






