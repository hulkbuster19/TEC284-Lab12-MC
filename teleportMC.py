# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MCPI must be open and in a world at
# this time)
mc = Minecraft.create()
mc.postToChat('Hello World!')

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

mc.player.setTile(x, y, z)