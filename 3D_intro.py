from ursina import *

app = Ursina()

from ursina.prefabs.first_person_controller import FirstPersonController

player = FirstPersonController(model = 'cube',collider = 'box')
ground = Entity(model = 'plane',
                collider ='box',
                scale = (50,1,50),
                color = color.light_gray,
                texture = 'white_cube',
                texture_scale = (50,50))



app.run()

#LEARNING INTENTIONS:
#1. Create a player (first person controller)
#2. Create ground (plane)
#3. Demonstrate movement in 3D space
