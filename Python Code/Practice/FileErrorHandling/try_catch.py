x = "word"
y = 2
try:
	z = x + y
except TypeError:
	print("Error: cannot add an int and a str")
else:
	print('Addition done')
finally:
	print("End of program")