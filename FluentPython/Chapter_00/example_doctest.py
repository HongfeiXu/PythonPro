def factorial(n:int):
	"""
	Return the factorial of n, an exact integer >= 0

	>>> factorial(5)
	120
	>>> factorial(-1)
	Traceback (most recent call last):
	...
	ValueError: n must be >= 0
	>>> factorial(30.1)
	Traceback (most recent call last):
	...
	ValueError: n must be exact integer
	>>> factorial(1e100)
	Traceback (most recent call last):
	...
	OverflowError: n too larges
	"""
	import math
	if not n >= 0:
		raise ValueError("n must be >= 0")
	if math.floor(n) != n:
		raise ValueError("n must be exact integer")
	if n + 1 == n:
		raise OverflowError("n too large")
	result = 1
	factor = 2
	while factor <= n:
		result *= factor
		factor += 1
	return result


if __name__ == "__main__":
	import doctest
	doctest.testmod()


"""
用法：
py.exe -m doctest .\example_doctest.py
py.exe -m doctest .\example_doctest.py -v

PS E:\BooksLearn\PythonPro\FluentPython\Chapter_00> py.exe -m doctest .\example_doctest.py -v
Trying:
    factorial(5)
Expecting:
    120
ok
Trying:
    factorial(-1)
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: n must be >= 0
ok
Trying:
    factorial(30.1)
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: n must be exact integer
ok
Trying:
    factorial(1e100)
Expecting:
    Traceback (most recent call last):
    ...
    OverflowError: n too large
ok
1 items had no tests:
    __main__
1 items passed all tests:
   4 tests in __main__.factorial
4 tests in 2 items.
4 passed and 0 failed.
Test passed.
PS E:\BooksLearn\PythonPro\FluentPython\Chapter_00>
"""

