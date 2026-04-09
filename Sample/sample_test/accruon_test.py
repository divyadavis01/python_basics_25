# inventory=[(1,"Laptop",10),(2,"Mouse",50),(3,"keyboard",30)]
# orders=[(101,"Laptop",2),(102,"Mouse",5),(103,"Laptop",1),(104,"Keyboard",3),(105,"Mouse",5)]
# 1
# l=[]
# for i in orders:
#     products_list=i[1]
#     l=l+[products_list]
# ls=set(l)
# print(f"Unique product = {ls}")

# dic={}
# for i in range(len(orders)):
#     word = orders[i][1]
#     qty=orders[i][2]
#     if word in dic:
#         dic[word] = dic[word]+qty
#         # print(dic[word]," and ", qty)
#     else:
#         dic[word] = qty
#         # print(dic[word]," and ", qty)

# for m,n in dic.items():
#     print(m,":",n)

     
#3
# inv_list=[list(item) for item in inventory]
# new=[5,7,10]
# print(inv_list)
# for i,list in enumerate(inv_list):
#     inv_list[i][2]=new[i]
# print(inv_list)
# inve=[tuple(items) for items in inv_list]
# print(inve)

# 4
# orders=[(101,"Laptop",2),(102,"Mouse",5),(103,"Laptop",1),(104,"Keyboard",3),(105,"Mouse",5)]
# new_dict={}
# new=[]
# for i in range(len(orders)):
#     word=orders[i][1]
#     times=0
#     if word in new_dict:
#         new_dict[word]=new_dict[word]+1
#     else:
#         new_dict[word]=1
# for m,n in new_dict.items():
#     if n > 1:
#         new=new+[m]
# print(new)

#5
# inventory=[(1,"Laptop",7),(2,"Mouse",40),(3,"Keyboard",27)]
# for i in range(len(inventory)):
#     print(len(inventory))
#     print(len(inventory)-i-1)
#     for k in range(len(inventory)-i-1):
#         if inventory[k][2]>inventory[k+1][2]:
#             inventory[k],inventory[k+1]=inventory[k+1],inventory[k]
# print(inventory)          

#6
# inventory=[(1,"Laptop",7),(2,"Mouse",40),(3,"Keyboard",27)]
# inv=[list(item) for item in inventory]
# lowest_inv=[]
# for i in range(len(inv)):
#     for k in range(len(inv)-i-1):
#         if inv[k][2]>inv[k+1][2]:
#             inv[k][2],inv[k+1][2] = inv[k+1][2],inv[k][2]
#         else:
#             lowest_inv=inv[k]
# print(lowest_inv)





"""
[[1,0,0],[0,1,0],[1,1,0]]

1 0 0
0 1 0 
1 1 0


90 degree

1 0 1
1 1 0
0 0 0

"""

l=[[1,0,0],[0,1,0],[1,1,0]]
new_list=[]
size=len(l)
c=0
while c<size:
    nested_list=[]
    for r in range(2,-1,-1):
        nested_list.append(l[r][c])
    new_list.append(nested_list)
    c+=1

print(new_list)
for i in new_list:
    print(i)