# Rounding in python

# Python has a round() function that rounds numbers.

print(round(1,123456789))

# It is possible to round a number to a specific decimal place/digit.
print(round(1.123456789, 5)) # In this case, it rounded to 5 decimal digits, the 5th decimal place.
print()

# Python rounds even numbers down and odd numbers up

print("Unrounded Numbers ≈ Rounded Numbers")
i = 1.5
while i <= 20:
  print(i, end = " ≈ ")
  print(round(i))
  i += 1
print()

# Python automatically assigns data types according to the result.
# For example: whole numbers are assigned as integers; while decimal numbers are assigned as floats.
# This even converts already existing data to different data types.

x = round(2.55)
print(x, type(x)) # Python converted the rounded number to integer type.

x = round(2.55, 1)
print(x, type(x)) # Python converted the rounded number into a float, which was previously an integer.

x = round(2.55)
print(x, type(x)) # Python converted the rounded float back into an integer.

# Here is how to round lists
listy = [ 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5 ]
print(listy)
roundylisty = [ round(i) for i in listy ]
print(roundylisty)
# print(round(roundy)) This would not work.

# Rounding Libraries
# It is also possible to use the numpy library for rounding

import numpy as np

array = np.array([[1.5,2.5,3.5,4.5,5.5], [6.5,7.5,8.5,9.5,10.5]])

print("You'd like me to round these numbers?")
print(array)
print("I'm very odd at rounding numbers, but lemme try! Even numbers are oddly rounded down. Odd numbers are normally rounded up. Did I do it right?")
print(np.round(array))

#print(round(array)) does not work in native Python. That is one reason to use numpy.

# Additionally, you can also truncate in Numpy. Note that numpy returns floats
print("Numpy: Untruncated Numbers ≈ Truncated Numbers")
i = 1.5
while i < 11:
  print(i, end = " ≈ ")
  print(np.trunc(i))
  i += 1
print()

# Additionally, you can also truncate in Math. Note that math returns integers
print("Math: Untruncated Numbers ≈ Truncated Numbers")
i = 1.5
while i < 11:
  print(i, end = " ≈ ")
  print(math.trunc(i))
  i += 1
print()

# Furthermore, it is possible to round down or up.
print("Math: Unfloored Numbers ≈ Floored (Rounded Down) Numbers")
i = 1.5
while i < 11:
  print(i, end = " ≈ ")
  print(math.floor(i))
  i += 1
print()

print("Math: Unceiled Numbers ≈ Ceiled (Rounded Up) Numbers")
i = 1.5
while i < 11:
  print(i, end = " ≈ ")
  print(math.ceil(i))
  i += 1
print()

