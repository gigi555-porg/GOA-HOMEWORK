from turtle import * 

#we want to paint a house  

#step 1:  draw  a square 

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
forward(70)
color("brown")
begin_fill()
left(90)
forward(75)
right(90)
forward(60)
right(90)
forward(75)
end_fill()


penup()
goto(200, 200)
pendown()


color("green")
begin_fill()
right(140)
forward(157)
left(100)
forward(157)
end_fill()


penup()
goto(130, 130)
pendown()


color("black")
begin_fill()
left(41)
forward(20)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
end_fill()


penup()
goto(45, 110)
pendown()


color("black")
begin_fill()
left(90)
forward(20)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
left(90)
forward(55)
end_fill()


exitonclick() 