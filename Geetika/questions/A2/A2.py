x=int(input("enter radius : "))
def area(radius):                    
   return(3.14*radius*radius)

def peri(radius):
      return(2*3.14*radius)


def sqr (r):
     return( r**0.5)
  


x=int(input("enter radius : "))
print("Area of the circle is : ", area(x))
print("Perimeter of the circle is : ", peri(x))
print("Square root of the radius is : ", sqr(x))