# # dictionary - {} key:value,
d={'name':'jaskaran','class':'btech','rollno':12,'isownapet':True} 

# print(d)
# print(type(d))


# print(d['class'])
# print(d['name'])
# # print(d['names'])

# print(d.get('names','key not present'))

# d.pop('rollno')
# print(d)

# # add 
# d.update(hobby='gaming')
# print(d)

# d['marks']=100
# print(d)

# d['class']='btech CSE'
# print(d)


# print(d.keys())
# print(d.items())
# print(d.values())


# for i,j in d.items():
#     print(i,"--",j)
    
    
# # dictionary comprehension
print(d)
print({j:i for i,j in d.items()})