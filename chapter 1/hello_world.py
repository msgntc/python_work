confusingvariablename = "its dangerous to go alone, take this! <=====|--->"
print(confusingvariablename)

def greet(name):
    return f"Hello, {name}!"
print(greet("Adventurer"))
def add(a, b):
    return a + b
print(add(5, 7))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
def is_even(num):
    return num % 2 == 0
print(is_even(10))
print(is_even(7))   

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print(fibonacci(10))
print(fibonacci(15))
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello, World!"))
print(reverse_string("Python"))
def square_list(lst):
    return [x**2 for x in lst]
print(square_list([1, 2, 3, 4, 5]))
print(square_list([-1, -2, -3]))
def find_max(lst):
    return max(lst)
print(find_max([3, 1, 4, 1, 5, 9, 2, 6, 5]))
print(find_max([-10, -20, -3, -4]))
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
print(count_vowels("Hello, World!"))
print(count_vowels("Python Programming"))