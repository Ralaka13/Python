#print("Hello, World")

#myint = 7
#print(myint)

#myfloat = 7.0
#print(myfloat)

#yfloat = float(7)
#print(myfloat)

#mystring = 'hello'
#print(mystring)
#mystring = "hello"
#print(mystring)

#mystring = "Don't worry about using apostrophes"
#print(mystring)

#one = 1
#two = 2
#three = one + two
#print(three)

#hello = "hello"
#world = "world"
#helloworld = hello + " " + world
#print(helloworld)

#a, b = 3, 4
#print(a,b)

#This will not work
#one = 1
#two = 2
#hello = "hello"

#print(one + two + hello)

# change this code
#mystring = "hello"
#myfloat = float(10)
#myint = 20

# testing code
#if mystring == "hello":
#    print("String: %s" % mystring)
#if isinstance(myfloat, float) and myfloat == 10.0:
#    print("Float: %f" % myfloat)
#if isinstance(myint, int) and myint == 20:
#    print("Integer: %d" % myint)

#mylist = []
#mylist.append(1)
#mylist.append(2)
#mylist.append(3)
#print(mylist[0])
#print(mylist[1])
#print(mylist[2])

#for x in mylist:
#    print(x)

#mylist = [1,2,3]
#print(mylist[10])

#Exercise Lists
#numbers = [1,2,3]
#strings = ["hello","world"]
#names = ["John","Eric","Jessica"]

#write code here
#second_name = names[1]

#this code should write out the filled arrays and the second name in the names list (Eric)
#print(numbers)
#print(strings)
#print("The second name on the names list is %s" % second_name)

#Basic Operators

#Arithmetic Operators
#number= 1 + 2 * 3 / 4.0
#print(number)

#remainder = 11 % 3
#print(remainder)

#squared = 7 ** 2
#cubed = 2 ** 3
#print(squared)
#print(cubed)

#helloworld = "hello" + " " + "world"
#print(helloworld)

#lotsofhellos = "hello" * 10
#print(lotsofhellos)

#even_numbers = [2,4,6,8]
#odd_numbers = [1,3,5,7,]
#all_numbers = odd_numbers + even_numbers
#print(all_numbers)

#print([1,2,3] * 3)

#Exercise

#x = object()
#y = object()

#x_list = ([x] * 10)
#y_list = ([y] * 10)
#big_list = x_list + y_list

#print("x_list contains %d objects" % len(x_list))
#print("y_list contains %d objects" % len(y_list))
#print("big_list contains %d objects" % len(big_list))

#if x_list.count(x) == 10 and y_list.count(y) == 10:
#    print("Almost there...")
#if big_list.count(x) == 10 and big_list.count(y)  == 10:
#    print("Great!")

#String Formatting
#Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

#Let's say you have a variable called "name" with your user name in it, and you would then like to print(out a greeting to that user.)

name = "John"
print("Hello, %s!" % name) 


name = "John"
age = 23
print("%s is %d years old." %(name, age))

mylist = [1,2,3]
print("A lsit: %s" % mylist)

#Here are some basic argument specifiers you should know:

#%s - String (or any object with a string representation, like numbers)

#%d - Integers

#%f - Floating point numbers

#%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

#%x/%X - Integers in hex representation (lowercase/uppercase)

#Exercise
#You will need to write a format string which prints out the data using the following syntax: Hello John Doe. Your current balance is $53.44.

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current account balance is %s"

print(format_string % data)