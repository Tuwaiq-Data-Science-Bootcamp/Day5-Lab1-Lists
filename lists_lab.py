my_list : list = [5, 4, 17, 19, 30, 2, 7, 10, 45]

# - Q1: Write a Python program to sum all the items in the list.
total : int = 0
for i in my_list:
    total = total + i
print(total)

# Q2: Write a Python program to get the largest number from the list.
largest_value : int = 0
for i in my_list:
    if i > largest_value:
        largest_value = i
    else:
        largest_value = largest_value
print(largest_value)

#Q3: Use list comprehension, create a new list from the above list containing only even numbers.
new_list : list = []
[ new_list.append(i) for i in my_list if i%2 == 0]
print(new_list)

# Q4: Use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
new_list2 : list = print(my_list[0: 5])