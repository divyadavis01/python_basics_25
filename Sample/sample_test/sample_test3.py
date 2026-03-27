"""
1 2 3
4 5 6
7 8 9
matrix to 90 degree
3 6 9
2 5 8
1 4 7

"""
# n=3
# for i in range(1,4):
#     for j in range(1,4):
#         print(n,end=" ")
#         n=n+3
#     n=3-i
#     print()

"""
7 4 1
8 5 2
9 6 3
"""

# n=7
# for i in range(1,4):
#     for j in range(1,4):
#         print(n,end=" ")
#         n=n-3
#     n=7+1
#     print()

"""
string reverse
hello 

olleh
"""
# s=input("Enter a string: ")
# ch=""
# for i in s:
#     ch=i+ch
# print(ch)

"""
palindrome
"""
# n=input("Enter a string: ")
# if n==n[::-1]:
#     print("palindrome")

""" find largest element in the list """

# n=int(input("Enter the size of the list: "))
# l=[]
# for i in range(n):
#     li=int(input(f"ENter the {i+1} element: "))
#     l=l+[li]
# for i in range(n):
#     for j in range(n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l[n-1])

"""
frequency of character
"""
# s=input("Enter a string:")
# d={}
# for ch in s:
#     if ch in d:
#         d[ch]=d[ch]+1
#     else:
#         d[ch]=1
# for m,n in d.items():
#     print(f"{m} : {n}")

"""
frequency of word in a list
"""
# strword=input("Enter words with a space: ")
# word=[]
# space=""
# d={}
# for ch in strword:
#     if ch!=" ":
#         space=space+ch
#     else:
#         if space:
#             word=word+[space]
#             space=""
# if space:
#     word=word+[space]
# print(f"{word}")
# for w in word:
#     if w in d:
#         d[w] = d[w] + 1
#     else:
#         d[w] = 1
# for m,n in d.items():
#     print(f"{m} : {n}")


""" if multiple of 3 print fizz"""
# for i in range(1,51):
#     if i%3 == 0:
#         print("fizz")
#     else:
#         print(i)

"""
find higest mark
students = [
    ("Rahul", 78),
    ("Anita", 85),
    ("John", 92),
    ("Priya", 88)
]
"""

# students = [
#     ("Rahul", 78),
#     ("Anita", 85),
#     ("John", 92),
#     ("Priya", 88),
#     ("Anna",100)
# ]
# student=[list(items) for items in students]
# print(student)
# for i in range(len(student)):
#     for j in range(len(student)-i-1):
#         if student[i][1]>student[i+1][1]:
#             student[i][1],student[i+1][1]=student[i+1][1],student[i][1]
# students=[tuple(items) for items in student]
# print(students)
# print(f"Top Student : {students[i][0]} \nMark : {students[i][1]}")

"""
Return a list of employees earning more than 50,000.

employees = [
    ("Alice", 40000),
    ("Bob", 60000),
    ("Charlie", 75000),
    ("David", 45000)
]
"""
# employees = [
#     ("Alice", 40000),
#     ("Bob", 60000),
#     ("Charlie", 75000),
#     ("David", 45000)
# ]

# for i in range(len(employees)):
#     if employees[i][1] > 50000:
#         print(f"{employees[i][0]} : {employees[i][1]}")

"""
Each product is stored as a tuple:

(product_name, price, quantity)

Find the total inventory value.

Example
products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 10),
    ("Keyboard", 1500, 5)
]
"""
# products = [
#     ("Laptop", 50000, 2),
#     ("Mouse", 500, 10),
#     ("Keyboard", 1500, 5)
# ]

# total=0
# for p in products:
#     total=total+(p[1]*p[2])
# print(total)

"""
Sort student records based on marks.

Example
students = [
    ("Aman", 65),
    ("Riya", 92),
    ("Kiran", 78)
]
"""
# students = [
#     ("Aman", 65),
#     ("Riya", 92),
#     ("Kiran", 78)
# ]
# s=[list(items) for items in students]
# for i in range(len(s)):
#     for j in range(len(s)-i-1):
#         if s[j][1]<s[j+1][1]:
#             s[j][1],s[j+1][1]=s[j+1][1],s[j][1]
# student=[tuple(items) for items in s]
# print(student)

"""
convert to tuple
names = ["A", "B", "C"]
scores = [90, 85, 88]
"""
# names = ["A", "B", "C"]
# scores = [90, 85, 88]

# l=[]
# for i in range(len(names)):
#     l=l+[(names[i],scores[i])]
# print(l)

"""Remove duplicate records.

Example
data = [
    ("apple", 10),
    ("banana", 20),
    ("apple", 10)
]"""
# data = [
#     ("apple", 10),
#     ("banana", 20),
#     ("apple", 10)
# ]
# u=list(set(data))
# print(u)

"""
Calculate the average marks.

Example
students = [
    ("A", 80),
    ("B", 90),
    ("C", 70)
]
"""
# students = [
#     ("A", 80),
#     ("B", 90),
#     ("C", 70)
# ]
# t=0
# for i in students:
#     t=t+i[1]
# avg=t/len(students)
# print(avg)

"""
    *
   * *
  * * *
 * * * *
* * * * *
"""

# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

"""
find missing numbers in th list [1,3,5,6]
"""
# n=int(input("Enter the size: "))
# l=[]
# for i in range(n):
#     num=int(input(f"Enter element {i+1}: "))
#     l=l+[num]
# for i in range(len(l)):
#     for j in range(len(l)-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
# print(l[n-1])
# for i in range(l[0],l[n-1]):
#     if i not in l:
#         print(i)

"""GCD and LCM of 2 numbers """
a=int(input("Enter the first number: "))
b=int(input("Enter the 2nd element: "))
hcf=1
small=a if a<b else b
for i in range(1,small):
    if a%i==0 and b%i ==0:
        hcf=i
print(hcf)
lcm=(a*b)//hcf
print(lcm)

