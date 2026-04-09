
# find the largest element from the arrray
# arr=[10,8,5,6,12,14]
# for i in range(len(arr)):
#     for k in range(len(arr)-i-1):
#         if arr[k] > arr[k+1]:
#             pass
#         else:
#             arr[k],arr[k+1] = arr[k+1],arr[k]
# print(arr[0])

# reverse the string
# string="hello"
# s=""
# for ch in string:
#     s=ch+s
# print(s)

# prime
# string=input("Do you need to look for prime numbers: (y/n) :")
# while(True):
#     n=int(input("Enter a number: "))
#     flag=0
#     for i in range(2,n//2+1):
#         if n%i==0:
#             flag=1
#             break
#     if flag==0:
#         print(f"{n} is prime.")
#     else:
#         print(f"{n} is not prime.")
#     s=input("Do you wish to continue, (y/n):")
#     if s.lower() != 'y':
#         break


# count vowels in a string
# count=0
# string=input("Enter a string: ")
# for i in string:
#     if i in "aeiouAEIOU":
#         count=count+1
# print(f"Vowels in {string} are {count}")

# duplicate elements in arry
# arr=[4,4,5,5,7,7,8,8,7]
# a=[]
# for i in arr:
#     if i not in a:
#         a=a+[i]
# print(a)

# occurence of each char

# string=input("Enter a string: ")
# d={}
# for i in string:
#     if i in d:
#         d[i] =d[i]+1
#     else:
#         d[i] = 1
# for m,n in d.items():
    # print(m,":",n)

# occurence of word in a sentence
# sen=input("Enter a sentence: ")
# l=[]
# w=""
# for i in sen:
#     if i != " ":
#         w=w+i
#     else:
#         if w:
#             l=l+[w]
#         w=""
# if w:
#    l.append(w)
# print(l)
# d={}
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i] = 1
# for m,n in d.items():
#     print(m,":",n)

# missing number in array
# n=int(input("Enter the size of the array: "))
# l=[]
# for i in range(n):
#     num=int(input(f"Enter element {i+1}: "))
#     l=l+[num]
# for i in range(len(l)):
#     for k in range(len(l)-i-1):
#         if l[k]>l[k+1]:
#             l[k],l[k+1]=l[k+1],l[k]
# small=l[0]
# big=l[n-1]
# print(small,big)
# for i in range(small,big+1):
#     if i not in l:
#         print(i)

# input="two one seven eight "  output="2178"
# input="double two triple three" output="22333"

# number=input("Enter the phone number in words: (needs 10 digits)")
# word=[]
# space=""
# for i in number:
#     if i != " ":
#         space=space+i
#     else:
#         if space:
#             word=word+[space]
#         space=""
# if word:
#     word=word+[space]
# print(word)
# for i in range(len(word)):
#         if word[i] == "double":
#             word[i] = word[i+1]
#         if word[i] == "triple":
#                word[i]=word[i+1]
#                word=word[:i]+[word[i+1]]+word[i:]

# print(word)
# l=[]
# n=len(word)

# for i in word:
#     match i:
#         case "one": 
#                 l=l+["1"]
#         case "two":
#                 l=l+["2"]
#         case "three":
#                 l=l+["3"]
#         case "four":
#                 l=l+["4"]
#         case "five":
#                 l=l+["5"]
#         case "six":
#                 l=l+["6"]
#         case "seven":
#                 l=l+["7"]
#         case "eight":
#                 l=l+["8"]
#         case "nine":
#                 l=l+["9"]
#         case "zero":
#                 l=l+["0"]
#         case _:
#             print("You entered default value......!")

# print(l)
# num="" 
# for digit in l:
#       num=num+digit
# print(num)

# [[1,2,3],[4,5,6],[7,8,9]]
# list=[[1,2,3],[4,5,6],[7,8,9]]
# n_list=[]
# n=len(list)
# for i in range(n):
#     for j in range(i):
#         list[i][j],list[j][i]=list[j][i],list[i][j]
# print(list)
# new_l=[]
# for i in list:
#     for k in range(len(list)-1,-1,-1):
#         print(i[k],end=" ")
#     print()
# print(list)

# [[1,2,3],[4,5,6],[7,8,9]]
# list=[[1,2,3],[4,5,6],[7,8,9]]
# n_list=[]
# n=len(list)
# for i in range(n):
#     for j in range(i):
#         list[i][j],list[j][i]=list[j][i],list[i][j]
# print(list)
# for i in range(n):
#     list[i].reverse()
# print(list)
c="HHHHHHHHHHHHHHHHHHHHHHHHH"
co=0
for i in c:
    co=co+1
print(co)