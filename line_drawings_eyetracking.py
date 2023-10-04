# libraries
import os
import random
from math import floor

from PIL import Image, ImageDraw

# Define constants
cnt = 0
num_images = 9
image_size = 120
num_rows = 3
num_cols = 3
num_points = num_rows * num_cols
num_max_lines = 12
line_size = (image_size - 10) / 2
directions = ["left", "right", "up", "down"]
directionsTopLeftCorner = ["right", "down"]
directionsTopRightCorner = ["left", "down"]
directionsBottomRightCorner = ["left", "up"]
directionsBottomLeftCorner = ["right", "up"]
directionsTopEdge = ["left", "right", "down"]
directionsBottomEdge = ["left", "right", "up"]
directionsLeftEdge = ["right", "up", "down"]
directionsRightEdge = ["left", "up", "down"]

# Define paths
dir = "images"
if not os.path.exists(dir):
    os.mkdir(dir)


# helper functions
def draw_basic_line(draw, x1, y1, x2, y2):
    draw.line((x1, y1, x2, y2), width=5, joint="curve")


def get_direction_set(row, col):
    if row == 0 and col == 0:
        return directionsTopLeftCorner
    elif row == 0 and col == num_cols - 1:
        return directionsTopRightCorner
    elif row == num_rows - 1 and col == 0:
        return directionsBottomLeftCorner
    elif row == num_rows - 1 and col == num_cols - 1:
        return directionsBottomRightCorner
    elif row == 0:
        return directionsTopEdge
    elif row == num_rows - 1:
        return directionsBottomEdge
    elif col == 0:
        return directionsLeftEdge
    elif col == num_cols - 1:
        return directionsRightEdge
    else:
        return directions


def get_x_y_values(row_xy, col_xy, direction_xy):
    p_x1 = 5 + col_xy * line_size
    p_y1 = 5 + row_xy * line_size

    if direction_xy == "left":
        p_x2 = p_x1 - line_size
        p_y2 = p_y1
    elif direction_xy == "up":
        p_x2 = p_x1
        p_y2 = p_y1 - line_size
    elif direction_xy == "right":
        p_x2 = p_x1 + line_size
        p_y2 = p_y1
    else:  # case for down
        p_x2 = p_x1
        p_y2 = p_y1 + line_size

    return p_x1, p_y1, p_x2, p_y2


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

        directionSet = get_direction_set(row, col)
        direction = random.choice(directionSet)
        print(direction)

        x1, y1, x2, y2 = get_x_y_values(row, col, direction)
        draw_basic_line(draw, x1, y1, x2, y2)

    # save image to file
    im.save(dir + "/test" + str(i + 1) + ".png")
    print(i + 1, "th image generated")
