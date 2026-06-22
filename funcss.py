# functions - user defined and pre-defined 
# pre-defined - input, print, sum, ..... lower(), upper() 
# user defined functions - def 
def func1():
    print("Hello")

# func1()

def myfunc(a,b):  # parameters  
    print(a+b)

# myfunc(10,14)  # arguments 
# i=int(input("i "))
# j=int(input("j "))
# myfunc(i,j)
# i=int(input("i "))
# j=int(input("j "))

# def myFunc1(a,b,c):
#     # print(a+b+c)
#     return a+b+c
#     # print('hi')
    
# # print(myFunc1(12,13,14))
# ans=myFunc1(12,13,14)
# # print(ans)



# function with default parameter 

# def defaultFunc(a,c,b=10):
#     print(a*b)
    
# defaultFunc(12,20)


#keyword arguments 

# def keyArgs(a,b,c):
#     print(a,b,c)

# # i=10
# # j=20
# # k=30
# keyArgs(c=10,b=20,a=30)


l=[12,13,19,44,32,33]
# print(sum(l))

def listSum(a):
    # print(a)
    s=0 
    for i in l:
        s+=i
    return s

print(listSum(l))


def oddEven(i):
    if i%2==0:
        return "Even"
    else:
        return "Odd"
n=int(input("Enter num "))
print(oddEven(n))