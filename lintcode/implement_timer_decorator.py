'''

Decorator is a special python syntax, You can written on the above line of the function to be decorated with the syntax @decorator_name like this:

@decorator_name
def func():
    # do something
    pass
Decorator support some processing with certain universality before and after the function runs. These kind of processings usually need to package multiple functions, so decorator could help us to avoid duplicate codes and improve the readability.

The task of this problem is to implement a timer decorator, this decorator named timer. We could wrap timer to any functions so that when the function be called, the cost time of the function will be recorded and automatically printed out.

'''
def timer(func):
    def wrapper(*args, **kwargs):
        t = time.time()
        ans = func(*args, **kwargs)
        t = time.time() - t
        print(f"function {func.__name__} cost {t:.1f} seconds")
    return wrapper
