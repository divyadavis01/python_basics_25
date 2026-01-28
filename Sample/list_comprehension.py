num=[1,2,3,4,5,6,7]
print([f"{n} is even" for n in num if n%2==0])

name=["Anna","Biya","Cia","Ann"]
new_Name=[f for f in name if f.startswith("A")]
print(new_Name)

newname=[f for f in name if "A" in f and "a" in f]
print(newname)

# zip


a=[1,2,"Three"]
b=[[1,2],"hello",4]
c=["hai",4,7]

print(list(zip(a,b)))

for k in zip(a,b):
    print(k)

zipped_data = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
names, grades = zip(*zipped_data)
names = list(names)
grades = list(grades)
print(names) 
print(grades) 