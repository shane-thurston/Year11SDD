from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

#LEARNING INTENTIONS:
#1. Create a set of unique but randomised locations
locations = set()
for i in range(0,300):
    x = random.randint(-24,24)
    y = 0
    z = random.randint(-24,24)
    locations.add((x,y,z))
    
finish_location = random.choice(list(locations))
locations.remove(finish_location)
    


#2. Assign one location for finish and the rest for the obstacles
#3. Create all the obstacles

finish = Entity(model = 'cube',
                collider= 'box',
                scale = (2,2,2),
                color = color.green,
                position = finish_location)

player = FirstPersonController(model = 'cube',collider = 'box')

ground = Entity(model = 'plane',
                collider ='box',
                scale = (50,1,50),
                color = color.light_gray,
                texture = 'white_cube',
                texture_scale = (50,50))

for loc in locations:
    cube_width = random.randrange(1,3)
    cube_height = random.randrange(2,8)
    cube_depth = random.randrange(1,3)
    obstacle = Entity(model = 'cube',
                      scale = (cube_width, cube_height, cube_depth),
                      position = loc,
                      collider = 'box',
                      color = color.yellow,
                      texture = 'brick',)


def update():
    hit_info = player.intersects()
    if hit_info.hit:
        if hit_info.entity == finish:
            message  = Text(text = 'YOU WON', scale = 2, origin = (0,0), background = True, color = color.blue)
            application.pause()
            mouse.locked = False
            
app.run()
