list1=[20,43,33,65,74,35]
list2=[82,24,51,32,79,12]
combined_list=list1+list2
even_list=[]
odd_list=[]
for i in combined_list:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
mergedlist=even_list+odd_list
print("list1",list1)
print("list2",list2)
print("combined_list",combined_list)
print("mergedlist",mergedlist)
