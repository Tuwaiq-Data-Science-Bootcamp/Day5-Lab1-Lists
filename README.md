# Day5-Lab1-Lists

Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]

- Q1: Write a Python program to sum all the items in the list.
- Q2: Write a Python program to get the largest number from the list.
- Q3: Use list comprehension, create a new list from the above list containing only even numbers.
- Q4: Use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

#Q1: Write a Python program to sum all the items in the list.
list = [5, 4, 17, 19, 30, 2, 7, 10, 45]

s =sum(list)
print(s)
#Q2: Write a Python program to get the largest number from the list.
m = max(list)
m
#Q3: Use list comprehension, create a new list from the above list containing only even numbers.
x = [i for i in list if i % 2 ==0]
print(x)

#Q4: Use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
  listslice = list[6:]
    listslice
