class person : 
    name : str
    age : int
    def __init__ (self , name1,  age1):
        name = name1 
        age = age1

p = person("jack" , 70)


p.__dict__["city"]="Boston"

print(p.city)

print (p.__dict__)