# for i in range(1,10):
#     print(i)

# for i in range(1,10,3):
#     print(i)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

#finding prime number
a= int(input("enter a  number"))
c=0;
for i in range(1,a+1):
   if(a%i==0):
      c=c+1;
if(c==2):
   print("prime number")
else:
   print("its not a prime number");
   