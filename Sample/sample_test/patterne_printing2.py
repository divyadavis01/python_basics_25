"""
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 

"""
# for i in range(1,5+1):
#     for j in range(1,5-i+2):
#         print(j,end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


"""
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
# for i in range(5,0,-1):
#     r=i
#     d=1
#     for j in range(1,i+1):
#         print(r,end=" ")
#         r=r-d
#     print()

"""
1
3 2
6 5 4
10 9 8 7
"""

# for i in range(1,5+1):
#     r=i*(i+1)//2
#     for j in range(1,i+1):
#         print(r,end=" ")
#         r=r-1
            
#     print()

"""
      *
    *   *
  *       *
* * * * * * *
"""
for i in range(1,6+1):
    for j in range(1,6-i+1):
        print(end=" ")
    for k in range(1,i+1):
        if i == 6 or k==1 or k==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

