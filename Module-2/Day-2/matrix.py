# A=[[2,3,4],[3,4,5],[5,6,7]]
# B=[[2,3,4],[3,4,5],[5,6,7]]
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]


# for i in range(3):
#    # iterate through columns
#     for j in range(3):
#          result[i][j] = A[i][j] + B[i][j]

# print(result)
# result[1][1]=True
# print(result)


# print(A[1])
# print(A[1][1])

A=[5,6,7]
temp=A[0]
for element in A:
    if element>temp:
        temp=element
    max_value=temp
print(max_value)
    




