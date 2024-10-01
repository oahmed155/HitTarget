#HitTarget.py
#OmarAHmed
#9/26/23
#This launches a turtle at a target and gives feedback about your aim
from turtle import *
import math 
#Initialization Section


speed(1)
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

setup(600,600)
penup()
goto (100,250)
pendown()
setheading (EAST)
forward (25)
setheading (NORTH)
forward (25)
setheading(WEST)
forward (25)
setheading(SOUTH)
forward(25)
penup()
goto(0,0)
setheading(EAST)

#Input Section
angle = float (input("Set launch angle for turtle: "))
#input and convert to float in one step
distance = input ("Enter distance in pixels: ") # input as one step
distance = float(distance) # then float as the second step

pendown()
setheading(angle)
forward(distance)
if xcor() >= 100 and xcor() <= 125 and ycor() >= 250 and ycor() <= 275:
  print("Yay!!! You hit the target!!!")
else:
    print ("Sorry, missed")
mindist = math.sqrt (100*100 + 250*250)
maxdist = math.sqrt (125*125 + 275*275)
if distance < mindist:
  print("Use less force")
  
mintan = 250 / 125 
maxtan = 275/ 100
turtan = ycor() / xcor()
if turtan < mintan:
  print("")
elif turtan > maxtan:
  print("")

x = input("Hit any key to stop")
