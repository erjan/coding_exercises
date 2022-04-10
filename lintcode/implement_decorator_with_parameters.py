'''

Please implement a decorator named repeat_func, it takes an integer n as parameter which indicate how many times to repeat running the decorated function.

Besides repeat running the decorated function, you code need to print before function run before the function be called, and print after function run after all functions finished running.

You can check the code in main.py to see how repeat_func be called.

'''


def repeat_func(n):


	def wrapper(func):

		def f():
			print('before function run')
			for _ in range(n):
				func()
			print('after function run')
		return f
	return wrapper
