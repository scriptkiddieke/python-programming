# python variables
fruit = "mangos"
anotherfruit = "orange"
name = "Alex"

#display the output using the print statement
print(fruit)
print(anotherfruit)
print(name)

# python datatypes datatype
x = 10 # x is an integer
y = 20.5 # y is a float datatype value
name = 'John Doe' # name is a string datatype value
message = "let's code" #string with double quotes
isTrue = x > y #boolean value
myList = ['alex','mwangi','mungai',794555400,'alex@gmail.com'] #list datatype value
myDctionary = {
    "name" : "John Doe",
    "Email" : "doe@gmail.com",
    "phone number" : +254794555400,
    "Adress" : "Nakuru",
    "Id N0" : 24537212,
    "is maried" : "false"
}

print(x + y) # add 2 integers
print(name," ",message) #print a string
print(isTrue) #print boolean value (true or false)
print(myList)
print(myDctionary)

#python numbers
a = 3 # inter number
b = 3.5 # float number
c = 3.5j # complex number
d = 10.02345

print('a : ', a , '\nb : ', b , '\nc : ', c)

# getting the type of datatypes
print(type(a))
print(type(b))
print(type(c))
print(type(d))


# python number method

# The round() method is used to round numbers
pi = 3.1454567
rounded_number = round(pi, 2) 
print(rounded_number) #print the rounded number which is 3.

# the pow() method
myNumber = pow(3, 2)
print(myNumber) # prints 9

# getting the absolute value
# the abs() function return the absolute value
a = abs(-1)
print(a)

#getting the quotient and remainder using divmod() function
x = divmod(5, 2)
print(x) # prints the quotient and the remainder

# Python strings
text = 'Hello world'
print(text) # prints hello world