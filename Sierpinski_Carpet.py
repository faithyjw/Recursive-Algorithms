#Name: Faith Yeo
#Admin No.: 230859Q
#Tutorial Group: 01

#Question: 1B) SIERPINSKI CARPET

#library
import turtle

def drawSquare(points, myTurtle, color):
    myTurtle.fillcolor(color) #drawing with colors
    myTurtle.up()  #Pen up (moving with no ink on screen)
    myTurtle.goto(points[0][0], points[0][1]) #starts drawing at the bottom left
    myTurtle.down()  #Pen down (moving down with no ink on screen)
    myTurtle.begin_fill() #filling the square with the colours
    myTurtle.goto(points[1][0], points[1][1]) #top-left of the square
    myTurtle.goto(points[2][0], points[2][1]) #top-right of the square
    myTurtle.goto(points[3][0], points[3][1]) #bottom-right of the square
    myTurtle.goto(points[0][0], points[0][1]) #bottom-left of the square
    myTurtle.end_fill() #finish coloring

def getMid(p1, p2, v, h): #find the midpoints of the square; p1 = x-coordinate, p2 = y-coordinate, v = vertical, h = horizontal
    x1, y1 = p1 #initializing x1 and y1 into p1
    x2, y2 = p2 #initializing x2 and y2 into p2
    x3 = x1 + v/3 * (x2 - x1) #new/x3 midpoint of x-coordinate
    y3 = y1 + h/3 * (y2 - y1) #new/y3 midpoint of y-coordinate
    return x3, y3 #returning variables

def sierpinski(points, degree, myTurtle):
    colors = ['skyblue', 'lightcoral', 'lightgreen', 'lightcyan', 'lightyellow', 'lightpink', 'lightsalmon']
    
    # Draw a triangle based on the 3 points given
    drawSquare(points, myTurtle, colors[degree])

    #recursion
    if degree > 0: #base case
        sierpinski([ #first-row left square
                getMid(points[0], points[2], 0, 0), #bottom left vertex
                getMid(points[0], points[2], 0, 1), #bottom right vertex
                getMid(points[0], points[2], 1, 1), #top right vertex
                getMid(points[0], points[2], 1, 0) #top left vertex
               ], degree-1, myTurtle) #degree decrement for base case

        sierpinski([ #second-row left square
                getMid(points[0], points[2], 0, 1),
                getMid(points[0], points[2], 0, 2),
                getMid(points[0], points[2], 1, 2),
                getMid(points[0], points[2], 1, 1)
               ], degree-1, myTurtle)

        sierpinski([ #third-row left square
                getMid(points[0], points[2], 0, 2),
                getMid(points[0], points[2], 0, 3),
                getMid(points[0], points[2], 1, 3),
                getMid(points[0], points[2], 1, 2)
               ], degree-1, myTurtle)

        sierpinski([ #third-row middle square
                getMid(points[0], points[2], 1, 2),
                getMid(points[0], points[2], 1, 3),
                getMid(points[0], points[2], 2, 3),
                getMid(points[0], points[2], 2, 2)
               ], degree-1, myTurtle)

        sierpinski([ #third-row right square
                getMid(points[0], points[2], 2, 2),
                getMid(points[0], points[2], 2, 3),
                getMid(points[0], points[2], 3, 3),
                getMid(points[0], points[2], 3, 2)
               ], degree-1, myTurtle)

        sierpinski([ #second-row right square
                getMid(points[0], points[2], 2, 1),
                getMid(points[0], points[2], 2, 2),
                getMid(points[0], points[2], 3, 2),
                getMid(points[0], points[2], 3, 1)
               ], degree-1, myTurtle)

        sierpinski([ #first-row right square
                getMid(points[0], points[2], 2, 0),
                getMid(points[0], points[2], 2, 1),
                getMid(points[0], points[2], 3, 1),
                getMid(points[0], points[2], 3, 0)
               ], degree-1, myTurtle)

        sierpinski([ #first-row left square
                getMid(points[0], points[2], 1, 0),
                getMid(points[0], points[2], 1, 1),
                getMid(points[0], points[2], 2, 1),
                getMid(points[0], points[2], 2, 0)
               ], degree-1, myTurtle)

def main():
    myTurtle = turtle.Turtle() #initializing variable
    myTurtle.speed(10)  # adjust the drawing speed here
    myWin = turtle.Screen() #creating window for Turtle
    myWin.bgcolor("black") #window to have a black background
    myWin.tracer(0) #see end product without animations

    # 4 points of the first triangle based on [x,y] coordinates
    myPoints = [[-200, -200], [-200, 200], [200, 200], [200, -200]]
    degree = 4  # Vary the degree of complexity here; MAX is 6

    # first call of the recursive function
    sierpinski(myPoints, degree, myTurtle)

    myTurtle.hideturtle()  # Hide the turtle cursor after drawing is completed
    myWin.exitonclick()  # Exit program when the user clicks on the window

main() #to run