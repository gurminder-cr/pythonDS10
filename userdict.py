# user input in dictionary 
l=[{"name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },]
def addValues():
    mname=input("Enter Movie Name ")
    time=int(input("Enter time in minutes "))
    year=int(input("Enter Year "))
    genres=[]
    for i in range(0,5):
        j=input("Enter Genres")
        genres.append(j)
        k=input("Do you want to add gen yes/no ")
        if k=="yes":
            continue
        else:
            break            
    l.append({'name':mname,'year':year,'duration':time,'genres':genres})
addValues() 


print(l)
    
