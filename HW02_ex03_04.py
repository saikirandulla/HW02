#!/usr/bin/env python
# HW02_ex03_04

# A function object is a value you can assign to a variable or pass as an 
# argument. For example, do_twice is a function that takes a function object 
# as an argument and calls it twice:

# def do_twice(f):
#     f()
#     f()

# Here's an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
#     print 'spam'

# do_twice(print_spam)

# 1. Type this example into this script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value,
#  and calls the function twice, passing the value as an argument.
# 3. Write a more general version of print_spam, called print_twice, that takes a 
# string as a parameter and prints it twice.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam'
#  as an argument.
# 5. Define a new function called do_four that takes a function object and a value 
# and calls the function four times, passing the value as a parameter. There 
# should be only two statements in the body of this function, not four.
################################################################################
# Write your functions below:
# Body
#
#2. def do_twice(f,s):
#	f(s)
#	f(s)
	
#def print_spam(s):
#	print s
	
#3. 

#def print_twice(s): 
#	print s
#	print s
	
#def new_do_twice(f,s):
#	f(s)
#	f(s)
	
#def print_spam(s):
#	print s
	
#def print_twice(s): 
#	print s
#	print s

def do_four(f,s):
	f(s)
	
def print_four(s):
	print (s*4)
	

# Write your functions above:
################################################################################
def main():
  """Call your functions within this function.
  When complete have one function call in this function:
  do_four([function object], [some_value])
  """
  print("Hello World!")
#  print_twice("spam1")
#  new_do_twice(print_twice,"spam")
  do_four(print_four,"Hi")
#	print_twice("spam")

if __name__ == "__main__":
    main()