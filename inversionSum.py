# def inversionSum(N,A):
#     product =1
#     for x in range(N):
#         product=product*A[x]
#     inv_count = 0
#     for i in range(N):
#         for j in range(i + 1, N):
#             if (A[i] > A[j]):
#                 inv_count += 1
#     return product*(inv_count)



# print(inversionSum(6,[2,1,3,4,6,5]))

# def fun1(N,A):
#     # arrsort = A.sort()
#     print(N)
#     print(A)
#     print(A.sort())
# fun1(6,[2,1,3,4,6,5])

def findId(N,M):
    for x in range(N):
        if 1 not in M[x]:
            return (x)
        
print(findId(3,[[0,1,0],[0,0,0],[0,1,0]]))
