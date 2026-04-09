"""
Remove Duplicates: Convert a list to a set and back to a list to remove duplicates quickly.
"""

# n=int(input("How many numbers should be entered to the list: "))
# m=input("enter the number:(with space) ")
# num=m.split()
# print(num)
# int_n=[int(x) for x in num]
# print(int_n)
# s=set(int_n)
# l=list(s)
# print(l)

# def add(n):
#     for i in range(1,11):
#         k=n*i
#         print(f"{n} * {i} = {k}")
    
# n=int(input("Enter a number: "))
# add(n)

# def reverse_string(s):
#      if len(s) == 0:
#          return s 
#      else: 
#         return reverse_string(s[1:]) + s[0]
# print(reverse_string("hello")) # Output: "olleh"

# square = lambda x: x * x 
# print(square(7))

# num=[1,2,3,4,5,6,7,8,9,10]
# square=[ x*x for x in num ]
# print(square)

# string = 'Python Programming is fun'
# for str in string:
#     if str in "aeiouAEIOU":
#         print(str,end=" ")

# numbers = range(1, 21)
# even= [num for num in numbers if num % 2 == 0]
# print(even)

# text="python"
# reversed_text = text[::-1]
# print(reversed_text)

# text="marble"
# print(text.count("m")) 

# sentence = "Python is fun to learn"
# print(sentence.replace(" ", "_"))


"""
Enter a list; list out the missing numbers from that list
list=[2,5,3,8]
output=[4,6,7]
"""
# l=int(input("Enter the size of the list:"))
# list=[]
# for i in range(1,l+1):
#     n=int(input(f"Enter the {i} element: "))
#     list=list+[n]
# print(list)
# for j in range(l):
#     for k in range(0,l-j-1):   
#         # print(l-j-1)
#         if list[j]>list[j+1]:  #2>5
#             print(list[j],list[j+1])
#             n=list[j]
#             list[j]=list[j+1]
#             list[j+1]=n
# print(list)
# small=list[0]
# large=list[-1]
# print(small,large)

# for num in range(small,large+1):
#     if num not in list:
#         print(num)

"""reverse a list """
# l=[1,2,3,4,5]
# n=len(l)
# for i in range(n,0,-1):
#     print(i)
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    for k in range(len(l)-1,-1,-1):
        print(i[k],end=" ")
    print()
