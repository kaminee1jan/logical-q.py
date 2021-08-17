list1 = [-1,3,4,87,-7,5]
i = 0
while i < len(list1):
    j = 0 
    while j < len(list1):
        if list1[i] < list1[j]:
            a = list1[i]
            b = list1[j]
            list1[i] = b
            list1[j] = a
        j = j + 1
    i = i + 1
print(list1)




n=[2,11,7,15]
i=0
b=[]
while i<len(n):
    j=i
    while j<len(n):
        if n[i]+n[j]==9:
            b.append(i)
            b.append(j)
        j=j+1
    i=i+1
print(b)

