# a=[1,2,3,4,5]
# for i in a:
#     print(i)

# b=[1,"abc",3j]
# for j in b:
#     print(j)

# c=(1,2,"three")
# for k in c:
#     print(k,end=" ")

# end is used as a space 

# a={1:"one",2:"two",3:"three"}
# for i,j in a.items():
#     print(f"{i} {j}")

# b="Python"
# for i in b:
#     print(i)

# c={1,2,3,4,5,6,7,8}
# for i in c:
#  if i%2 != 0:
#   print(i)



# print("Enter a number for multiplication table: ")
# a=int(input())
# for i in range(1,11):
#     print(f"{i} * {a} = {i*a}")


n=int(input("Enter a number: "))
fact=1
for k in range(1,n+1):
    fact=fact*k
print(fact)

# enumerator