
from itertools import cycle
colorList =['yellow', 'green', 'red', 'cyan', 'white', 'blue',
           'mediumpurple', 'aquamarine3', 'brown', 'coral',
           'pink','maroon']
colorCycle = cycle(colorList)

userPercentages = []

def user_input():
    numberSlices = int(input("How many proportions does your pie chart has? Answer: "))
    # below conditional statement helps avoid 2 consecutive sections from having the same color
    if numberSlices % 12 == 1:
        colorList.append("gray")
    while len(userPercentages) < numberSlices :
        percentages = float(input("Please input the proportion : "))
        userPercentages.append(percentages)     #append the ipnut data to the list
    return userPercentages
'''the below lines of code were an attempt to solve the problem if the user 
dont use 100 as a sum. However, it is not possible as it seems, so I changed my way.'''
#        sum_percent = 0
#        for item in userPercentages:
#            sum_percent += item
#            if sum_percent > 100:
#                print("Sorry, your sum of percentages exceeds 100%. Please try again!")
#                user_input()

user_input()

sumItem = 0
for item in userPercentages:        #calculated the sum of input data to calculate the relative fraction
    sumItem += item

import turtle              #found out that the program would crash if turtle were imported prior to using
nina = turtle.Turtle()
nina.pensize(0.1)
nina.pencolor('black')
nina.speed(10)
radius = 200
label_radius = radius * 0.5
nina.sety(-radius)

jem = turtle.Screen()
jem.bgcolor('MistyRose')
def draw_pie():
    for item in userPercentages:
        percent = (item / sumItem)*360      #convert fraction of a section/sum -> degrees, since a circle has 360 degrees
        nina.fillcolor(next(colorCycle))    #select the next color in the list for the next segment
        nina.begin_fill()
        nina.circle(radius, percent)        #draw a circle whose radius is 200 and draw each angle one by one
        pos = nina.position()               #identify the last position of the turle on the circumference
        nina.goto(0,0)                      #move turtle back to the center to complete a segment
        nina.end_fill()
        nina.setposition(pos)               #move turtle to the last position on the circumference -> keep on drawing
draw_pie()

proportion_list = []
for item in userPercentages:
    item = (item / sumItem)
    proportion_list.append(item)

nina.penup()
nina.sety(-label_radius)

def draw_labels():
    for label in proportion_list:
        nina.circle(label_radius, (label/ 2)*360)
        label = round(label, 2)
        for label in proportion_list:
            label = '{:.2%}'.format(label)
            nina.write(label, align="center", font=("Candara", 11, "normal"))
        nina.circle(label_radius, (label / 2)*360)
draw_labels()
nina.hideturtle()

jem.exitonclick()




