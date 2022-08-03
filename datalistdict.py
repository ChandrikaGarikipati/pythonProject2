My_details=(("name",'chandrika'),("ID",'2100031842'))
output_details=dict((key,value)for key,value in My_details)
print(output_details)
list1=[1,2,3,4]
list2=['a','b','c','d']
output1=dict({y:y*y for y in list1})
output=dict((zip(list2,list1)))
print(output1)
print(output)