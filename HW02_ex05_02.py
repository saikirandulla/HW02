#!/usr/bin/env python
# HW02_ex05_02

# Write a function called do_n that takes a function object and a number, n, as 
# arguments, and that calls the given function n times.

################################################################################
# Write your functions below:
# Body


def do_n(f,n):
	f(n) 
def print_hello(n):
	print("Hello World")
	n = n - 1
	if n <> 0:
		print_hello(n)
################################################################################
def main():
	
#    """Call your function within this function.
#    When complete have one function call in this function:
#    do_n(print_hello, 10)
#    """print_hello() # replace this with do_n(print_hello, 10)
	do_n(print_hello,10)


if __name__ == "__main__":
    main()