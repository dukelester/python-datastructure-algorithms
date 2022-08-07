

def myDecorator(function):
    function()
    print("Yes how are you doing today")


def functionDecorator(func):
    def inner_function():
        func()
        print('Decorator is here')
        return inner_function
@functionDecorator
def greet():
    print("Hello duke lester")

greet()


