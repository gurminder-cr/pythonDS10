# functions

# def sumall(a,b):
#     print(a+b)

# arbitrary arguments - *args - args - any variable name
# def sumall(*a):
#     # print(a)
#     s=0
#     for i in a:
#         s+=i 
#     print(s)

# sumall(12,13)
# sumall(12,13,15)
# sumall(12,13,15,11)
# sumall(12,13,15,11,45)

# keyword arbitrary arguments - **kwargs 
# def keywordArgs(a,b):
#     print(a,b)
# def keywordArgs(**a):
#     print(a)

# keywordArgs(a=10,b=20)
# keywordArgs(a=10,b=20,c=34)
# keywordArgs(a=10,b=20,c=34,d=44)


# lambda functions - anonymous, single line function
# syntax -  a=lambda paramters: statement 
# l= lambda a,b: print(a+b)
# l= lambda a,b: a+b
# print(l(12,13))
# def oddEven(i):
#     if i%2==0:
#         return "Even"
#     else:
#         return "Odd"
# n=int(input("Enter num "))
# print(oddEven(n))
# oddEven = lambda i:"Even" if i%2==0 else "Odd"
# print(oddEven(23))


# map 
l=[23,45,33,21,10,14]
# def func1(a):
#     return a+2
# k= map(lambda a:a+2, l)
# print(k)
# print(list(k)) 

# h=map(lambda a,b:a+b, [1,2,3,4],[4,3,5,6])
# print(tuple(h))


# Enumerate function 
l=[1,2,3,2,4,5]
# for i in l:
#     print(i)
# for i in range(len(l)):
#     print(i, l[i])

# for i in enumerate(l):
#     print(i)
for i,j in enumerate(l):
    print(i,"-",j)
    

d={'name':'jaskaran','class':'btech','rollno':12,'isownapet':True} 
for i,j in enumerate(d.items()):
    print(i,"-",j)


print("Hello")