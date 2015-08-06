#!/usr/bin/env python
# HW02_ex03_05

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated
# sequence:

# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the 
# value printed next appears on the same line.

# print '+', 
# print '-'

# The output of these statements is '+ -'.

# A print statement all by itself ends the current line and goes to the next line.


def two_by_two(d,f):
	print d
	print f
	print f
	print f
	print f
	print d
	print f
	print f
	print f
	print f
	print d




# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def four_by_four(h,i):
	print h
	print i
	print i
	print i
	print i
	print h
	print i
	print i
	print i
	print i
	print h
	print i
	print i
	print i
	print i
	print h
	print i
	print i
	print i
	print i
	print h

# Write your functions above:
################################################################################
def main():
	print("Hello World!")
	a = '+'
	b = '-'
	c='|'
	e = " "
	d = a + 4*b + a + 4*b + a
	f = c + 4*e + c + 4*e + c 
	two_by_two(d,f)
	h = a + 4*b + a + 4*b + a + 4*b + a + 4*b + a
	i = c + 4*e + c + 4*e + c + 4*e + c + 4*e + c
	four_by_four(h,i)

if __name__ == "__main__":
    main()