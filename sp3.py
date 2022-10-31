class Vector2D:
        x = 0.0
        y = 0.0
  
        # Creating a method named Set
        def Set(self, x, y):     
                self.x = x
                self.y = y
  
def Main():
        # vec is an object of class Vector2D
        vec = Vector2D()   
         
        # Passing values to the function Set
        # by using dot(.) operator.
        vec.Set(5, 6)       
        print("X: " + str(vec.x) + ", Y: " + str(vec.y))
  
if __name__=='__main__':
        Main()

