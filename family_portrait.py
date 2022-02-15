
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n8882959
#    Student name: Joseph Urban
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  MY STRETCHY FAMILY
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_portrait".
#  You are required to complete this function so that when the
#  program is run it produces a portrait of a stick figure family in
#  the style of the car window stickers that have become popular in
#  recent years, using data stored in a list to determine the
#  locations and heights of the figures.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  only your final solution, whether or not you complete both
#  parts.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for drawing the background.  You should not change any
# of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to import any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

window_height = 550 # pixels
window_width = 900 # pixels
grass_height = 200 # pixels
grass_offset = -100 # pixels
location_width = 150 # pixels
num_locations = 5

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background and the locations where the individuals in the
# portrait are required to stand.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up.
#


# Draw the grass as a big green rectangle
def draw_grass():
    
    penup()
    goto(-window_width / 2, grass_offset) # start at the bottom-left
    setheading(90) # face north
    fillcolor('pale green')
    begin_fill()
    forward(grass_height)
    right(90) # face east
    forward(window_width)
    right(90) # face south
    forward(grass_height)
    right(90) # face west
    forward(window_width)
    end_fill()


# Draw the locations where the individuals must stand
def draw_locations(locations_on = True):

    # Only draw the locations if the argument is True
    if locations_on:

        # Define a small gap at each end of each location
        gap_size = 5 # pixels
        location_width_less_gaps = location_width - (gap_size * 2) # pixels

        # Start at the far left, facing east
        penup()
        goto(-num_locations * location_width / 2, 0)
        setheading(0) 
  
        # Draw each location as a thick line with a gap at each end
        color('dark khaki')
        for location in range(num_locations):
            penup()
            forward(gap_size)
            pendown()
            width(5) # draw a thick line
            forward(location_width_less_gaps)
            width(1)
            penup()
            forward(gap_size)


# Draw the numeric labels on the locations
def draw_labels(labels_on = True):

    # Only draw the labels if the argument is True
    if labels_on:
    
        font_size = 16 # size of characters for the labels

        # Start in the middle of the left-hand location, facing east
        penup()
        goto(-((num_locations - 1) * location_width) / 2,
             -font_size * 2)
        setheading(0) 

        # Walk to the right, print the labels as we go
        color('dark khaki')
        for label in range(num_locations):
            write(label, font = ('Arial', font_size, 'bold'))
            forward(location_width)


# As a debugging aid, mark certain absolute coordinates on the canvas
def mark_coords(marks_on = True):

    # Only mark the coordinates if the argument is True
    if marks_on:

        # Mark the "home" coordinate
        home()
        width(1)
        color('black')
        dot(3)
        write('0, 0', font = ('Arial', 10, 'normal'))

        # Mark the centre point of each individual's location
        max_x = (num_locations - 1) * location_width / 2
        penup()
        for x_coord in range(-max_x, max_x + location_width, location_width):
            for y_coord in [0, 400]:
                goto(x_coord, y_coord)
                dot(3)
                write(str(x_coord) + ', ' + str(y_coord),
                      font = ('Arial', 10, 'normal'))
                
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the positions for
# the people in the portrait:
#
# 1. The name of the individual, from 'Person A' to 'Person D' or 'Pet'
# 2. The place where that person/pet must stand, from location 0 to 4
# 3. How much to stretch the person/pet vertically, from 0.5 to 1.5
#    times their normal height
# 4. A mystery value, either '*' or '-', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily include all people and sometimes
# they require the same person to be drawn more than once.  You
# can assume, however, that they never put more than one person in
# the same location.
#
# You may add additional data sets but you may not change any of the
# given data sets below.
#

# The following data set doesn't require drawing any people at
# all.  You may find it useful as a dummy argument when you
# first start developing your "draw_portrait" function.

portrait_00 = []

# The following data sets each draw just one of the individuals
# at their default height.

portrait_01 = [['Person A', 2, 1.0, '-']]

portrait_02 = [['Person B', 3, 1.0, '-']]

portrait_03 = [['Person C', 1, 1.0, '-']]

portrait_04 = [['Person D', 0, 1.0, '-']]

portrait_05 = [['Pet', 4, 1.0, '-']]

# The following data sets each draw just one of the individuals
# but multiple times and at different sizes.

portrait_06 = [['Person A', 3, 1.0, '-'],
               ['Person A', 1, 0.75, '-'],
               ['Person A', 2, 0.5, '-'],
               ['Person A', 4, 1.4, '-']]

portrait_07 = [['Person B', 0, 0.5, '-'],
               ['Person B', 2, 1.0, '-'],
               ['Person B', 3, 1.5, '-']]

portrait_08 = [['Person C', 0, 0.5, '-'],
               ['Person C', 1, 0.75, '-'],
               ['Person C', 2, 1.0, '-'],
               ['Person C', 3, 1.25, '-'],
               ['Person C', 4, 1.5, '-']]

portrait_09 = [['Person D', 3, 1.25, '-'],
               ['Person D', 1, 0.8, '-'],
               ['Person D', 0, 1.0, '-']]

portrait_10 = [['Pet', 1, 1.3, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Pet', 3, 0.7, '-']]

# The following data sets each draw a family portrait with all
# individuals at their default sizes.  These data sets create
# "natural" looking portraits.  Notably, the first two both
# show the full family.

portrait_11 = [['Person A', 0, 1.0, '-'],
               ['Person B', 1, 1.0, '-'],
               ['Person C', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Pet', 4, 1.0, '-']]

portrait_12 = [['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*'],
               ['Person C', 1, 1.0, '-'],
               ['Person D', 4, 1.0, '-'],
               ['Pet', 0, 1.0, '-']]

portrait_13 = [['Person B', 1, 1.0, '-'],
               ['Pet', 2, 1.0, '-'],
               ['Person C', 3, 1.0, '*']]

portrait_14 = [['Person C', 0, 1.0, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.0, '*'],
               ['Person D', 3, 1.0, '-'],
               ['Person B', 4, 1.0, '-']]

portrait_15 = [['Person D', 4, 1.0, '*'],
               ['Person A', 3, 1.0, '-'],
               ['Person B', 2, 1.0, '-']]

portrait_16 = [['Person D', 1, 1.0, '-'],
               ['Person C', 0, 1.0, '-'],
               ['Person A', 2, 1.0, '-'],
               ['Person B', 3, 1.0, '*']]

# The following data sets draw all five individuals at their
# minimum and maximum heights.

portrait_17 = [['Person A', 0, 0.5, '-'],
               ['Person B', 1, 0.5, '-'],
               ['Person C', 2, 0.5, '*'],
               ['Person D', 3, 0.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_18 = [['Person A', 4, 1.5, '-'],
               ['Person B', 3, 1.5, '*'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 1, 1.5, '-'],
               ['Pet', 0, 1.5, '-']]

# The following data sets each draw a family portrait with
# various individuals at varying sizes.

portrait_19 = [['Person A', 0, 0.5, '*'],
               ['Person B', 1, 0.8, '-'],
               ['Person C', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '-'],
               ['Pet', 4, 0.5, '-']]

portrait_20 = [['Person B', 1, 0.8, '*'],
               ['Pet', 2, 1.4, '-'],
               ['Person C', 3, 0.7, '-']]

portrait_21 = [['Person C', 0, 1.5, '-'],
               ['Pet', 1, 1.0, '-'],
               ['Person A', 2, 1.5, '-'],
               ['Person D', 3, 1.5, '*'],
               ['Person B', 4, 1.5, '-']]

portrait_22 = [['Person D', 4, 1.2, '-'],
               ['Person A', 3, 1.0, '*'],
               ['Person B', 2, 0.8, '-']]

portrait_23 = [['Person D', 1, 1.1, '-'],
               ['Person C', 2, 0.9, '-'],
               ['Person A', 0, 1.1, '*'],
               ['Person B', 3, 0.9, '-']]

# ***** If you want to create your own data sets you can add them here
# ***** (but your code must still work with all the data sets above plus
# ***** any other data sets in this style).

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_portrait" function.
#

# Draw the stick figures as per the provided data set

### Much of the code at the beginning and end of each body part is
### redundant. It was written this way to help prevent errors, and made
### copy-pasting and moving the code around far easier (it worked).
### Some of the body parts could have been written as definitions to help
### condense the code and make it easier to read, but I ran out of time.
### It also would have made the figures slightly less unique for small
### variations, however.
### The crown could have also been made a definition, but again, I ran
### out of time.
### The cat was made mainly out of stamped elipses, mainly as an experiment
### in contrast to the goto()-dominant humaniod figures. Enjoy my program!

# Uses a for loop to set the variables for the person's definition,
# then draws that person

def draw_portrait(portrait_list):
    for variable in portrait_list:
        location = variable[1]
        scale = variable[2]
        hat = variable[3]

        if variable[0] == 'Person A':
            father(variable[1], variable[2], variable[3])
        elif variable[0] == 'Person B':
            mother(variable[1], variable[2], variable[3])
        elif variable[0] == 'Person C':
            son(variable[1], variable[2], variable[3])
        elif variable[0] == 'Person D':
            daughter(variable[1], variable[2], variable[3])
        elif variable[0] == 'Pet':
            cat(variable[1], variable[2], variable[3])

def father(location, scale, hat):

#scale factor (k was used to cut down on typing and make the goto's
# easier to read)
    k = scale

#location to draw in (uses booleans to determine location to draw person)
    if location == 0:
        pu()
        goto(-300,0)
        pd()
        location_offset_x = -300
        location_offset_y = 0

    elif location == 1:
        pu()
        goto(-150,0)
        pd()
        location_offset_x = -150
        location_offset_y = 0

    elif location == 2:
        pu()
        goto(0,0)
        pd()
        location_offset_x = 0
        location_offset_y = 0

    elif location == 3:
        pu()
        goto(150,0)
        pd()
        location_offset_x = 150
        location_offset_y = 0

    elif location == 4:
        pu()
        goto(300,0)
        pd()
        location_offset_x = 300
        location_offset_y = 0 
        
    width(3)
    
#left shoe
    pu()
    goto(-35 + location_offset_x,k*(18 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.8 * k, 1.5, 3)
    fillcolor('brown')
    pencolor('black')
    stamp()
#return shape to normal
    shape('classic')
    shapesize(1,1,1)

#right shoe
    pu()
    goto(35 + location_offset_x,k*(18 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.8 * k, 1.5, 3)
    fillcolor('brown')
    pencolor('black')
    stamp()
#return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#pants
    pu()
    fillcolor('dark gray')
    begin_fill()
    goto(0 + location_offset_x,k*(80 + location_offset_y))

    pd()
    goto(-20 + location_offset_x,k*(20 + location_offset_y))
    goto(-40 + location_offset_x,k*(20 + location_offset_y))
    goto(-30 + location_offset_x,k*(100 + location_offset_y))
    goto(30 + location_offset_x,k*(100 + location_offset_y))
    goto(40 + location_offset_x,k*(20 + location_offset_y))
    goto(20 + location_offset_x,k*(20 + location_offset_y))
    goto(0 + location_offset_x,k*(80 + location_offset_y))
    end_fill()

#belt
    pu()
    fillcolor('black')
    begin_fill()
    goto(-30 + location_offset_x,k*(100 + location_offset_y))

    pd()
    goto(-30 + location_offset_x,k*(105 + location_offset_y))
    goto(30 + location_offset_x,k*(105 + location_offset_y))
    goto(30 + location_offset_x,k*(100 + location_offset_y))
    goto(-30 + location_offset_x,k*(100 + location_offset_y))
    end_fill()
#neck
    pu()
    fillcolor('tan')
    goto(-5 + location_offset_x,k*(160 + location_offset_y))
    begin_fill()

    pd()
    goto(5 + location_offset_x,k*(160 + location_offset_y))
    goto(5 + location_offset_x,k*(190 + location_offset_y))
    goto(-5 + location_offset_x,k*(190 + location_offset_y))
    goto(-5 + location_offset_x,k*(160 + location_offset_y))
    end_fill()
    
#left arm
    pu()
    fillcolor('tan')
    goto(-55 + location_offset_x,k*(160 + location_offset_y))
    begin_fill()

    pd()
    goto(-70 + location_offset_x,k*(140 + location_offset_y))
    goto(-40 + location_offset_x,k*(120 + location_offset_y))
    goto(-35 + location_offset_x,k*(123 + location_offset_y))
    goto(-60 + location_offset_x,k*(140 + location_offset_y))
    goto(-45 + location_offset_x,k*(160 + location_offset_y))
    pu()
    end_fill()

#right arm
    pu()
    fillcolor('tan')
    goto(55 + location_offset_x,k*(160 + location_offset_y))
    begin_fill()

    pd()
    goto(70 + location_offset_x,k*(140 + location_offset_y))
    goto(40 + location_offset_x,k*(120 + location_offset_y))
    goto(35 + location_offset_x,k*(123 + location_offset_y))
    goto(60 + location_offset_x,k*(140 + location_offset_y))
    goto(45 + location_offset_x,k*(160 + location_offset_y))
    pu()
    end_fill()
    
#shirt
    pu()
    fillcolor('light blue')
    goto(-30 + location_offset_x,k*(105 + location_offset_y))
    begin_fill()

    pd()
    goto(-40 + location_offset_x,k*(160 + location_offset_y))
    goto(-50 + location_offset_x,k*(150 + location_offset_y))
    goto(-60 + location_offset_x,k*(160 + location_offset_y))
    goto(-40 + location_offset_x,k*(180 + location_offset_y))
    goto(-10 + location_offset_x,k*(180 + location_offset_y))
    goto(0 + location_offset_x,k*(165 + location_offset_y))
    goto(10 + location_offset_x,k*(180 + location_offset_y))
    goto(40 + location_offset_x,k*(180 + location_offset_y))
    goto(60 + location_offset_x,k*(160 + location_offset_y))
    goto(50 + location_offset_x,k*(150 + location_offset_y))
    goto(40 + location_offset_x,k*(160 + location_offset_y))
    goto(30 + location_offset_x,k*(105 + location_offset_y))
    end_fill()

    pu()
    goto(0 + location_offset_x,k*(165 + location_offset_y))
    pd()
    begin_fill()
    goto(10 + location_offset_x,k*(160 + location_offset_y))
    goto(25 + location_offset_x,k*(180 + location_offset_y))
    end_fill
    pu()
    goto(0 + location_offset_x,k*(165 + location_offset_y))
    pd()
    begin_fill()
    goto(-10 + location_offset_x,k*(160 + location_offset_y))
    goto(-25 + location_offset_x,k*(180 + location_offset_y))
    end_fill()

#left hand
    pu()
    goto(-35 + location_offset_x,k*(120 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.6 * k, 1, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#right hand
    pu()
    goto(35 + location_offset_x,k*(120 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.6 * k, 1, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#tie
    pu()
    color('black')
    fillcolor('yellow')
    goto(-10 + location_offset_x,k*(160 + location_offset_y))
    begin_fill()

    pd()
    goto(0 + location_offset_x,k*(155 + location_offset_y))
    goto(10 + location_offset_x,k*(160 + location_offset_y))
    goto(0 + location_offset_x,k*(165 + location_offset_y))
    goto(-10 + location_offset_x,k*(160 + location_offset_y))
    end_fill()

    pu()
    goto(0 + location_offset_x,k*(155 + location_offset_y))
    pd()
    begin_fill()
    goto(-10 + location_offset_x,k*(120 + location_offset_y))
    goto(0 + location_offset_x,k*(110 + location_offset_y))
    goto(10 + location_offset_x,k*(120 + location_offset_y)) 
    goto(0 + location_offset_x,k*(155 + location_offset_y))
    end_fill()
    pu()

#head
    pu()
    goto(0 + location_offset_x,k*(210 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(2.2 * k, 2.2, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#face
    #mouth
    pu()
    goto(-10 + location_offset_x,k*(200 + location_offset_y))
    pd()
    goto(-5 + location_offset_x,k*(196 + location_offset_y))
    goto(0 + location_offset_x,k*(194 + location_offset_y))
    goto(5 + location_offset_x,k*(196 + location_offset_y))
    goto(10 + location_offset_x,k*(200 + location_offset_y))
    pu()
    
    #left eye
    pu()
    goto(-10 + location_offset_x,k*(215 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.4, 3)
    fillcolor('white')
    pencolor('black')
    stamp()

    #right eye
    pu()
    goto(10 + location_offset_x,k*(215 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.4, 3)
    fillcolor('white')
    pencolor('black')
    stamp()
    #return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#crown
    if hat == '*':
        pu()
        goto(0 + location_offset_x,k*(225 + location_offset_y))
        fillcolor('yellow')

        pd()
        begin_fill()
        goto(-20 + location_offset_x,k*(225 + location_offset_y))
        goto(-35 + location_offset_x,k*(245 + location_offset_y))
        goto(-10 + location_offset_x,k*(235 + location_offset_y))
        goto(0 + location_offset_x,k*(245 + location_offset_y))
        goto(10 + location_offset_x,k*(235 + location_offset_y))
        goto(35 + location_offset_x,k*(245 + location_offset_y))
        goto(20 + location_offset_x,k*(225 + location_offset_y))
        goto(0 + location_offset_x,k*(225 + location_offset_y))
        end_fill()
        pu()

    #crown jewels
        pu()
        goto(0 + location_offset_x,k*(235 + location_offset_y))
        resizemode('user')
        shape('circle')
        shapesize(0.4 * k, 0.4, 1)
        fillcolor('red')
        pencolor('black')
        stamp()
        goto(-15 + location_offset_x,k*(231 + location_offset_y))
        shapesize(0.3 * k, 0.3, 1)
        fillcolor('blue')
        pencolor('black')
        stamp()
        goto(15 + location_offset_x,k*(231 + location_offset_y))
        shapesize(0.3 * k, 0.3, 1)
        fillcolor('blue')
        pencolor('black')
        stamp()

        #return shape to normal
        shape('classic')
        shapesize(1,1,1)
    
    else:
        pass


def mother(location, scale, hat):

#scale factor
    k = scale

#location to draw in 
    if location == 0:
        pu()
        goto(-300,0)
        pd()
        location_offset_x = -300
        location_offset_y = 0

    elif location == 1:
        pu()
        goto(-150,0)
        pd()
        location_offset_x = -150
        location_offset_y = 0

    elif location == 2:
        pu()
        goto(0,0)
        pd()
        location_offset_x = 0
        location_offset_y = 0

    elif location == 3:
        pu()
        goto(150,0)
        pd()
        location_offset_x = 150
        location_offset_y = 0

    elif location == 4:
        pu()
        goto(300,0)
        pd()
        location_offset_x = 300
        location_offset_y = 0 
        
    width(3)
    
#left leg
    pu()
    fillcolor('tan')
    goto(-32 + location_offset_x,k*(55 + location_offset_y))
    
    pd()
    begin_fill()
    goto(-40 + location_offset_x,k*(18 + location_offset_y))
    goto(-35 + location_offset_x,k*(18 + location_offset_y))
    goto(-26 + location_offset_x,k*(55 + location_offset_y))
    goto(-32 + location_offset_x,k*(55 + location_offset_y))
    end_fill()
    pu()

#right leg
    pu()
    fillcolor('tan')
    goto(32 + location_offset_x,k*(55 + location_offset_y))
    
    pd()
    begin_fill()
    goto(40 + location_offset_x,k*(18 + location_offset_y))
    goto(35 + location_offset_x,k*(18 + location_offset_y))
    goto(26 + location_offset_x,k*(55 + location_offset_y))
    goto(32 + location_offset_x,k*(55 + location_offset_y))
    end_fill()
    pu()
    
#left shoe
    pu()
    goto(-40 + location_offset_x,k*(18 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.7 * k, 1.2, 3)
    fillcolor('gray')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#right shoe
    pu()
    goto(40 + location_offset_x,k*(18 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.7 * k, 1.2, 3)
    fillcolor('gray')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#skirt
    pu()
    fillcolor('dark blue')
    begin_fill()
    goto(-50 + location_offset_x,k*(50 + location_offset_y))

    pd()
    goto(-30 + location_offset_x,k*(105 + location_offset_y))
    goto(30 + location_offset_x,k*(105 + location_offset_y))
    goto(50 + location_offset_x,k*(50 + location_offset_y))
    goto(-50 + location_offset_x,k*(50 + location_offset_y))
    end_fill()

#hair
    pu()
    fillcolor('sandy brown')
    goto(-40 + location_offset_x,k*(185 + location_offset_y))
    begin_fill()

    pd()
    goto(-35 + location_offset_x,k*(225 + location_offset_y))
    goto(-30 + location_offset_x,k*(230 + location_offset_y))
    goto(-15 + location_offset_x,k*(236 + location_offset_y))
    goto(-10 + location_offset_x,k*(238 + location_offset_y))
    goto(0 + location_offset_x,k*(240 + location_offset_y))
    goto(10 + location_offset_x,k*(238 + location_offset_y))
    goto(15 + location_offset_x,k*(236 + location_offset_y))
    goto(30 + location_offset_x,k*(230 + location_offset_y))
    goto(35 + location_offset_x,k*(225 + location_offset_y))
    goto(40 + location_offset_x,k*(185 + location_offset_y))
    goto(-40 + location_offset_x,k*(185 + location_offset_y))
    end_fill()
    pu()
    
#neck
    pu()
    fillcolor('tan')
    goto(-5 + location_offset_x,k*(160 + location_offset_y))
    begin_fill()

    pd()
    goto(5 + location_offset_x,k*(160 + location_offset_y))
    goto(5 + location_offset_x,k*(190 + location_offset_y))
    goto(-5 + location_offset_x,k*(190 + location_offset_y))
    goto(-5 + location_offset_x,k*(160 + location_offset_y))
    end_fill()
    
#left arm
    pu()
    fillcolor('tan')
    goto(-55 + location_offset_x,k*(160 + location_offset_y))
    begin_fill()

    pd()
    goto(-70 + location_offset_x,k*(140 + location_offset_y))
    goto(-40 + location_offset_x,k*(120 + location_offset_y))
    goto(-35 + location_offset_x,k*(123 + location_offset_y))
    goto(-60 + location_offset_x,k*(140 + location_offset_y))
    goto(-45 + location_offset_x,k*(160 + location_offset_y))
    pu()
    end_fill()

#right arm
    pu()
    fillcolor('tan')
    goto(55 + location_offset_x,k*(160 + location_offset_y))
    begin_fill()

    pd()
    goto(70 + location_offset_x,k*(140 + location_offset_y))
    goto(40 + location_offset_x,k*(120 + location_offset_y))
    goto(35 + location_offset_x,k*(123 + location_offset_y))
    goto(60 + location_offset_x,k*(140 + location_offset_y))
    goto(45 + location_offset_x,k*(160 + location_offset_y))
    pu()
    end_fill()
    
#shirt
    pu()
    fillcolor('white')
    goto(-35 + location_offset_x,k*(105 + location_offset_y))
    begin_fill()

    pd()
    goto(-25 + location_offset_x,k*(135 + location_offset_y))
    goto(-40 + location_offset_x,k*(160 + location_offset_y))
    goto(-50 + location_offset_x,k*(150 + location_offset_y))
    goto(-60 + location_offset_x,k*(160 + location_offset_y))
    goto(-40 + location_offset_x,k*(180 + location_offset_y))
    goto(-10 + location_offset_x,k*(180 + location_offset_y))
    goto(0 + location_offset_x,k*(165 + location_offset_y))
    goto(10 + location_offset_x,k*(180 + location_offset_y))
    goto(40 + location_offset_x,k*(180 + location_offset_y))
    goto(60 + location_offset_x,k*(160 + location_offset_y))
    goto(50 + location_offset_x,k*(150 + location_offset_y))
    goto(40 + location_offset_x,k*(160 + location_offset_y))
    goto(25 + location_offset_x,k*(135 + location_offset_y))
    goto(35 + location_offset_x,k*(105 + location_offset_y))
    goto(-35 + location_offset_x,k*(105 + location_offset_y))
    end_fill()

    pu()
    goto(0 + location_offset_x,k*(165 + location_offset_y))
    pd()
    begin_fill()
    goto(10 + location_offset_x,k*(160 + location_offset_y))
    goto(25 + location_offset_x,k*(180 + location_offset_y))
    end_fill
    pu()
    goto(0 + location_offset_x,k*(165 + location_offset_y))
    pd()
    begin_fill()
    goto(-10 + location_offset_x,k*(160 + location_offset_y))
    goto(-25 + location_offset_x,k*(180 + location_offset_y))
    end_fill()

#left hand
    pu()
    goto(-35 + location_offset_x,k*(120 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.6 * k, 1, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#right hand
    pu()
    goto(35 + location_offset_x,k*(120 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.6 * k, 1, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#head
    pu()
    goto(0 + location_offset_x,k*(210 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(2.2 * k, 2.2, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#hair pt2 electric boogaloo 
    pu()
    fillcolor('sandy brown')
    goto(-35 + location_offset_x,k*(225 + location_offset_y))
    begin_fill()
    pd()
    goto(35 + location_offset_x,k*(225 + location_offset_y))
    pu()
    goto(0 + location_offset_x,k*(238 + location_offset_y))
    end_fill()
    pu()
    
#face
    #mouth
    pu()
    goto(-10 + location_offset_x,k*(200 + location_offset_y))
    pd()
    goto(-5 + location_offset_x,k*(200 + location_offset_y))
    goto(0 + location_offset_x,k*(200 + location_offset_y))
    goto(5 + location_offset_x,k*(200 + location_offset_y))
    goto(10 + location_offset_x,k*(200 + location_offset_y))
    pu()
    
    #left eye
    pu()
    goto(-10 + location_offset_x,k*(215 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.4, 3)
    fillcolor('light blue')
    pencolor('black')
    stamp()
    
    #right eye
    pu()
    goto(10 + location_offset_x,k*(215 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.4, 3)
    fillcolor('light blue')
    pencolor('black')
    stamp()
    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#crown
    if hat == '*':
        pu()
        goto(0 + location_offset_x,k*(230 + location_offset_y))
        fillcolor('yellow')

        pd()
        begin_fill()
        goto(-20 + location_offset_x,k*(230 + location_offset_y))
        goto(-35 + location_offset_x,k*(250 + location_offset_y))
        goto(-10 + location_offset_x,k*(240 + location_offset_y))
        goto(0 + location_offset_x,k*(250 + location_offset_y))
        goto(10 + location_offset_x,k*(240 + location_offset_y))
        goto(35 + location_offset_x,k*(250 + location_offset_y))
        goto(20 + location_offset_x,k*(230 + location_offset_y))
        goto(0 + location_offset_x,k*(230 + location_offset_y))
        end_fill()
        pu()

    #crown jewels
        pu()
        goto(0 + location_offset_x,k*(240 + location_offset_y))
        resizemode('user')
        shape('circle')
        shapesize(0.4 * k, 0.4, 1)
        fillcolor('red')
        pencolor('black')
        stamp()
        goto(-15 + location_offset_x,k*(236 + location_offset_y))
        shapesize(0.3 * k, 0.3, 1)
        fillcolor('blue')
        pencolor('black')
        stamp()
        goto(15 + location_offset_x,k*(236 + location_offset_y))
        shapesize(0.3 * k, 0.3, 1)
        fillcolor('blue')
        pencolor('black')
        stamp()

        #return shape to normal
        shape('classic')
        shapesize(1,1,1)
    
    else:
        pass

def son(location, scale, hat):

#scale factor
    k = scale

#location to draw in 
    if location == 0:
        pu()
        goto(-300,0)
        pd()
        location_offset_x = -300
        location_offset_y = 0

    elif location == 1:
        pu()
        goto(-150,0)
        pd()
        location_offset_x = -150
        location_offset_y = 0

    elif location == 2:
        pu()
        goto(0,0)
        pd()
        location_offset_x = 0
        location_offset_y = 0

    elif location == 3:
        pu()
        goto(150,0)
        pd()
        location_offset_x = 150
        location_offset_y = 0

    elif location == 4:
        pu()
        goto(300,0)
        pd()
        location_offset_x = 300
        location_offset_y = 0 
        
    width(3)
    
#left leg
    pu()
    fillcolor('tan')
    goto(-32 + location_offset_x,k*(55 + location_offset_y))
    
    pd()
    begin_fill()
    goto(-40 + location_offset_x,k*(18 + location_offset_y))
    goto(-35 + location_offset_x,k*(18 + location_offset_y))
    goto(-26 + location_offset_x,k*(55 + location_offset_y))
    goto(-32 + location_offset_x,k*(55 + location_offset_y))
    end_fill()
    pu()

#right leg
    pu()
    fillcolor('tan')
    goto(32 + location_offset_x,k*(55 + location_offset_y))
    
    pd()
    begin_fill()
    goto(40 + location_offset_x,k*(18 + location_offset_y))
    goto(35 + location_offset_x,k*(18 + location_offset_y))
    goto(26 + location_offset_x,k*(55 + location_offset_y))
    goto(32 + location_offset_x,k*(55 + location_offset_y))
    end_fill()
    pu()
    
#left shoe
    pu()
    goto(-40 + location_offset_x,k*(18 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.7 * k, 1.2, 3)
    fillcolor('white')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#right shoe
    pu()
    goto(40 + location_offset_x,k*(18 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.7 * k, 1.2, 3)
    fillcolor('white')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#pants
    pu()
    fillcolor('blue')
    begin_fill()
    goto(0 + location_offset_x,k*(70 + location_offset_y))

    pd()
    goto(-20 + location_offset_x,k*(50 + location_offset_y))
    goto(-40 + location_offset_x,k*(50 + location_offset_y))
    goto(-30 + location_offset_x,k*(80 + location_offset_y))
    goto(30 + location_offset_x,k*(80 + location_offset_y))
    goto(40 + location_offset_x,k*(50 + location_offset_y))
    goto(20 + location_offset_x,k*(50 + location_offset_y))
    goto(0 + location_offset_x,k*(70 + location_offset_y))
    end_fill()

#neck
    pu()
    fillcolor('tan')
    goto(-5 + location_offset_x,k*(120 + location_offset_y))
    begin_fill()

    pd()
    goto(5 + location_offset_x,k*(120 + location_offset_y))
    goto(5 + location_offset_x,k*(143 + location_offset_y))
    goto(-5 + location_offset_x,k*(143 + location_offset_y))
    goto(-5 + location_offset_x,k*(120 + location_offset_y))
    end_fill()
    
#left arm
    pu()
    fillcolor('tan')
    goto(-55 + location_offset_x,k*(140 + location_offset_y))
    begin_fill()

    pd()
    goto(-75 + location_offset_x,k*(160 + location_offset_y))
    goto(-60 + location_offset_x,k*(180 + location_offset_y))
    goto(-50 + location_offset_x,k*(180 + location_offset_y))
    goto(-65 + location_offset_x,k*(160 + location_offset_y))
    goto(-40 + location_offset_x,k*(140 + location_offset_y))
    pu()
    end_fill()

#right arm
    pu()
    fillcolor('tan')
    goto(55 + location_offset_x,k*(140 + location_offset_y))
    begin_fill()

    pd()
    goto(75 + location_offset_x,k*(160 + location_offset_y))
    goto(60 + location_offset_x,k*(180 + location_offset_y))
    goto(50 + location_offset_x,k*(180 + location_offset_y))
    goto(65 + location_offset_x,k*(160 + location_offset_y))
    goto(40 + location_offset_x,k*(140 + location_offset_y))
    pu()
    end_fill()
    
#shirt
    pu()
    fillcolor('green')
    goto(-35 + location_offset_x,k*(75 + location_offset_y))
    begin_fill()

    pd()
    goto(-40 + location_offset_x,k*(125 + location_offset_y))
    goto(-60 + location_offset_x,k*(140 + location_offset_y))
    goto(-45 + location_offset_x,k*(150 + location_offset_y))
    goto(-35 + location_offset_x,k*(140 + location_offset_y))
    goto(-10 + location_offset_x,k*(135 + location_offset_y))
    goto(0 + location_offset_x,k*(130 + location_offset_y))
    goto(10 + location_offset_x,k*(135 + location_offset_y))
    goto(35 + location_offset_x,k*(140 + location_offset_y))
    goto(45 + location_offset_x,k*(150 + location_offset_y))
    goto(60 + location_offset_x,k*(140 + location_offset_y))
    goto(40 + location_offset_x,k*(125 + location_offset_y))
    goto(35 + location_offset_x,k*(75 + location_offset_y))
    goto(-35 + location_offset_x,k*(75 + location_offset_y))
    end_fill()

   
#left hand
    pu()
    goto(-50 + location_offset_x,k*(183 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.6 * k, 1, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#right hand
    pu()
    goto(50 + location_offset_x,k*(183 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.6 * k, 1, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#hair
    pu()
    fillcolor('brown')
    goto(-10 + location_offset_x,k*(160 + location_offset_y))
    begin_fill()

    pd()
    goto(-25 + location_offset_x,k*(180 + location_offset_y))
    goto(-20 + location_offset_x,k*(175 + location_offset_y))
    goto(-15 + location_offset_x,k*(185 + location_offset_y))
    goto(-10 + location_offset_x,k*(180 + location_offset_y))
    goto(-5 + location_offset_x,k*(190 + location_offset_y))
    goto(0 + location_offset_x,k*(185 + location_offset_y))
    goto(5 + location_offset_x,k*(190 + location_offset_y))
    goto(10 + location_offset_x,k*(180 + location_offset_y))
    goto(15 + location_offset_x,k*(185 + location_offset_y))
    goto(20 + location_offset_x,k*(175 + location_offset_y))
    goto(25 + location_offset_x,k*(180 + location_offset_y))
    goto(10 + location_offset_x,k*(160 + location_offset_y))
    end_fill()
    pu()

#head
    pu()
    goto(0 + location_offset_x,k*(160 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(2 * k, 2, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#face
    #mouth
    pu()
    goto(-10 + location_offset_x,k*(150 + location_offset_y))
    pd()
    goto(-5 + location_offset_x,k*(153 + location_offset_y))
    goto(0 + location_offset_x,k*(154 + location_offset_y))
    goto(5 + location_offset_x,k*(153 + location_offset_y))
    goto(10 + location_offset_x,k*(150 + location_offset_y))
    pu()
    
    #left eye
    pu()
    goto(-10 + location_offset_x,k*(165 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.4, 3)
    fillcolor('dark green')
    pencolor('black')
    stamp()

    #right eye
    pu()
    goto(10 + location_offset_x,k*(165 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.4, 3)
    fillcolor('dark green')
    pencolor('black')
    stamp()
    #return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#crown
    if hat == '*':
        pu()
        goto(0 + location_offset_x,k*(175 + location_offset_y))
        fillcolor('yellow')

        pd()
        begin_fill()
        goto(-20 + location_offset_x,k*(175 + location_offset_y))
        goto(-35 + location_offset_x,k*(195 + location_offset_y))
        goto(-10 + location_offset_x,k*(185 + location_offset_y))
        goto(0 + location_offset_x,k*(195 + location_offset_y))
        goto(10 + location_offset_x,k*(185 + location_offset_y))
        goto(35 + location_offset_x,k*(195 + location_offset_y))
        goto(20 + location_offset_x,k*(175 + location_offset_y))
        goto(0 + location_offset_x,k*(175 + location_offset_y))
        end_fill()
        pu()

    #crown jewels
        pu()
        goto(0 + location_offset_x,k*(185 + location_offset_y))
        resizemode('user')
        shape('circle')
        shapesize(0.4 * k, 0.4, 1)
        fillcolor('red')
        pencolor('black')
        stamp()
        goto(-15 + location_offset_x,k*(181 + location_offset_y))
        shapesize(0.3 * k, 0.3, 1)
        fillcolor('blue')
        pencolor('black')
        stamp()
        goto(15 + location_offset_x,k*(181 + location_offset_y))
        shapesize(0.3 * k, 0.3, 1)
        fillcolor('blue')
        pencolor('black')
        stamp()

        #return shape to normal
        shape('classic')
        shapesize(1,1,1)
    
    else:
        pass

def daughter(location, scale, hat):

#scale factor
    k = scale

#location to draw in 
    if location == 0:
        pu()
        goto(-300,0)
        pd()
        location_offset_x = -300
        location_offset_y = 0

    elif location == 1:
        pu()
        goto(-150,0)
        pd()
        location_offset_x = -150
        location_offset_y = 0

    elif location == 2:
        pu()
        goto(0,0)
        pd()
        location_offset_x = 0
        location_offset_y = 0

    elif location == 3:
        pu()
        goto(150,0)
        pd()
        location_offset_x = 150
        location_offset_y = 0

    elif location == 4:
        pu()
        goto(300,0)
        pd()
        location_offset_x = 300
        location_offset_y = 0 
        
    width(3)
    
#left leg
    pu()
    fillcolor('tan')
    goto(-22 + location_offset_x,k*(55 + location_offset_y))
    
    pd()
    begin_fill()
    goto(-28 + location_offset_x,k*(30 + location_offset_y))
    goto(-35 + location_offset_x,k*(47 + location_offset_y))
    goto(-40 + location_offset_x,k*(47 + location_offset_y))
    goto(-28 + location_offset_x,k*(23 + location_offset_y))
    goto(-22 + location_offset_x,k*(30 + location_offset_y))
    goto(-18 + location_offset_x,k*(55 + location_offset_y))
    end_fill()
    pu()
    
#right leg
    pu()
    fillcolor('tan')
    goto(22 + location_offset_x,k*(55 + location_offset_y))
    
    pd()
    begin_fill()
    goto(28 + location_offset_x,k*(30 + location_offset_y))
    goto(35 + location_offset_x,k*(47 + location_offset_y))
    goto(40 + location_offset_x,k*(47 + location_offset_y))
    goto(28 + location_offset_x,k*(23 + location_offset_y))
    goto(22 + location_offset_x,k*(30 + location_offset_y))
    goto(18 + location_offset_x,k*(55 + location_offset_y))
    end_fill()
    pu()
    
#left shoe
    pu()
    goto(-40 + location_offset_x,k*(47 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.7 * k, 1.2, 3)
    fillcolor('sandy brown')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#right shoe
    pu()
    goto(40 + location_offset_x,k*(47 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.7 * k, 1.2, 3)
    fillcolor('sandy brown')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#skirt
    pu()
    fillcolor('purple')
    begin_fill()
    goto(-40 + location_offset_x,k*(50 + location_offset_y))

    pd()
    goto(-30 + location_offset_x,k*(80 + location_offset_y))
    goto(30 + location_offset_x,k*(80 + location_offset_y))
    goto(40 + location_offset_x,k*(50 + location_offset_y))
    goto(-40 + location_offset_x,k*(50 + location_offset_y))
    
    end_fill()

#neck
    pu()
    fillcolor('tan')
    goto(-5 + location_offset_x,k*(120 + location_offset_y))
    begin_fill()

    pd()
    goto(5 + location_offset_x,k*(120 + location_offset_y))
    goto(5 + location_offset_x,k*(143 + location_offset_y))
    goto(-5 + location_offset_x,k*(143 + location_offset_y))
    goto(-5 + location_offset_x,k*(120 + location_offset_y))
    end_fill()
    
#left arm
    pu()
    fillcolor('tan')
    goto(-55 + location_offset_x,k*(140 + location_offset_y))
    begin_fill()

    pd()
    goto(-75 + location_offset_x,k*(160 + location_offset_y))
    goto(-60 + location_offset_x,k*(180 + location_offset_y))
    goto(-50 + location_offset_x,k*(180 + location_offset_y))
    goto(-65 + location_offset_x,k*(160 + location_offset_y))
    goto(-40 + location_offset_x,k*(140 + location_offset_y))
    pu()
    end_fill()

#right arm
    pu()
    fillcolor('tan')
    goto(55 + location_offset_x,k*(120 + location_offset_y))
    begin_fill()

    pd()
    goto(65 + location_offset_x,k*(100 + location_offset_y))
    goto(35 + location_offset_x,k*(80 + location_offset_y))
    goto(30 + location_offset_x,k*(83 + location_offset_y))
    goto(55 + location_offset_x,k*(100 + location_offset_y))
    goto(40 + location_offset_x,k*(120 + location_offset_y))
    pu()
    end_fill()
    
#shirt
    pu()
    fillcolor('red')
    goto(-35 + location_offset_x,k*(75 + location_offset_y))
    begin_fill()

    pd()
    goto(-40 + location_offset_x,k*(125 + location_offset_y))
    goto(-60 + location_offset_x,k*(140 + location_offset_y))
    goto(-45 + location_offset_x,k*(150 + location_offset_y))
    goto(-35 + location_offset_x,k*(140 + location_offset_y))
    goto(-10 + location_offset_x,k*(135 + location_offset_y))
    goto(0 + location_offset_x,k*(130 + location_offset_y))
    goto(10 + location_offset_x,k*(135 + location_offset_y))
    goto(35 + location_offset_x,k*(135 + location_offset_y))
    goto(55 + location_offset_x,k*(120 + location_offset_y))
    goto(45 + location_offset_x,k*(115 + location_offset_y))
    goto(35 + location_offset_x,k*(120 + location_offset_y))
    goto(35 + location_offset_x,k*(75 + location_offset_y))
    goto(-35 + location_offset_x,k*(75 + location_offset_y))
    end_fill()

   
#left hand
    pu()
    goto(-50 + location_offset_x,k*(183 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.6 * k, 1, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#right hand
    pu()
    goto(30 + location_offset_x,k*(80 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.6 * k, 1, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)


#head
    pu()
    goto(0 + location_offset_x,k*(160 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(2 * k, 2, 3)
    fillcolor('tan')
    pencolor('black')
    stamp()

    #return shape to normal
    shape('classic')
    shapesize(1,1,1)

#hair
    pu()
    fillcolor('brown')
    goto(-20 + location_offset_x,k*(173 + location_offset_y))
    begin_fill()
    
    pd()
    goto(-15 + location_offset_x,k*(178 + location_offset_y))
    goto(-10 + location_offset_x,k*(182 + location_offset_y))
    goto(-5 + location_offset_x,k*(185 + location_offset_y))
    goto(0 + location_offset_x,k*(186 + location_offset_y))
    goto(5 + location_offset_x,k*(185 + location_offset_y))
    goto(10 + location_offset_x,k*(182 + location_offset_y))
    goto(15 + location_offset_x,k*(178 + location_offset_y))
    goto(20 + location_offset_x,k*(173 + location_offset_y))
    goto(-20 + location_offset_x,k*(173 + location_offset_y))
    end_fill()
    pu()
    
    goto(10 + location_offset_x,k*(182 + location_offset_y))
    pd()
    begin_fill()
    goto(25 + location_offset_x,k*(197 + location_offset_y))
    goto(23 + location_offset_x,k*(190 + location_offset_y))
    goto(28 + location_offset_x,k*(194 + location_offset_y))
    goto(23 + location_offset_x,k*(185 + location_offset_y))
    goto(32 + location_offset_x,k*(190 + location_offset_y))
    goto(22 + location_offset_x,k*(180 + location_offset_y))
    goto(10 + location_offset_x,k*(182 + location_offset_y))
    end_fill()
    pu()
    
#face
    #mouth
    pu()
    goto(-10 + location_offset_x,k*(150 + location_offset_y))
    pd()
    fillcolor('white')
    begin_fill()
    goto(-5 + location_offset_x,k*(147 + location_offset_y))
    goto(0 + location_offset_x,k*(146 + location_offset_y))
    goto(5 + location_offset_x,k*(147 + location_offset_y))
    goto(10 + location_offset_x,k*(150 + location_offset_y))
    goto(-10 + location_offset_x,k*(150 + location_offset_y))
    end_fill()
    pu()
    
    #left eye
    pu()
    goto(-10 + location_offset_x,k*(165 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.4, 3)
    fillcolor('purple')
    pencolor('black')
    stamp()

    #right eye
    pu()
    goto(10 + location_offset_x,k*(165 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.4, 3)
    fillcolor('purple')
    pencolor('black')
    stamp()
    #return shape to normal
    shape('classic')
    shapesize(1,1,1)
    
#crown
    if hat == '*':
        pu()
        goto(0 + location_offset_x,k*(175 + location_offset_y))
        fillcolor('yellow')

        pd()
        begin_fill()
        goto(-20 + location_offset_x,k*(175 + location_offset_y))
        goto(-35 + location_offset_x,k*(195 + location_offset_y))
        goto(-10 + location_offset_x,k*(185 + location_offset_y))
        goto(0 + location_offset_x,k*(195 + location_offset_y))
        goto(10 + location_offset_x,k*(185 + location_offset_y))
        goto(35 + location_offset_x,k*(195 + location_offset_y))
        goto(20 + location_offset_x,k*(175 + location_offset_y))
        goto(0 + location_offset_x,k*(175 + location_offset_y))
        end_fill()
        pu()

    #crown jewels
        pu()
        goto(0 + location_offset_x,k*(185 + location_offset_y))
        resizemode('user')
        shape('circle')
        shapesize(0.4 * k, 0.4, 1)
        fillcolor('red')
        pencolor('black')
        stamp()
        goto(-15 + location_offset_x,k*(181 + location_offset_y))
        shapesize(0.3 * k, 0.3, 1)
        fillcolor('blue')
        pencolor('black')
        stamp()
        goto(15 + location_offset_x,k*(181 + location_offset_y))
        shapesize(0.3 * k, 0.3, 1)
        fillcolor('blue')
        pencolor('black')
        stamp()

        #return shape to normal
        shape('classic')
        shapesize(1,1,1)
    
    else:
        pass

def cat(location, scale, hat):

#scale factor
    k = scale

#location to draw in 
    if location == 0:
        pu()
        goto(-300,0)
        pd()
        location_offset_x = -300
        location_offset_y = 0

    elif location == 1:
        pu()
        goto(-150,0)
        pd()
        location_offset_x = -150
        location_offset_y = 0

    elif location == 2:
        pu()
        goto(0,0)
        pd()
        location_offset_x = 0
        location_offset_y = 0

    elif location == 3:
        pu()
        goto(150,0)
        pd()
        location_offset_x = 150
        location_offset_y = 0

    elif location == 4:
        pu()
        goto(300,0)
        pd()
        location_offset_x = 300
        location_offset_y = 0 
        
    width(3)
    

#front leg 1
    pu()
    goto(-30 + location_offset_x,k*(38 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(1.7 * k, 0.3, 3)
    fillcolor('grey')
    pencolor('black')
    stamp()

#front leg 1 foot
    pu()
    goto(-35 + location_offset_x,k*(25 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.8, 3)
    fillcolor('white')
    pencolor('black')
    stamp()

#front leg 2
    pu()
    goto(-20 + location_offset_x,k*(35 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(1.7 * k, 0.3, 3)
    fillcolor('grey')
    pencolor('black')
    stamp()

#front leg 2 foot
    pu()
    goto(-25 + location_offset_x,k*(22 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.8, 3)
    fillcolor('white')
    pencolor('black')
    stamp()
    
#back leg 1
    pu()
    goto(20 + location_offset_x,k*(38 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(1.7 * k, 0.3, 3)
    fillcolor('grey')
    pencolor('black')
    stamp()

#back leg 1 foot
    pu()
    goto(15 + location_offset_x,k*(25 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.8, 3)
    fillcolor('white')
    pencolor('black')
    stamp()

#front leg 2
    pu()
    goto(30 + location_offset_x,k*(35 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(1.7 * k, 0.3, 3)
    fillcolor('grey')
    pencolor('black')
    stamp()

#front leg 2 foot
    pu()
    goto(25 + location_offset_x,k*(22 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.4 * k, 0.8, 3)
    fillcolor('white')
    pencolor('black')
    stamp()
    
#tail
    pu()
    seth(-25)
    goto(38 + location_offset_x,k*(62 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(2.3 * k, 0.5, 3)
    fillcolor('grey')
    pencolor('black')
    stamp()
    seth(0)
    
#body
    pu()
    goto(-5 + location_offset_x,k*(50 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(1 * k, 4.5, 3)
    fillcolor('grey')
    pencolor('black')
    stamp()


#head
    pu()
    goto(-50 + location_offset_x,k*(60 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(1.5 * k, 1.5, 3)
    fillcolor('grey')
    pencolor('black')
    stamp()

#ears
    pu()
    fillcolor('grey')
    goto(-50 + location_offset_x,k*(73 + location_offset_y))
    begin_fill()
    pd()
    goto(-45 + location_offset_x,k*(79 + location_offset_y))
    goto(-40 + location_offset_x,k*(73 + location_offset_y))
    end_fill()
    pu()
    goto(-60 + location_offset_x,k*(73 + location_offset_y))
    begin_fill()
    pd()
    goto(-55 + location_offset_x,k*(79 + location_offset_y))
    goto(-50 + location_offset_x,k*(73 + location_offset_y))
    end_fill()
    pu()

#mouth
    pu()
    goto(-59 + location_offset_x,k*(53 + location_offset_y))
    pd()
    goto(-55 + location_offset_x,k*(48 + location_offset_y))
    goto(-49 + location_offset_x,k*(53 + location_offset_y))
    goto(-45 + location_offset_x,k*(48 + location_offset_y))
    goto(-41 + location_offset_x,k*(53 + location_offset_y))

#eyes
    pu()
    goto(-45 + location_offset_x,k*(60 + location_offset_y))
    resizemode('user')
    shape('circle')
    shapesize(0.2 * k, 0.2, 3)
    fillcolor('black')
    pencolor('black')
    stamp()
    goto(-55 + location_offset_x,k*(60 + location_offset_y))
    stamp()
    
#return shape to normal
    shape('classic')
    shapesize(1,1,1)


#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your stick figures.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing window with a blue background representing
# the sky, and with the "home" coordinate set to the middle of the
# area where the stick figures will stand
setup(window_width, window_height)
setworldcoordinates(-window_width / 2, grass_offset,
                    window_width / 2, window_height + grass_offset)
bgcolor('sky blue')

# Draw the grass (with animation turned off to make it faster)
tracer(False)
draw_grass()

# Give the window a title
# ***** Replace this title with one that describes your choice
# ***** of individuals
title('My Stretchy Family (Generic Family Sitcom Family)')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Draw the locations to stand, their labels and selected coordinates
# ***** If you don't want to display these background elements,
# ***** to make your portrait look nicer, change the corresponding
# ***** argument(s) below to False
draw_locations(True)
draw_labels(True)
mark_coords(False)

# Call the student's function to display the stick figures
# ***** If you want to turn off animation while drawing your
# ***** stick figures, to make your program draw faster, change
# ***** the following argument to False
tracer(True)
# ***** Change the argument to this function to test your
# ***** code with different data sets
draw_portrait(portrait_18)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

