class MyClass:  
        # assign the values to the MyClass attributes
        number = 0       
        name = "noname"
  
def Main():
        # Creating an object of the MyClass. 
        # Here, 'me' is the object
        me = MyClass() 
  
        # Accessing the attributes of MyClass
        # using the dot(.) operator   
        me.number = 1337    
        me.name = "Harssh"
  
        # str is an build-in function that 
        # creates an string
        print(me.name + " " + str(me.number))

