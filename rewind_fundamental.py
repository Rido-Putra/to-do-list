'''# Variables and Data Types Exercise:
name = "rido"
age = 27
hobby = "fishing"
print(f"My name is {name}, I am {age} years old, and i enjoyed {hobby}.")

# Basic Operations Practice:
length = float(input("Enter the length of the rectangle: "))
width =  float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")
print("___________________________________")
# #Excercise 1 : Even or Odd
# asks user to enter a number
# checks whether the number is even or odd
# prints out an appropriate message to the user

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

print("___________________________________")
# #Excercise 2 : sum of a list
def sum_of_list(numbers):
    return sum(numbers)

my_numbers = [1,2,3,4,5,6,7]
print(f"the sum of the list is: {sum_of_list(my_numbers)}")
'''

#explore more on  functions
def greet(name):
    return f'hello, {name}'
print(greet("Rido"))

#Excercise 1. Maximum Value in a List
def find_max(numbers):
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

my_numbers = [2,6,4,8,9,2,3]
print(f'the maximum value is: {find_max(my_numbers)}')

def square_number(number):
    return number  * number
my_number_ = 2
print(f"the square number is {square_number(my_number_)}")

###List Comprehensions
## basic structure list comprehension 
## [expression for item in iterable]
squares = []
for i in range (1,6):
    squares.append(1 * i)
print(squares)

squares = [i * 1 for i in range(1,6)]
print(squares)

evens = []
for i in range (1,11):
    if i % 2 == 0:
        evens.append(i)  
print(evens)

evens = [i for i in range(1,11) if i % 2 == 0]
print(evens)

#Advanced use
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
flattened = [num for row in matrix for num in row]
print(flattened)

# question
matrix1 = [[[1,2,3],[4,5,6]],[7,8,9]]
print(matrix1)
flattened1 = [num for row in matrix1 for num in row for num in row]
print(flattened1)

def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Example usage:
area, perimeter = calculate_rectangle_properties(4, 6)
print(f"Area: {area}, Perimeter: {perimeter}")
