
# multiplication function
def multiply(x,y):
    return x * y

# division function
def divide(x,y):
    return x / y

# addition function
def add(x,y):
    return x + y

# subtraction function
def subtract(x,y):
    return x - y

print("This calculator function will multiply 8 and 9")
x = multiply(8,9)
print(x)

print("This calculator function will divide 8 and 9")
x = divide(8,9)
print(x)

print("This calculator function will add 8 and 9")
x = add(8,9)
print(x)

print("This calculator function will subtract 9 from 8")
x = subtract(8,9)
print(x)

#Bonus section (print functions commented out as they were not asked in the assignment)

# square function
def square(x):
    return x ** 2
# print( "This calculator function will square 12")
# x = square(12)
# print(x)


# cube function
def cube(x):
    return x ** 3
# print( "This calculator function will take the cube of 8")
# x = cube(8)
# print(x)


#I think the last exercise in the bonus section can be interpreted in two ways. I've listed both below. 

# function that squares a number and multiplies it with a specified number
def square_n_times(x,n):
	return (x ** 2)* n 
# print( "This calculator function will square 4 and multiply the result by 3")
# x = square_n_times(4,3)
# print(x)

# a function that squares a number and raises the result to the power of a specicified number
def square_n_times_alternate(x,n):
	return (x**2)**n
# print( "This calculator function will square 3 and raise the result to the power of 2")
# x = square_n_times_alternate(3,2)
# print(x)
	