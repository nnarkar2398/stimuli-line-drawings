#libraries
from PIL import Image, ImageDraw, ImageColor

#image size
im = Image.new('RGB', (100, 100))


draw = ImageDraw.Draw(im)
#draw.line((0, 0) + im.size, fill= 0)
#draw.line((0, im.size[1], im.size[0], 0), fill= 0)
draw.line((0, 0, im.size[0], 0), width = 10, fill = (255, 255, 255), joint = "curve")
draw.line((0, 0, 0, im.size[1]), width = 10, fill = (255, 255, 255), joint = "curve")
draw.line((0, im.size[1], 50, im.size[1]), width = 10, fill = (255, 255, 255), joint = "curve")

im.save('test1.png')

im2 = Image.new('RGB', (100, 100))
draw2 = ImageDraw.Draw(im2)
#draw.line((0, 0) + im.size, fill= 0)
#draw.line((0, im.size[1], im.size[0], 0), fill= 0)
draw2.line((0, 0, 45, 0), width = 8, fill = (255, 255, 255))
draw2.line((45, 2, 90, 2), width = 8, fill = (255, 255, 255))
draw2.line((90, 2, 90, 45), width = 8, fill = (255, 255, 255))
draw2.line((2, 2, 2, 45), width = 8, fill = (255, 255, 255))
draw2.line((45, 2, 45, 45), width = 8, fill = (255, 255, 255))
draw2.line((2, 45, 2, 90), width = 8, fill = (255, 255, 255))
draw2.line((0, 90, 45, 90), width = 8, fill = (255, 255, 255))

im2.save('test2.png')
