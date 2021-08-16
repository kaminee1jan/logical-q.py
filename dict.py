import json
d='{"1":"One","2":"Two","3":"Four"}'
json_object = json.loads(d)
print(json_object)
d={1:"One",2:"Two",3:"Three"}   
list1=[]
list2=[]
i=1
while i<=len(d):
    list1.append(i)
    list2.append(d[i])
    i=i+1
print(list2)
print(list1)

import json
d='{"1":"One","2":"Two","3":"Four"}'
json_object = json.loads(d)
print(json_object)
json_object={1:"One",2:"Two",3:"Three"}   
list1=[]
list2=[]
i=1
while i<=len(json_object):
    list1.append(i)
    list2.append(json_object[i])
    i=i+1
print(list2)
print(list1)


# l=["rupali","kaminee","prgna","priya"]
# l1=[]
# l2=[]
# i=0
# while i<len(l):
#     j=0
#     while j<len(l):
#         k=0
#         while k<len(l):
#             if l[k]==l[i]:
#                 l1.append(l1[j])
#                 l1.append(l1[k])
#             k=k+1
#         j=j+1
#     i=i+1
# print(l1)