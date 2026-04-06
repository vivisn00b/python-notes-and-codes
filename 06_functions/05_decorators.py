# Decorators are a flexible way to modify or extend behavior of functions or methods, without changing their actual code.
# A decorator is essentially a function that takes another function as an argument and returns a new function with enhanced functionality.
# Decorators are often used in scenarios such as logging, authentication and memorization, allowing us to add additional functionality to existing functions or methods in a clean, reusable way.

def decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()

# @decorator is syntactic sugar for:
# say_hello = decorator(say_hello)


# Decorators with arguments

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        res = func(*args, **kwargs)
        print("After function runs")
        return res
    return wrapper

@decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Viiiv")


# Decorators that return values

def double_res(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res*2
    return wrapper

@double_res
def add(a, b):
    return a+b

print(add(1, 2))


# Using multiple decorators

def bold(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello, world!"

print(text())


# Built-in decorators

# @staticmethod – makes a method static
# @classmethod – receives class as first argument instead of instance
# @property – turns method into a read-only attribute

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
print(c.area)  # No parentheses needed!
