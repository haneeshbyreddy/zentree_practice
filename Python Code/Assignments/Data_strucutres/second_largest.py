my_list = [15,6,9,5,8,12]

var1 = var2 = 0

print("taken list", my_list)

for i in my_list:
    if i > var2:
        var1 = var2
        var2 = i
    if i > var1 and i != var2:
        var1 = i

print("second largest number", var1)
