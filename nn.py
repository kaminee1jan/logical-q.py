name=input("enter the string")
i=0
while i<len(name):
    print(name[i],i)
    i=i+1

l=[12,67,98,34]
i=0
list1=[]
while i<len(l):
    modules=l[i]%10
    f_division=l[i]//10
    add=modules+f_division
    list1.append(add)
    i=i+1
print(list1)
print(list1)

dic={
    "x":[11,12,13,14,15,16,17,18,19],
    "y":[21,22,23,20,25,26,27,28,29],
    "z":[30,31,32,33,34,35,36,37,38,39]
}
d={}
user=int(input("enter the number"))
for i in dic.values():
    c=1
    for j in i:
        if c==user:
            print(j)
        c=c+1


    