# libraries
import os
import random
from math import floor

from PIL import Image, ImageDraw

# Define constants
cnt = 0
num_images = 3
image_size = 120
num_points = 9
num_max_lines = 12
line_size = image_size / 2

# Define paths
dir = "images"
if not os.path.exists(dir):
    os.mkdir(dir)


# helper functions
def draw_basic_line(draw, x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), width=10, joint="curve")


# loop for each image
for i in range(num_images):
    # init
    num_lines = random.randrange(1, num_max_lines + 1)

    # image details
    im = Image.new('RGB', (image_size, image_size))
    draw = ImageDraw.Draw(im)

    # draw each line
    for j in range(num_lines):
        point_location = random.randrange(0, num_points)

        row = floor(point_location / 3)
        col = point_location % 3
        x1 = 5 + row * line_size / 2
        y1 = col * line_size / 2
        x2 = x1
        y2 = y1 + 20

        print("point: ", point_location)
        print("row: ", row, "col:", col)
        draw_basic_line(draw, x1, y1, x2, y2)

    # save image to file
    im.save(dir + "/test" + str(i + 1) + ".png")
    print(i + 1, "th image generated")
