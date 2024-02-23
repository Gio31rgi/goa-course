from turtle import*


#we want to paint a house

#step1: draw aspuare 
speed(15)
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
left(90)
forward(30)
left(90)
forward(60)
color("white")
forward(15)
color("red") 
left(90)
forward(160)
right(90)
#end of window

#start of tree
color("green")
forward(250)
left(180)
forward(37)
left(90)

color("brown")
begin_fill()
forward(155)
right(90)
forward(18)
right(90)
forward(155)
end_fill() 

right(180)
forward(155)
color("green")
begin_fill()
right(85)
circle(90)
end_fill()
#end of tree

#start of sun
color("brown")
right(100)
forward(155)
left(95)
color("green")
forward(209)
color("red")
forward(200)
color("white")
forward(185)
color("red")
left(90)
color("white")
forward(300)
left(90)
forward(40)
right(90)
color("orange")
begin_fill()
circle(60)
end_fill()



exitonclick()