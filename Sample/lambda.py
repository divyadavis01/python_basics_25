# lambda -- used to excute single line instru
# map   --- used to iterate each element and give a map object
# filter -- used to extract elemnts that satisfes given condition

# def add(a,b):
#     c=a+b
#     return c
# print(add(10,5))

# lambda usage

# c=lambda a,b:a+b
# print(c(10,10))

# def multiply(num):
#     return num*2
# n=[10,20,30]
# for i in n:
#     print(multiply(i))

# map
# should be iteratable
# n=[10,20,30]
# print(list(map(lambda num:num*2,n)))

# n=[10,20,30,15]
# print(list(map(lambda num:True if num%2==0 else False,n))) 

#filter using map n lambda
n=[10,20,30,15]
# print(list(filter(lambda num:True if num%2==0 else False,n))) 

# lists=[10,20,30,15]
# print(list(filter(lambda l:True if l*2==20 else False,lists)))

# print(sorted(n))


# item=[("A",7,2000),("B",5,2000),("C",2,2000)]

# print(sorted(stock for _,stock,_ in item))
# print(sum(stock for _,stock,_ in item), sum(price for _,_,price in item))

# print()

# print(sorted(item,key = lambda pro:pro[1]))

# # try using dict

Marks=[("Anna",20,30,40,25),("Ben",30,40,20,25),("Catherine",50,30,20,40),("Disna",20,50,30,40)]
print(sum(maths for _,maths,_,_,_ in Marks))
# print(sum(sci for _,_,sci,_,_ in Marks))

# print(sorted(Marks,key = lambda m:m[1]))

