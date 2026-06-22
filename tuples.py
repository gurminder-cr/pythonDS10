# heterogenous elements, ordered or indexed,immutable(cannot change during runtime)
# ()
a=(12,14,'hi',7.87,True)
print(a)
n=(12,14,16)
print(n)
print(type(n))

k=(10,)
print(k)
print(type(k))
# 12, 14, 'hi', 7.87, True
# slicing 
print(a[1])
print(a[:])
print(a[:3])
print(a[1:5])
print(a[1:9])

# a[2]=100
a=list(a)
# print(a)
a[2]=100
a=tuple(a)
print(a)


j=["hello","Class","how","are","you"]
# sum(j)

print("_".join(j))

