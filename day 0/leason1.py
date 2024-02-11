from turtle import*


#we want to paint a house

#step1: draw aspuare 
speed(5)
width(7)
color("red")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200) 
left(90)
#end of square

#drawing of door

forward(100)
color("gray")
begin_fill()
left(90)
forward(62)
right(90)
color("black")
forward(10)
left(180)
forward(10)
right(90)
color("gray")
forward(62)
right(90)
forward(60)
right(90)
forward(125)
end_fill()
#end of door

#start of roof
penup()
goto(200, 200)
pendown()

color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof

#start of window
color("red")
pendown()
goto(0, 160)

color("white")
goto(15, 160)

color("red")
left(120)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(60)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(60)

exitonclick()