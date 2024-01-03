#addition 
def addition (x,y,z):
    return x+y+z 
    print (x+y+z)

#subtraction  
def subtraction (x,y,z): 
    return x-y-z
    print (x-y-z)

#Multilpication 
def multilpication (x,y,z) : 
    return x*y*z
    print (z*y*z)

#Division 
def division (x,y): 
    return x/y
    print (x/y)


class Person : 
    def __init__ (self, name, Age) : 
        self.name = name 
        self.Age = Age 

    def display (self) : 
        print (f"Name : {self.name} and Age is : {self.Age}")