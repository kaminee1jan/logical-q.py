# def check_space(string):
#     count = 0
#     i=0
#     while i<len(string):
#         if string[i] == " ":
#             count=count+1
#         i=i+1
#     return count
# string = input("enter the string,,,,,,,,")
# print("number of spaces ",check_space(string))

list1=[10,11,12,13,14,17,18,19]
num=30
i=0
empty=[]
while i<len(list1):
    j=i
    empty1=[]
    while j<len(list1):
        if list1[i]+list1[j]==num:
            empty1.append (list1[i])
            empty1.append(list1[j])
            empty.append(empty1)
        j=j+1

    i=i+1
print(empty)            
