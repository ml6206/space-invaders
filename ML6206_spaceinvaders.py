# Mengxun Lin
# CS-UY 1114
# Final project Status Report

import turtle
import time

# This variable store the horizontal position
# of the player's ship. It will be adjusted
# when the user press left and right keys, and
# will be used by the draw_frame() function to draw
# the ship. The ship never moves vertically, so
# we don't need a variable to store its y position.
userx = 0

# This variable is a list of enemies currently in
# the game. Each enemy is represented by a tuple
# containing its x,y position as well as a string
# indicated the enemy's current direction of travel
# (either left or right). 
# Your final game should include more enemies, although
# the exact arrangement is up to you.
enemies = [(300,30, "left"), (-100,30, "left"), (-220, 30, "left"),\
           (-200,-100,'right'),(200,-100, 'right'),(-140,-100, 'right'),\
           (50,170,'right'),(-170,170, 'right'),(100,170, 'right')]

#create a new list of the enemies with left/right, deleting the ones clicked 
# This variable is a list of all bullets currently
# in the game. It is a list of tuples of (x,y)
# coordinates, one for each bullet. An elements will
# be added when a new bullet is fired, and removed
# when a bullet is destroyed (either by leaving
# the screen or by hitting an enemy).
bullets = []

# This variable is checked by the game's main
# loop to determine when it should end. When
# the game ends (either when the player's ship
# is destroyed, or when all enemies have been 
# destroyed), your code should set this variable
# to True, causing the main loop to end.
gameover = False

def draw_player_ship():
    """
    sig: () -> NoneType
    Draw the player's ship
    """
    """
    turtle.color("blue")
    turtle.penup()
    turtle.speed(0)
    turtle.setposition(0,280)
    turtle.penup
    """
    #player ship
    turtle.penup()
    turtle.setposition(0 + userx,280)
    turtle.pendown()
    turtle.color("blue","blue")
    turtle.begin_fill()
    for side in range(3):
        turtle.forward(30)
        turtle.right(120)
    turtle.end_fill()
    turtle.tracer(1)
    turtle.penup()
     
def draw_enemies():
    """
    sig: () -> NoneType
    Draw the enemies
    """
    turtle.color("red")
    turtle.penup()
    for (x,y,startx) in enemies:
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        #turtle.begin_fill()
        turtle.circle(10)
        #turtle.end_fill()
    turtle.penup()
    
def draw_bullets():
    """
    sig: () -> NoneType
    """
    for k in range(len(bullets)):
        turtle.setposition(bullets[k])
        turtle.pendown()
        turtle.color("green")
        turtle.circle(1)
        turtle.penup()
        bullets[k] = (bullets[k][0], bullets[k][1]-30)

def draw_status():
    """
    sig: () -> NoneType
    Draw the status info in the screen.
    It displays how many enemies left and the number of bullets used.
    """
    turtle.up()
    turtle.color("black")
    turtle.goto(-turtle.window_width()/2 + 10, turtle.window_height()/2 - 50)
    turtle.down()
    msg1 = "Enemies left: " + str(len(enemies))
    #msg = "\n".join([msg1,msg2])
    turtle.write(msg1, font=("Calibri", 10, "normal"))

def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the player's ship,
    the enemies, and the bullets.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    draw_player_ship()
    draw_enemies()
    draw_bullets()
    draw_status()
    
def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    userx.
    """
    global userx
    userx -= 15
    if userx < -360 + 5:
        print("Hit left")
        userx = -360 + 5
        
def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    user1x.
    """
    global userx
    userx += 15
    if userx > 360 - 35:
        print("Hit right")
        userx = 360 -35

        
def key_space():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the space key. It should
    add a new bullet to the list of bullets.
    """
    bullets.append((userx + 15, 275))
    # Bullet list only has the initial x,y values

def distance(first,second):
    a1 = first[0]
    a2 = first[1]
    b1 = second[0]
    b2 = second[1]
    d = ((a1-b1)**2 + (b1-a1)**2)**0.5
    print(d)
    if d < 20:
        return True            
    else:
        return False
    
def physics():
    """
    signature: () -> NoneType
    Update the state of the game world, as
    stored in the global variables. Here, you
    should check the positions of the bullets,
    and remove them if they go off the screen
    or collide with an enemy. In the later case
    you should also remove the enemy. That is,
    given the current position of the bullets,
    calculate their position in the next frame.
    """
    global bullets
    global enemies
    n = 0
    j = 0
    while n < len(bullets):
        if bullets[n][1] < -360:
            bullets.pop(n)
        while j < len(enemies):
            #print(distance(bullets[n], enemies[j]))
            if n < len(bullets) and j < len(enemies) and distance(bullets[n], enemies[j]):
                print(bullets[n], enemies[j])
                bullets.pop(n)
                enemies.pop(j)
            j += 1
        n += 1

def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by updating the position of the
    enemies, storied in the enemies global
    variable. That is, given their current
    position, calculate their position
    in the next frame.
    If the enemies reach the player's ship,
    you should set the gameover variable
    to True. Also, if there are no more
    enemies left, set gameover to True.
    """
    global enemies
    global gameover
    new_enemies = []
    w = turtle.window_width()
    for i in range(len(enemies)):
        if enemies[i][0] > 350:
            new_enemies.append((enemies[i][0]-10,enemies[i][1]+30,"left"))
            continue
        elif enemies[i][0] < -350:
            new_enemies.append((enemies[i][0]+10,enemies[i][1]+30,"right"))
            continue
        if enemies[i][2] == 'left':
            new_enemies.append((enemies[i][0]-10,enemies[i][1],"left"))
        elif enemies[i][2] == 'right':
            new_enemies.append((enemies[i][0]+10,enemies[i][1],"right"))
        if (enemies[i][0],enemies[i][1]) == (userx,280):
            gameover = True
        if len(enemies) == 0:
            gameover = True
    enemies = new_enemies.copy()

def reset():
    """
    signature: () -> NoneType
    This function is called when your game starts.
    It should set initial value for all the
    global variables.
    """
    global enemies
    global bullets
    global userx
    global gameover
    gameover = False
    bullets = []
    userx = 0
    enemies = [(300,30, "left"), (-100,30, "left"), (-220, 30, "left"),\
           (-200,-100,'right'),(200,-100, 'right'),(-140,-100, 'right'),\
           (50,170,'right'),(-170,170, 'right'),(100,170, 'right')]

def main():
    """
    signature: () -> NoneType
    Run the game. You shouldn't need to
    modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.onkey(key_space, "space")
    turtle.listen()
    reset()
    while not gameover:
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)

main()
