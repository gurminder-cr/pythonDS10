# text,json 
# file handling - with, open 
# mode - r, w, a, r+, w+, x 
# with open('t.txt','r') as f:
#     print(f.read())
# with open('t.txt','w') as f:
#     f.write("Hello Guys")

# with open('t.txt','a') as f:
#     f.write(" Jaskaran")
    

# with open('file.txt','x') as f:
#     f.write("hi")

# with open('file.txt','r+') as f:
#     print(f.read())
#     f.seek(3)
#     f.write("Hello Class")

with open('file.txt','w+') as f:
    f.write("Hello Class")
    f.seek(0)
    print(f.read())