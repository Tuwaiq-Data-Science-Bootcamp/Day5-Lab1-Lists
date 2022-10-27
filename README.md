# Day5-Lab1-Lists

Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]

- Q1: Write a Python program to sum all the items in the list.
lst =[5, 4, 17, 19, 30, 2, 7, 10, 45]
x=0
for i in lst:
    x=x+i
print(x)
- Q2: Write a Python program to get the largest number from the list.
y=0
for i in lst:
    if i > y:
        y=i
    else: y=y
print (y)
- Q3: Use list comprehension, create a new list from the above list containing only even numbers.
list2=[]
for iteam in lst:
    if iteam%2==0:
        list2.append(iteam)
print(list2)
- Q4: Use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
newList = lst[:5]
print(newList)
