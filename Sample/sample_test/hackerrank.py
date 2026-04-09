"""
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12





m=int(input())
n=set(map(int,input().split()))
o=int(input())
p=set(map(int,input().split()))
r=n.difference(p)
l=[]
for i in sorted(r):
    l=l+[i]
re=p.difference(n)
for i in sorted(re):
    l=l+[i]
for i in sorted(l):
    print(i)
"""


"""
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain 1 unit of happiness for elements 3 and 1 in set . You lose 1 unit for 5 in set . The element 7 in set B does not exist in the array so it is not included in the calculation.

Hence, the total happiness is 2-1=1.




# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
m=list(map(int,input().split()))
o=set(map(int,input().split()))
p=set(map(int,input().split()))
# print(n,m,o,p)

happiness=0
for i in m:
    if i in o:
        happiness=happiness+1
    if i in p:
        happiness=happiness-1
print(happiness)
"""



"""
7 countries "uk","france","germany","italy","canada","uk","france" in a set 

output =5


s=set()
for i in countries:
   use add method
find len of s

"""




"""
Task

You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer , the number of elements in the set .
The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer , the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.

Constraints



Output Format

Print the sum of the elements of set  on a single line.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output

4
Explanation

After completing these  operations on the set, we get set. Hence, the sum is .

Note: Convert the elements of set s to integers while you are assigning them. 
To ensure the proper input of the set, we have added the first two lines of code to the editor.


n = int(input())
s = set(map(int, input().split()))

m=int(input())
for _ in range(m):
    cmd=input().split()
    if cmd[0]=="pop":
        s.pop()
    elif cmd[0]=="remove":
        s.remove(int(cmd[1]))
    elif cmd[0]=="discard":
        s.discard(int(cmd[1]))
print(sum(s))
"""