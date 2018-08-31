#!/usr/bin/env python
import sys
x = 3
y = 4
z = x + y
print("Program evaluates a defined function z.")
print("Enter z<Enter> and then <Ctrl-D>")
result = eval(sys.stdin.read())
#enter "z" at the command line
#Press Ctrl-D to end entry
print (result, type(result))
