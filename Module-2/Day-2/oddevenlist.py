# a=[1,2,3,4,5,6]
# even_list=[]
# odd_list=[]
# for element in a:
#         if element % 2 == 0:
#           even_list.append(element)
#         else:
#             odd_list.append(element)
  
# print(even_list)
# print(odd_list)


# list comprehension technique
# very very important
a=[1,2,3,4,5,6] 
# c=[element+2 for element in a]
# print(c)

result=[element for element in a if element%2==0]
print(result)
