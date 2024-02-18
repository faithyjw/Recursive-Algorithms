#Name: Faith Yeo
#Admin No.: 230859Q
#Tutorial Group: 01

#Question: 3A) SYMMETRICAL/BALANCED PYTHAGORAS TREE

#libraries
import turtle
import math

def drawSquare(t, size, color):
  t.begin_fill() #filling the shapes with the colors
  t.fillcolor(color) #drawing with colors
  for i in range(4): #square = 4 sides so iterates over the 4 sides
    t.forward(size) #moves forward
    t.left(90) #turn left by 90 degree
  t.end_fill() #finish coloring

def drawTriangle(t,size,innerColor):
    #drawing external EQUILATERAL triangles
    t.begin_fill() #filling the shapes with the colors
    t.fillcolor(innerColor) #drawing with colors inside the triangle
    for i in range(3): #triangle = 3 sides so iterates over the 3 sides
      t.forward(size /math.sqrt(2)) #moves forward with the pythagoras formula
      t.left(120) #turn left by 120 degrees
    t.end_fill() #finish coloring

def drawNode(t, size, level, outerColor, innerColor): #function(object, size, recursion level(degree), outer color, inner color)
  #recursion
  if (level < 1): #base case
    return
  else:
    drawSquare(t, size, outerColor)

    #drawing the tree's LEFT branch
    leftSize = math.sqrt(size * size / 2) #pythagoras formula for balanced tree
    t.forward(size) #moves forward
    t.left(90) #turn left by 90 degree
    t.forward(size) #moves forward
    t.right(135) # if left-side angle is 45 degrees, this angle is 180-45=135
    t.forward(leftSize) #move forward with the pythagoras formula
    t.left(90) #turn left by 90 degree
    
    drawTriangle(t,size,innerColor)

    drawNode(t, leftSize, level - 1, outerColor, innerColor) #level decrement for base case

    #drawing the tree's RIGHT branch
    rightSize = math.sqrt(size * size / 2) #pythagoras formula for balanced tree
    t.right(180) #turns right by 180 degree
    t.forward(rightSize) #move forward with the pythagoras forumla
    t.left(90) #turns left by 90 degree

    drawTriangle(t,size,innerColor)

    drawNode(t, rightSize, level - 1, outerColor, innerColor) #level decrement for base case

    #if right-side angle is 45 degrees, this angle is = 45
    t.left(45) #turns left by 45 degree; adjusting turtle's orientation 
    t.back(size) #moving backward with the distance equal to the parameter

def main():
  screen = turtle.Screen() #creating window for Turtle
  screen.bgcolor("lightblue") #window to have a light blue background
  #screen.tracer(0) #see end product without animations
  
  myTurtle = turtle.Turtle() #initializing variable
  # myTurtle.shape("turtle") #cursor shape
  # myTurtle.color("black") #shapes' outline color
  # myTurtle.fillcolor("pink") #shapes' color
  myTurtle.speed(0) #speed of the drawing

  myTurtle.penup() #Pen up (moving with no ink on screen)
  myTurtle.goto(30, -150) #coordinates at which it will start drawing at
  myTurtle.left(90) #turn left by 90 degree
  myTurtle.pendown() #Pen down (moving down with no ink on screen)

  drawNode(myTurtle, 80, 8, "pink", "lightgreen") #function(object, size, recursion level(degree), outer color, inner color)
  #level 14:
  #drawNode(myTurtle, 100, 14, "pink", "lightgreen")

  myTurtle.hideturtle() #hide the turtle cursor after drawing is completed
  screen.exitonclick() #exit program when the user clicks on the window

main() #to run