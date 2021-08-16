import json
a=open("council.txt","w")
a.write(" Disco Kaminee \n T&P Shireen \n HC Himani \n IT Riya \n FM S khan")
a.close()
a=open("council.txt","r")
a1=a.read()
b=a1.split("\n")
dict1={}
for i in b:
    i.split()
    c=i.split()
    if len(c)==2:
        dict1[c[0]]=c[1]
    if len(c)>2:
        j=1
        k=" "
        while j<len(c):
            k+=c[j]
            j+=1
            k+=" "
        dict1[c[0]]=k
print(dict1)
a.close()
c=open("council.json","w")
json.dump(dict1,c,indent=4)
c.close()