# sets - {} 
# unordered, unique elements
a={12,15,19,32,'hello',True,9.98,100,15,19,32,12}
print(a)
print(type(a))
# i={}
i=set()
print(type(i))

# methods 
#pop, remove, discard 
# print(a)  
# a.pop()
# print(a)

# a.remove(100) #Remove an element from a set; it must be a member
# print(a)

# a.discard(19) #Remove an element from a set if it is a member.
# print(a)


a.update({4,5,6,12}) # Update a set with the union of itself and others.
print(a)

# a.add(10) #Add an element to a set.
# a.add(1) #Add an element to a set.
# print(a)


i={12,13,14,15,1}
j={13,15,19,30,True}

print(i.union(j))
print(j.union(i))
print(i.intersection(j))
print(j.intersection(i))

