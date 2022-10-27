# Day5-Lab1-Lists

Given the following list : [5, 4, 17, 19, 30, 2, 7, 10, 45]

- Q1: Write a Python program to sum all the items in the list.




mylist = [5, 4, 17, 19, 30, 2, 7, 10, 45]



mysum = sum(mylist)
print(mysum)




- Q2: Write a Python program to get the largest number from the list.

mylist = [5, 4, 17, 19, 30, 2, 7, 10, 45]


mymax= max(mylist)


print(mymax)




- Q3: Use list comprehension, create a new list from the above list containing only even numbers.

lst1 = [5, 4, 17, 19, 30, 2, 7, 10, 45]

for x in lst1 :
    if x%2==0:
        print(x, 'Is an even number')


