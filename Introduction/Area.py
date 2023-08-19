shape = input("Enter any shape to find its area:")

if shape == "Square":
  side= float(input("Enter the side of square:"))
  square = side**2
  print(square,"is the area of square")

elif shape == "Rectangle":
  length= float(input("Enter the length of rectangle:"))
  width= float(input("Enter the width of rectangle:"))
  rectangle = length*width
  print(rectangle,"is the area of rectangle")

elif shape == "Circle":
  radius= float(input("Enter the radius of the circle:"))
  pi= 22/7
  circle  = pi*radius**2
  print(circle,"is the area of circle")
  
elif shape == "Parallelogram":
  base= float(input("Enter the base of the parallelogram:"))
  height= float(input("Enter the height of the parallelogram:"))
  parallelogram  = height*base
  print(parallelogram,"is the area of parallelogram")

elif shape == "Trapezium":
  base1= float(input("Enter the base of the trapezium:"))
  base2= float(input("Enter the base of the trapezium:"))
  height1= float(input("Enter the height of the trapezium:"))
  trapezium = ((base1+base2)/2)*height1
  print(trapezium,"is the area of trapezium")

elif shape == "Sphere":
  radius= float(input("Enter the radius of the sphere:"))
  pi= 22/7
  sphere  = 4*pi*radius**2
  print(sphere,"is the area of sphere")