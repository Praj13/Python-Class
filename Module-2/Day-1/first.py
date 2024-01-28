#list
a=[1,2,3,4,5,"hello",5,True]
print(type(a))

#tuple
b=(1,2,3,4,5,"hello",True)
print(type(b))

print(a[3])
print(a[-3])

#append means adding
a.append("hi")
print(a)
print(a[-1])

#removing element from last index
a.pop()
print(a)

#prints index of the hello
print(a.index("hello"))


# 5 khoj 5 index paxi  
print(a.index(5,5))


#bich maa element append garna
a.insert(7,"sameer")
print(a)

a.insert(4,"hritik")
print(a)

a.insert(4,"bhhupen")
a.insert(a.index(4),"bhhupendra")
a.insert(a.index(4),"don")


#removes element of index 3
a.remove(4)

# a.reverse()

#slicing
print(a)
b=a[1:6]
c=a[1:-1]
e=a[4:]
f=a[:9:2]



print(a)

a[::-1]
print(a)
print(len(a))
# h=a[1::2]
# print(h)


# to count the number of particular element
print(a.count(5))

sor=[3,2,1,4,22]
sor.sort()
print(sor)




