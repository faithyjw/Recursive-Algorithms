#library
import turtle

def drawTriangle(points, myTurtle, color):
    myTurtle.fillcolor(color) #drawing with colors
    myTurtle.up()  #Pen up (moving with no ink on screen)
    myTurtle.goto(points[0][0], points[0][1]) #starts drawing at the bottom left (0)
    myTurtle.down()  #Pen down (moving down with no ink on screen)
    myTurtle.begin_fill() #filling the triangle with the colours
    myTurtle.goto(points[1][0], points[1][1]) #top of the triangle (1)
    myTurtle.goto(points[2][0], points[2][1]) #bottom-right of the triangle (2)
    myTurtle.goto(points[0][0], points[0][1]) #bottom-left of the triangle (0)
    myTurtle.end_fill() #finish coloring

def getMid(p1, p2): #find the midpoints of the triangle; p1 = x-coordinate, p2 = y-coordinate
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2) #first half = x-coordinate, second half = y-coordinate

def sierpinski(points, degree, myTurtle):
    colors = ['skyblue', 'lightcoral', 'lightgreen', 'lightcyan', 'lightyellow', 'lightpink', 'lightsalmon']
    
    # Draw a triangle based on the 3 points given
    drawTriangle(points, myTurtle, colors[degree])

    #recursion
    if degree > 0: #base case
        sierpinski([points[0], #bottom left of the triangle
                    getMid(points[0], points[1]), #bottom left and top vertices
                    getMid(points[0], points[2])], #bottom left and bottom right vertices
                    degree - 1, myTurtle) #degree decrement for base case
        sierpinski([points[1], #top of the triangle
                    getMid(points[0], points[1]), 
                    getMid(points[1], points[2])],
                    degree - 1, myTurtle)
        sierpinski([points[2], #bottom right of the triangle
                    getMid(points[2], points[1]), #bottom right and top vertices
                    getMid(points[0], points[2])],
                    degree - 1, myTurtle)

def main():
    myTurtle = turtle.Turtle() #initializing variable
    myTurtle.speed(10)  # adjust the drawing speed here
    myWin = turtle.Screen() #creating window for Turtle
    myWin.bgcolor("gray") #window to have a black background
    #myWin.tracer(0) #see end product without animations

    # 3 points of the first triangle based on [x,y] coordinates
    myPoints = [[-200, -50], [0, 200], [200, -50]]
    degree = 5  # Vary the degree of complexity here; MAX is 6

    # first call of the recursive function
    sierpinski(myPoints, degree, myTurtle)

    myTurtle.hideturtle()  # Hide the turtle cursor after drawing is completed
    myWin.exitonclick()  # Exit program when the user clicks on the window

main() #to run
