# libraries
import os
import random
from math import floor

from PIL import Image, ImageDraw

# Define constants
num_images = 30
num_min_lines = 3
num_max_lines = 4
square_size = 3

num_rows = square_size
num_cols = square_size
num_points = num_rows * num_cols
image_list = list()

line_size = 50
image_size = line_size * (num_rows - 1) + 10

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


def generate_coordinates():
    point_location = random.randrange(0, num_points)
    row = floor(point_location / 3)
    col = point_location % 3

    direction_set = get_direction_set(row, col)
    direction = random.choice(direction_set)

    return get_x_y_values(row, col, direction)


def check_to_regenerate(x1, y1, x2, y2, line_set, visited):
    if (x1, y1, x2, y2) in line_set:
        return True
    else:
        if (x1, y1) not in visited and (x2, y2) not in visited:
            return True
        else:
            return False


def generate_image(im):
    # init
    num_lines = random.randrange(num_min_lines, num_max_lines + 1)
    visited = set()
    line_set = set()

    draw = ImageDraw.Draw(im)

    # draw each line
    for j in range(num_lines):
        x1, y1, x2, y2 = generate_coordinates()
        if j == 0:
            visited.add((x1, y1))
            visited.add((x2, y2))
            line_set.add((x1, y1, x2, y2))
            line_set.add((x2, y2, x1, y1))

        else:
            while check_to_regenerate(x1, y1, x2, y2, line_set, visited):
                x1, y1, x2, y2 = generate_coordinates()

            visited.add((x1, y1))
            visited.add((x2, y2))
            line_set.add((x1, y1, x2, y2))
            line_set.add((x2, y2, x1, y1))
        draw_basic_line(draw, x1, y1, x2, y2)

    return list(line_set)


# loop for each image
for i in range(num_images):
    # image details
    im = Image.new('RGB', (image_size, image_size))
    image = generate_image(im)

    # save image to file
    if image not in image_list:
        im.save(dir + "/test" + str(i + 1) + ".png")
        image_list.append(image)
        print(i + 1, "th image generated")
    else:
        # im.save(dir + "/test" + str(i + 1) + "_dupe.png")
        print("dupe - did not generate")
    im.close()
