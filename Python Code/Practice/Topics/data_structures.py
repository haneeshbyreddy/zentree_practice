# List
names = ['sam', 'rob', 'petter']
#slice
first_two_names = names[:2]
#insert
names.insert(2, 'alex')
# extend
names.extend(['robert', 'henry'])
# remove
names.pop(1)
del names[1]
# List Comprehension
names = [i.upper() for i in names]
# sort
nums = [3,5,2,1,6,8,0]
sorted_nums = sorted(nums) # returns sorted list
reverse_sorted_nums = sorted(nums, reverse=True) # return reverse sorted list
nums.sort() # inplace sort
# copy
copy_nums = nums.copy()

# Tuples
my_tuple = (1, 'sam', 'rob', False)
# slice
first_two = my_tuple[:2]
# using *
(one, *two) = my_tuple # one is element and two is list
# count
no_of_False = my_tuple.count(False)

# Sets
my_set = {'sam', 'rob', 'petter'}
# check element
bool_sam = 'sam' in my_set
# add element
my_set.add('robert')
# remove
my_set.remove('rob')
# union
dup_set = my_set.union({"alex", 'robert'})
# intersection
common_set = my_set.intersection({'sam', 'rob'})
# uncommon elements in set_1
my_set = my_set - {'sam'}