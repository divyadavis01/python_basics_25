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

def add(n):
    for i in range(1,11):
        k=n*i
        print(f"{n} * {i} = {k}")
    
n=int(input("Enter a number: "))
add(n)