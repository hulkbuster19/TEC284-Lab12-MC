# Import the api
from mcpi_addons.minecraft import Minecraft
# Initialize the api (MCPI must be open and in a world at
# this time)
mc = Minecraft.create()
mc.postToChat('Hello World!')

x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

#mc.player.setTile(x, y, z)

l = 10
h = 10
w = 10

mc.setBlocks(x, y, z, x + w, y + h, z +
l, 3)

mc.setBlocks(x, y, z, x + w -1, y + h -1, z + l -1, 0)