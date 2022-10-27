# Day5-Lab1-Lists

Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]

- Q1: Write a Python program to sum all the items in the list.

lst = [5, 4, 17, 19, 30, 2, 7, 10, 45]

i = 0
sum = 0
while i < len(lst):
    sum = sum + lst[i]
    i = i + 1
print (sum)

- Q2: Write a Python program to get the largest number from the list.

print(max(lst))


- Q3: Use list comprehension, create a new list from the above list containing only even numbers.

newList = []
for x in lst:
    if x % 2 == 0:
        newList.append(x)
print(newList)

- Q4: Use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

x = slice(0,5)
print(lst[x])
