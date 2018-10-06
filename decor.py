import time

def how_long(func):
	def function(arg):
		start = time.clock()
		result = func(arg)
		end = time.clock()
		print('Function ', func.__name__, 'time is ', end - start)
		return result
	return function


@how_long
def long_func(arg):
	time.sleep(arg)
	return arg