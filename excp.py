#1.- Name and handle the exception occured in the following program: 

a=3
try:
    if a<4:
        a=a/(a-3)
        print(a)
except Exception as er :
    print("Name of exception occured is :",er)
print("\n")
print("*"*25)
print("\n")

#2- Name and handle the exception occurred in the following program:

l=[1,2,3]
try:
    print(l[3])

except Exception as er :
    print("Name of exception occured is :",er)
print("\n")
print("*"*25)
print("\n")

#3- What will be the output of the following code:

'''# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not'''
'''OUTPUT:
    An exception
    Traceback (most recent call last):
    File "C:\Git\assignment_13\excp.py", line 31, in <module>
    raise NameError("Hi there")  # Raise Error
    NameError: Hi there'''


#4- What will be the output of the following code:

''' # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

OUTPUT:
    -5.0
    a/b result in 0'''

#5.Write a program to show and handle following exceptions: 
#1. Import Error
#2. Value Error
#3. Index Error

try :
    from math import minus
except ImportError as er1:
    print("EXCEPTION OCCURED")
    print(er1)
    print("\n")
try:
    li = [0,1,3,str]
    print(li[5])
except IndexError as er2:
    print("EXCEPTION OCCURED")
    print(er2)
    print("\n")
try:
    val = int("meenal")
except ValueError as er3:
    print("EXCEPTION OCCURED")
    print(er3)
    print("\n")
print("\n")
print("*"*25)
print("\n")

#6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18).

class AgeTooSmallError(Exception):
    "Raised when age is less than 18"

age = 18

while True:
    try:

        ip_age = int(input("enter the age:"))
        if (ip_age<age):
            raise AgeTooSmallError
        break
    except  AgeTooSmallError:
        print("WARNING : Age must not be less than 18")
        print()
print("YEAH,it's perfect")
    
    
    

    

