# list comprehension 
# l=[]
# for i in range(0,20):
    # if i%2==0:
#       l.append(i)
# print(l)

# l=[i for i in range(0,20)]
# l=[i for i in range(0,20) if i%2==0]
# print(l)

# p=[32,22,10,15,19,20,25,78,100]
# p=[i+2 for i in p]
# print(p)


# p=[i if i%3==0 else i**2 for i in range(1,25)]
# print(p)

a=[12,13,15,6,7]
b=[4,5,6,7,10]

# for i in a:
#     for j in b :
#         if i==j:
#             print(i)
# for i in a:
#     if i in b:
#             print(i)

# k=[i for i in a for j in b if i==j]
k=[(i,i) for i in a if i in b]
print(k)
