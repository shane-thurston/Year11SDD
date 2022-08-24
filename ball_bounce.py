#LEARNING INTENTIONS
#2. Create a collsion so that the ball bounces off the square

from ursina import *
app = Ursina()

#1. Create a second entity Ball (IMPORTANT NOTE: change dx and dy to suit your computer performance)
ball = Entity(model = 'circle', scale = 0.2, position = (-3,0,0), collider = 'box', dx = 0.07, dy = 0.07, color = color.yellow)

#2. Create the four walls
ceiling = Entity(model = 'quad',color = color.blue, scale = (15,0.2), position = (0,4,0), collider = 'box')
left_wall = Entity(model = 'quad',color = color.blue, scale = (0.2,10), position = (-7.2,0,0), collider = 'box')
right_wall = Entity(model = 'quad',color = color.blue, scale = (0.2,10), position = (7.2,0,0), collider = 'box')

#3. Create a wall of bricks
bricks = []
for x_pos in range(0,14):
    for y_pos in range(3,7):
        brick = Entity(model = 'quad', scale = (0.9,0.25), x = x_pos-6.5, y= 0.5+ y_pos/3, collider = 'box', color = color.red)
        bricks.append(brick)

#4. Creating a paddle (player)
paddle = Entity(model = 'quad', scale = (2,0.25), position = (0,-3.6,0), collider = 'box', color = color.green)


app.run()
