# Import required libraries
from time import sleep
import random
from colorama import Fore, Back, Style

# Define color representations for the cube faces
orange = Style.BRIGHT + Fore.LIGHTRED_EX + 'o' + Style.RESET_ALL
red = Fore.RED + 'r' + Style.RESET_ALL
green = Fore.GREEN + 'g' + Style.RESET_ALL
yellow = Fore.YELLOW + 'y' + Style.RESET_ALL
blue = Fore.BLUE + 'b' + Style.RESET_ALL
white = 'w'

# Define spacing for cube visualization
space = '       '

# Define face colors
green, orange, white, red, yellow, blue = 'g', 'o', 'w', 'r', 'y', 'b'
print(green, orange, white, red, yellow, blue)

# Initialize cube faces
GREEN, ORANGE, WHITE, RED, YELLOW, BLUE = [], [], [], [], [], []
for _ in range(9):
    GREEN.append(green)
    ORANGE.append(orange)
    WHITE.append(white)
    RED.append(red)
    YELLOW.append(yellow)
    BLUE.append(blue)

# Define cube rotation functions

def rotate_white_clockwise():
    # Rotate the white face clockwise
    temp = WHITE[1]
    WHITE[1], WHITE[3], WHITE[7], WHITE[5] = WHITE[3], WHITE[7], WHITE[5], temp

    temp = WHITE[0]
    WHITE[0], WHITE[6], WHITE[8], WHITE[2] = WHITE[6], WHITE[8], WHITE[2], temp

    # Update adjacent face edges
    temp = GREEN[8]
    GREEN[8], RED[2], BLUE[0], ORANGE[6] = RED[2], BLUE[0], ORANGE[6], temp

    temp = GREEN[7]
    GREEN[7], RED[5], BLUE[1], ORANGE[3] = RED[5], BLUE[1], ORANGE[3], temp

    temp = GREEN[6]
    GREEN[6], RED[8], BLUE[2], ORANGE[0] = RED[8], BLUE[2], ORANGE[0], temp

def rotate_white_counterclockwise():
    # Rotate the white face counterclockwise
    temp = WHITE[5]
    WHITE[3], WHITE[7], WHITE[5], WHITE[1] = WHITE[1], WHITE[3], WHITE[7], temp

    temp = WHITE[2]
    WHITE[6], WHITE[8], WHITE[2], WHITE[0] = WHITE[0], WHITE[6], WHITE[8], temp

    # Update adjacent face edges
    temp = ORANGE[6]
    RED[2], BLUE[0], ORANGE[6], GREEN[8] = GREEN[8], RED[2], BLUE[0], temp

    temp = ORANGE[3]
    RED[5], BLUE[1], ORANGE[3], GREEN[7] = GREEN[7], RED[5], BLUE[1], temp

    temp = ORANGE[0]
    RED[8], BLUE[2], ORANGE[0], GREEN[6] = GREEN[6], RED[8], BLUE[2], temp

def rotate_yellow_clockwise():
    # Rotate the yellow face clockwise
    temp = YELLOW[1]
    YELLOW[1], YELLOW[3], YELLOW[7], YELLOW[5] = YELLOW[3], YELLOW[7], YELLOW[5], temp

    temp = YELLOW[0]
    YELLOW[0], YELLOW[6], YELLOW[8], YELLOW[2] = YELLOW[6], YELLOW[8], YELLOW[2], temp

    # Update adjacent face edges
    temp = GREEN[2]
    GREEN[2], ORANGE[8], BLUE[6], RED[0] = ORANGE[8], BLUE[6], RED[0], temp

    temp = GREEN[1]
    GREEN[1], ORANGE[5], BLUE[7], RED[3] = ORANGE[5], BLUE[7], RED[3], temp

    temp = GREEN[0]
    GREEN[0], ORANGE[2], BLUE[8], RED[6] = ORANGE[2], BLUE[8], RED[6], temp

def rotate_yellow_counterclockwise():
    # Rotate the yellow face counterclockwise
    temp = YELLOW[5]
    YELLOW[3], YELLOW[7], YELLOW[5], YELLOW[1] = YELLOW[1], YELLOW[3], YELLOW[7], temp

    temp = YELLOW[2]
    YELLOW[6], YELLOW[8], YELLOW[2], YELLOW[0] = YELLOW[0], YELLOW[6], YELLOW[8], temp

    # Update adjacent face edges
    temp = RED[0]
    ORANGE[8], BLUE[6], RED[0], GREEN[2] = GREEN[2], ORANGE[8], BLUE[6], temp

    temp = RED[3]
    ORANGE[5], BLUE[7], RED[3], GREEN[1] = GREEN[1], ORANGE[5], BLUE[7], temp

    temp = RED[6]
    ORANGE[2], BLUE[8], RED[6], GREEN[0] = GREEN[0], ORANGE[2], BLUE[8], temp

def rotate_orange_clockwise():
    # Rotate the orange face clockwise
    temp = ORANGE[1]
    ORANGE[1], ORANGE[3], ORANGE[7], ORANGE[5] = ORANGE[3], ORANGE[7], ORANGE[5], temp

    temp = ORANGE[0]
    ORANGE[0], ORANGE[6], ORANGE[8], ORANGE[2] = ORANGE[6], ORANGE[8], ORANGE[2], temp

    # Update adjacent face edges
    temp = WHITE[2]
    YELLOW[6], BLUE[2], WHITE[2], GREEN[2] = GREEN[2], YELLOW[6], BLUE[2], temp

    temp = WHITE[8]
    YELLOW[0], BLUE[8], WHITE[8], GREEN[8] = GREEN[8], YELLOW[0], BLUE[8], temp

    temp = WHITE[5]
    YELLOW[3], BLUE[5], WHITE[5], GREEN[5] = GREEN[5], YELLOW[3], BLUE[5], temp

def rotate_orange_counterclockwise():
    # Rotate the orange face counterclockwise
    temp = ORANGE[5]
    ORANGE[3], ORANGE[7], ORANGE[5], ORANGE[1] = ORANGE[1], ORANGE[3], ORANGE[7], temp

    temp = ORANGE[2]
    ORANGE[6], ORANGE[8], ORANGE[2], ORANGE[0] = ORANGE[0], ORANGE[6], ORANGE[8], temp

    # Update adjacent face edges
    temp = GREEN[2]
    GREEN[2], YELLOW[6], BLUE[2], WHITE[2] = YELLOW[6], BLUE[2], WHITE[2], temp

    temp = GREEN[8]
    GREEN[8], YELLOW[0], BLUE[8], WHITE[8] = YELLOW[0], BLUE[8], WHITE[8], temp

    temp = GREEN[5]
    GREEN[5], YELLOW[3], BLUE[5], WHITE[5] = YELLOW[3], BLUE[5], WHITE[5], temp

def rotate_red_clockwise():
    # Rotate the red face clockwise
    temp = RED[1]
    RED[1], RED[3], RED[7], RED[5] = RED[3], RED[7], RED[5], temp

    temp = RED[0]
    RED[0], RED[6], RED[8], RED[2] = RED[6], RED[8], RED[2], temp

    # Update adjacent face edges
    temp = GREEN[0]
    GREEN[0], YELLOW[8], BLUE[0], WHITE[0] = YELLOW[8], BLUE[0], WHITE[0], temp

    temp = GREEN[3]
    GREEN[3], YELLOW[5], BLUE[3], WHITE[3] = YELLOW[5], BLUE[3], WHITE[3], temp

    temp = GREEN[6]
    GREEN[6], YELLOW[2], BLUE[6], WHITE[6] = YELLOW[2], BLUE[6], WHITE[6], temp

def rotate_red_counterclockwise():
    # Rotate the red face counterclockwise
    temp = RED[5]
    RED[3], RED[7], RED[5], RED[1] = RED[1], RED[3], RED[7], temp

    temp = RED[2]
    RED[6], RED[8], RED[2], RED[0] = RED[0], RED[6], RED[8], temp

    # Update adjacent face edges
    temp = WHITE[0]
    YELLOW[8], BLUE[0], WHITE[0], GREEN[0] = GREEN[0], YELLOW[8], BLUE[0], temp

    temp = WHITE[3]
    YELLOW[5], BLUE[3], WHITE[3], GREEN[3] = GREEN[3], YELLOW[5], BLUE[3], temp

    temp = WHITE[6]
    YELLOW[2], BLUE[6], WHITE[6], GREEN[6] = GREEN[6], YELLOW[2], BLUE[6], temp


def rotate_green_clockwise():
    # Rotate the green face clockwise
    temp = GREEN[1]
    GREEN[1], GREEN[3], GREEN[7], GREEN[5] = GREEN[3], GREEN[7], GREEN[5], temp

    temp = GREEN[0]
    GREEN[0], GREEN[6], GREEN[8], GREEN[2] = GREEN[6], GREEN[8], GREEN[2], temp

    # Update adjacent face edges
    temp = RED[0]
    RED[0], WHITE[0], ORANGE[0], YELLOW[0] = WHITE[0], ORANGE[0], YELLOW[0], temp

    temp = RED[1]
    RED[1], WHITE[1], ORANGE[1], YELLOW[1] = WHITE[1], ORANGE[1], YELLOW[1], temp

    temp = RED[2]
    RED[2], WHITE[2], ORANGE[2], YELLOW[2] = WHITE[2], ORANGE[2], YELLOW[2], temp


def rotate_green_counterclockwise():
    # Rotate the green face counterclockwise
    temp = GREEN[5]
    GREEN[3], GREEN[7], GREEN[5], GREEN[1] = GREEN[1], GREEN[3], GREEN[7], temp

    temp = GREEN[2]
    GREEN[6], GREEN[8], GREEN[2], GREEN[0] = GREEN[0], GREEN[6], GREEN[8], temp

    # Update adjacent face edges
    temp = YELLOW[0]
    WHITE[0], ORANGE[0], YELLOW[0], RED[0] = RED[0], WHITE[0], ORANGE[0], temp

    temp = YELLOW[1]
    WHITE[1], ORANGE[1], YELLOW[1], RED[1] = RED[1], WHITE[1], ORANGE[1], temp

    temp = YELLOW[2]
    WHITE[2], ORANGE[2], YELLOW[2], RED[2] = RED[2], WHITE[2], ORANGE[2], temp


def rotate_blue_clockwise():
    # Rotate the blue face clockwise
    temp = BLUE[1]
    BLUE[1], BLUE[3], BLUE[7], BLUE[5] = BLUE[3], BLUE[7], BLUE[5], temp

    temp = BLUE[0]
    BLUE[0], BLUE[6], BLUE[8], BLUE[2] = BLUE[6], BLUE[8], BLUE[2], temp

    # Update adjacent face edges
    temp = YELLOW[6]
    WHITE[6], ORANGE[6], YELLOW[6], RED[6] = RED[6], WHITE[6], ORANGE[6], temp

    temp = YELLOW[7]
    WHITE[7], ORANGE[7], YELLOW[7], RED[7] = RED[7], WHITE[7], ORANGE[7], temp

    temp = YELLOW[8]
    WHITE[8], ORANGE[8], YELLOW[8], RED[8] = RED[8], WHITE[8], ORANGE[8], temp


def rotate_blue_counterclockwise():
    # Rotate the blue face counterclockwise
    temp = BLUE[5]
    BLUE[3], BLUE[7], BLUE[5], BLUE[1] = BLUE[1], BLUE[3], BLUE[7], temp

    temp = BLUE[2]
    BLUE[6], BLUE[8], BLUE[2], BLUE[0] = BLUE[0], BLUE[6], BLUE[8], temp

    # Update adjacent face edges
    temp = RED[6]
    RED[6], WHITE[6], ORANGE[6], YELLOW[6] = WHITE[6], ORANGE[6], YELLOW[6], temp

    temp = RED[7]
    RED[7], WHITE[7], ORANGE[7], YELLOW[7] = WHITE[7], ORANGE[7], YELLOW[7], temp

    temp = RED[8]
    RED[8], WHITE[8], ORANGE[8], YELLOW[8] = WHITE[8], ORANGE[8], YELLOW[8], temp


def solve_green_daisy(green_position):
    if green_position == 0:
        rotate_green_clockwise()
        rotate_orange_clockwise()
        rotate_green_counterclockwise()
    elif green_position == 1:
        rotate_red_counterclockwise()
    elif green_position == 2:
        rotate_orange_clockwise()
    elif green_position == 3:
        rotate_green_clockwise()
        rotate_red_counterclockwise()
        rotate_green_counterclockwise()


def solve_orange_daisy(orange_position):
    if orange_position == 2:
        rotate_orange_clockwise()
        rotate_blue_clockwise()
        rotate_orange_counterclockwise()
    elif orange_position == 0:
        rotate_green_counterclockwise()
    elif orange_position == 3:
        rotate_blue_clockwise()
    elif orange_position == 1:
        rotate_orange_clockwise()
        rotate_green_counterclockwise()
        rotate_orange_counterclockwise()


def solve_blue_daisy(blue_position):
    if blue_position == 3:
        rotate_blue_clockwise()
        rotate_red_clockwise()
        rotate_blue_counterclockwise()
    elif blue_position == 2:
        rotate_orange_counterclockwise()
    elif blue_position == 1:
        rotate_red_clockwise()
    elif blue_position == 0:
        rotate_blue_clockwise()
        rotate_orange_counterclockwise()
        rotate_blue_counterclockwise()


def solve_red_daisy(red_position):
    if red_position == 1:
        rotate_red_clockwise()
        rotate_green_clockwise()
        rotate_red_counterclockwise()
    elif red_position == 3:
        rotate_blue_counterclockwise()
    elif red_position == 0:
        rotate_green_clockwise()
    elif red_position == 2:
        rotate_red_clockwise()
        rotate_blue_counterclockwise()
        rotate_red_counterclockwise()


def orient_last_layer(cross_type):
    if cross_type == 0:
        # Algorithm for OLL when no edges are oriented correctly
        rotate_blue_clockwise()
        rotate_red_clockwise()
        rotate_yellow_clockwise()
        rotate_red_counterclockwise()
        rotate_yellow_counterclockwise()
        rotate_red_clockwise()
        rotate_yellow_clockwise()
        rotate_red_counterclockwise()
        rotate_yellow_counterclockwise()
        rotate_blue_counterclockwise()
        rotate_yellow_clockwise()
        rotate_blue_clockwise()
        rotate_red_clockwise()
        rotate_yellow_clockwise()
        rotate_red_counterclockwise()
        rotate_yellow_counterclockwise()
        rotate_blue_counterclockwise()


def solve_daisy(GREEN, ORANGE, WHITE, RED, YELLOW, BLUE):
    daisy_solved = False
    attempts = 1
    while not daisy_solved:
        white_edge = (WHITE[1], WHITE[3], WHITE[5], WHITE[7])
        green_edge = (GREEN[1], GREEN[3], GREEN[5], GREEN[7])
        orange_edge = (ORANGE[1], ORANGE[3], ORANGE[5], ORANGE[7])
        red_edge = (RED[1], RED[3], RED[5], RED[7])
        blue_edge = (BLUE[1], BLUE[3], BLUE[5], BLUE[7])

        white_edge_moves = [rotate_green_clockwise, rotate_red_clockwise, rotate_orange_clockwise, rotate_blue_clockwise]

        # Move white edges from the white face to the yellow face
        if 'w' in white_edge:
            for i, edge in enumerate(white_edge):
                if edge == 'w':
                    white_edge_moves[i]()
                    white_edge_moves[i]()

        # Solve white edges on other faces
        for i, edge in enumerate(green_edge):
            if edge == 'w':
                solve_green_daisy(i)

        for i, edge in enumerate(orange_edge):
            if edge == 'w':
                solve_orange_daisy(i)

        for _ in range(random.randrange(1, 3)):
            rotate_yellow_counterclockwise()

        for i, edge in enumerate(blue_edge):
            if edge == 'w':
                solve_blue_daisy(i)

        for i, edge in enumerate(red_edge):
            if edge == 'w':
                solve_red_daisy(i)

        if YELLOW[1] == 'w' and YELLOW[3] == 'w' and YELLOW[5] == 'w' and YELLOW[7] == 'w':
            print(f"Daisy solved in {attempts} attempts")
            daisy_solved = True
        else:
            attempts += 1
            #sleep(.1)
            #visualize_cube()


def solve_white_cross(GREEN, ORANGE, WHITE, RED, YELLOW, BLUE):
    # Solve the white cross
    for _ in range(4):
        if GREEN[1] == 'g' and YELLOW[1] == 'w':
            rotate_green_clockwise()
            rotate_green_clockwise()
            break
        else:
            rotate_yellow_clockwise()

    for _ in range(4):
        if ORANGE[5] == 'o' and YELLOW[3] == 'w':
            rotate_orange_clockwise()
            rotate_orange_clockwise()
            break
        else:
            rotate_yellow_clockwise()

    for _ in range(4):
        if BLUE[7] == 'b' and YELLOW[7] == 'w':
            rotate_blue_clockwise()
            rotate_blue_clockwise()
            break
        else:
            rotate_yellow_clockwise()

    for _ in range(4):
        if RED[3] == 'r' and YELLOW[5] == 'w':
            rotate_red_clockwise()
            rotate_red_clockwise()
            break
        else:
            rotate_yellow_clockwise()


def solve_white_face(Green, Orange, White, Red, Yellow, Blue):
    # This function solves the white face of the Rubik's cube by positioning white corner pieces correctly

    while True:
        # Check the green-orange-yellow and green-orange-white corners
        green_orange_yellow_corner = (Green[2], Orange[2], Yellow[0])
        green_orange_white_corner = (Green[8], Orange[0], White[2])

        # If white is in any of the corners, adjust its position
        if 'w' in green_orange_white_corner or 'w' in green_orange_yellow_corner:
            if White[2] == 'w':  # If the white piece is already in place
                break
            else:
                # Keep rotating until white is aligned
                while White[2] != 'w':
                    rotate_orange_clockwise();
                    rotate_yellow_clockwise();
                    rotate_orange_counterclockwise();
                    rotate_yellow_counterclockwise()
        else:
            rotate_yellow_clockwise()  # Rotate the top layer to search for white

    while True:
        # Check the orange-blue-yellow and orange-blue-white corners
        orange_blue_yellow_corner = (Orange[8], Blue[8], Yellow[6])
        orange_blue_white_corner = (Orange[6], Blue[2], White[8])

        if 'w' in orange_blue_yellow_corner or 'w' in orange_blue_white_corner:
            if White[8] == 'w':  # White piece is in place
                break
            else:
                while White[8] != 'w':
                    rotate_blue_clockwise();
                    rotate_yellow_clockwise();
                    rotate_blue_counterclockwise();
                    rotate_yellow_counterclockwise()
        else:
            rotate_yellow_clockwise()

    while True:
        # Check the blue-red-yellow and blue-red-white corners
        blue_red_yellow_corner = (Blue[6], Red[6], Yellow[8])
        blue_red_white_corner = (Blue[0], Red[8], White[6])

        if 'w' in blue_red_yellow_corner or 'w' in blue_red_white_corner:
            if White[6] == 'w':
                break
            else:
                while White[6] != 'w':
                    rotate_red_clockwise();
                    rotate_yellow_clockwise();
                    rotate_red_counterclockwise();
                    rotate_yellow_counterclockwise()
        else:
            rotate_yellow_clockwise()

    while True:
        # Check the red-green-yellow and red-green-white corners
        red_green_yellow_corner = (Red[0], Green[0], Yellow[2])
        red_green_white_corner = (Red[2], Green[6], White[0])

        if 'w' in red_green_yellow_corner or 'w' in red_green_white_corner:
            if White[0] == 'w':
                break
            else:
                while White[0] != 'w':
                    rotate_green_clockwise();
                    rotate_yellow_clockwise();
                    rotate_green_counterclockwise();
                    rotate_yellow_counterclockwise()
        else:
            rotate_yellow_clockwise()

    # Correct the orientation of the white corners
    while True:
        # Check if the green edge piece is in the correct position
        if Green[8] == "g":  # If the green face is aligned correctly
            break
        elif Orange[6] == "g":  # If orange face contains the green piece, move it to the correct face
            rotate_blue_clockwise();
            rotate_yellow_clockwise();
            rotate_blue_counterclockwise();
            rotate_orange_counterclockwise()
            rotate_green_clockwise();
            rotate_orange_clockwise();
            rotate_green_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_orange_clockwise();
            rotate_blue_counterclockwise();
            rotate_orange_counterclockwise();
            rotate_blue_clockwise()
            break
        elif Blue[0] == "g":  # If blue face contains the green piece
            rotate_orange_clockwise();
            rotate_red_clockwise();
            rotate_yellow_clockwise();
            rotate_yellow_clockwise()
            rotate_orange_counterclockwise();
            rotate_red_counterclockwise()
            break
        elif Red[2] == "g":  # If red face contains the green piece
            rotate_orange_clockwise();
            rotate_yellow_clockwise();
            rotate_orange_counterclockwise()
            rotate_green_counterclockwise();
            rotate_red_clockwise();
            rotate_green_clockwise()
            rotate_red_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_green_clockwise();
            rotate_orange_counterclockwise();
            rotate_green_counterclockwise();
            rotate_orange_clockwise()
            break
    while True:
        # Check if the orange edge piece is in the correct position
        if Orange[6] == "o":
            break
        elif Blue[0] == "o": # If the blue face has the orange edge, reposition it
            rotate_red_clockwise();
            rotate_yellow_clockwise();
            rotate_red_counterclockwise();
            rotate_blue_counterclockwise()
            rotate_orange_clockwise();
            rotate_blue_clockwise();
            rotate_orange_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_blue_clockwise();
            rotate_red_counterclockwise();
            rotate_blue_counterclockwise();
            rotate_red_clockwise()
            break

        elif Red[2] == "o": # If the red face has the orange edge
            rotate_blue_clockwise();
            rotate_green_clockwise();
            rotate_yellow_clockwise();
            rotate_yellow_clockwise()
            rotate_blue_counterclockwise();
            rotate_green_counterclockwise()
            break

    while True:
        # Check if the blue edge piece is in the correct position
        if Blue[0] == "b":
            break

        else: # If the blue edge is not in the correct position
            rotate_green_clockwise();
            rotate_yellow_clockwise();
            rotate_green_counterclockwise();
            rotate_red_counterclockwise()
            rotate_blue_clockwise();
            rotate_red_clockwise(); rotate_blue_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_red_clockwise();
            rotate_green_counterclockwise();
            rotate_red_counterclockwise();
            rotate_green_clockwise()


def solve_second_layer(Green, Orange, White, Red, Yellow, Blue):
    # Solve the second layer by positioning the edge pieces correctly

    while True:
        green_top_edge = (Green[1], Yellow[1])  # Check the green-yellow edge

        if Green[5] == 'g' and Orange[1] == 'o':
            break
        if Green[5] == 'y' or Orange[1] == 'y':
            break
        if 'y' in green_top_edge:
            rotate_yellow_clockwise();
            rotate_orange_clockwise();
            rotate_yellow_clockwise()
            rotate_orange_counterclockwise();
            rotate_yellow_counterclockwise();
            rotate_green_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_green_clockwise()
        rotate_yellow_clockwise()

    while True:
        orange_top_edge = (Orange[5], Yellow[3])  # Check the orange-yellow edge

        if Orange[7] == 'o' and Blue[5] == 'b':
            break
        if Orange[7] == 'y' or Blue[5] == 'y':
            break
        if 'y' in orange_top_edge:
            rotate_yellow_clockwise();
            rotate_blue_clockwise();
            rotate_yellow_clockwise()
            rotate_blue_counterclockwise();
            rotate_yellow_counterclockwise();
            rotate_orange_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_orange_clockwise()
        rotate_yellow_clockwise()

    while True:
        blue_top_edge = (Blue[7], Yellow[7])  # Check the blue-yellow edge

        if Blue[3] == 'b' and Red[7] == 'r':
            break
        if Blue[3] == 'y' or Red[7] == 'y':
            break
        if 'y' in blue_top_edge:
            rotate_yellow_clockwise();
            rotate_red_clockwise();
            rotate_yellow_clockwise()
            rotate_red_counterclockwise();
            rotate_yellow_counterclockwise();
            rotate_blue_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_blue_clockwise()
        rotate_yellow_clockwise()

    while True:
        red_top_edge = (Red[3], Yellow[5])  # Check the red-yellow edge

        if Red[1] == 'r' and Green[3] == 'g':
            break
        if Red[1] == 'y' or Green[3] == 'y':
            break
        if 'y' in red_top_edge:
            rotate_yellow_clockwise();
            rotate_green_clockwise();
            rotate_yellow_clockwise()
            rotate_green_counterclockwise();
            rotate_yellow_counterclockwise();
            rotate_red_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_red_clockwise()
        rotate_yellow_clockwise()

    # Now we correct misaligned pieces by inserting them into the second layer
    while True:
        if Green[5] == 'g' and Orange[1] == 'o':
            break
        if Green[1] == 'g' and Yellow[1] == 'o':
            rotate_yellow_clockwise();
            rotate_orange_clockwise();
            rotate_yellow_clockwise()
            rotate_orange_counterclockwise();
            rotate_yellow_counterclockwise();
            rotate_green_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_green_clockwise()
            break
        if Orange[5] == 'o' and Yellow[3] == 'g':
            rotate_yellow_counterclockwise();
            rotate_green_counterclockwise();
            rotate_yellow_clockwise()
            rotate_green_clockwise();
            rotate_orange_counterclockwise();
            rotate_green_clockwise();
            rotate_orange_clockwise();
            rotate_green_counterclockwise()
            break
        rotate_yellow_clockwise()

    while True:
        if Orange[7] == 'o' and Blue[5] == 'b':
            break
        if Orange[5] == 'o' and Yellow[3] == 'b':
            rotate_yellow_clockwise();
            rotate_blue_clockwise();
            rotate_yellow_clockwise()
            rotate_blue_counterclockwise();
            rotate_yellow_counterclockwise();
            rotate_orange_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_orange_clockwise()
            break
        if Blue[7] == 'b' and Yellow[7] == 'o':
            rotate_yellow_counterclockwise();
            rotate_orange_counterclockwise();
            rotate_yellow_clockwise()
            rotate_orange_clockwise();
            rotate_blue_counterclockwise();
            rotate_orange_clockwise();
            rotate_blue_clockwise();
            rotate_orange_counterclockwise()
            break
        rotate_yellow_clockwise()

    while True:
        if Blue[3] == 'b' and Red[7] == 'r':
            break
        if Blue[7] == 'b' and Yellow[7] == 'r':
            rotate_yellow_clockwise();
            rotate_red_clockwise();
            rotate_yellow_clockwise()
            rotate_red_counterclockwise();
            rotate_yellow_counterclockwise();
            rotate_blue_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_blue_clockwise()
            break
        if Red[3] == 'r' and Yellow[5] == 'b':
            rotate_yellow_counterclockwise();
            rotate_blue_counterclockwise();
            rotate_yellow_clockwise()
            rotate_blue_clockwise();
            rotate_red_counterclockwise();
            rotate_blue_clockwise();
            rotate_red_clockwise();
            rotate_blue_counterclockwise()
            break
        rotate_yellow_clockwise()

    while True:
        if Red[1] == 'r' and Green[3] == 'g':
            break
        if Red[3] == 'r' and Yellow[5] == 'g':
            rotate_yellow_clockwise();
            rotate_green_clockwise();
            rotate_yellow_clockwise()
            rotate_green_counterclockwise();
            rotate_yellow_counterclockwise();
            rotate_red_counterclockwise();
            rotate_yellow_counterclockwise()
            rotate_red_clockwise()
            break
        if Green[1] == 'g' and Yellow[1] == 'r':
            rotate_yellow_counterclockwise();
            rotate_red_counterclockwise();
            rotate_yellow_clockwise()
            rotate_red_clockwise();
            rotate_green_counterclockwise();
            rotate_red_clockwise();
            rotate_green_clockwise();
            rotate_red_counterclockwise()
            break
        rotate_yellow_clockwise()





def visualize_cube():
    # Display the current state of the cube
    print(space)
    print(space, sides, GREEN[0], GREEN[1], GREEN[2], sides)
    print(space, sides, GREEN[3], GREEN[4], GREEN[5], sides)
    print(space, sides, GREEN[6], GREEN[7], GREEN[8], sides)
    print(sides, RED[0], RED[1], RED[2], sides, WHITE[0], WHITE[1], WHITE[2], sides, ORANGE[0], ORANGE[1], ORANGE[2], sides, YELLOW[0], YELLOW[1], YELLOW[2], sides)
    print(sides, RED[3], RED[4], RED[5], sides, WHITE[3], WHITE[4], WHITE[5], sides, ORANGE[3], ORANGE[4], ORANGE[5], sides, YELLOW[3], YELLOW[4], YELLOW[5], sides)
    print(sides, RED[6], RED[7], RED[8], sides, WHITE[6], WHITE[7], WHITE[8], sides, ORANGE[6], ORANGE[7], ORANGE[8], sides, YELLOW[6], YELLOW[7], YELLOW[8], sides)
    print(space, sides, BLUE[0], BLUE[1], BLUE[2], sides)
    print(space, sides, BLUE[3], BLUE[4], BLUE[5], sides)
    print(space, sides, BLUE[6], BLUE[7], BLUE[8], sides)


def scramble_cube(num_moves):
    # Scramble the cube with a given number of random moves
    scramble_sequence = []
    for i in range(num_moves):
        move = random.randint(1, 12)
        if len(scramble_sequence) > 0:
            # Avoid immediate reverse moves
            if move % 2 != 0 and scramble_sequence[i-1] == move + 1:
                move += 1
            elif move % 2 == 0 and scramble_sequence[i-1] == move - 1:
                move -= 1
        if len(scramble_sequence) > 1:
            # Avoid three consecutive identical moves
            if move == scramble_sequence[i-1] and scramble_sequence[i-1] == scramble_sequence[i-2]:
                move += 1

        move = 12 if move == 0 else 1 if move == 13 else move

        scramble_sequence.append(move)

    # Execute the scramble moves
    move_mapping = {
        1: (rotate_white_clockwise, "F"),
        2: (rotate_white_counterclockwise, "F'"),
        3: (rotate_yellow_clockwise, "B"),
        4: (rotate_yellow_counterclockwise, "B'"),
        5: (rotate_green_clockwise, "U"),
        6: (rotate_green_counterclockwise, "U'"),
        7: (rotate_blue_clockwise, "D"),
        8: (rotate_blue_counterclockwise, "D'"),
        9: (rotate_orange_clockwise, "R"),
        10: (rotate_orange_counterclockwise, "R'"),
        11: (rotate_red_clockwise, "L"),
        12: (rotate_red_counterclockwise, "L'")
    }

    for i in range(len(scramble_sequence)):

        move_function, move_notation = move_mapping[scramble_sequence[i]]
        move_function()#print(move_notation);visualize_cube()
        scramble_sequence[i] = move_notation

    print(*scramble_sequence)
    return scramble_sequence

def controls():
    user_move = input('move? ').upper()

    if user_move in move_set:

        move_set[user_move]()
    else:
        print('doesnt exist')


# Define move sets and options
sides = '|'
move_set = {
    "F": rotate_white_clockwise, "F'": rotate_white_counterclockwise,
    "B": rotate_yellow_clockwise, "B'": rotate_yellow_counterclockwise,
    "U": rotate_green_clockwise, "U'": rotate_green_counterclockwise,
    "D": rotate_blue_clockwise, "D'": rotate_blue_counterclockwise,
    "R": rotate_orange_clockwise, "R'": rotate_orange_counterclockwise,
    "L": rotate_red_clockwise, "L'": rotate_red_counterclockwise
}

# Main solving loop
cube_scrambled = False

while True:
    if not cube_scrambled:
        scramble_cube(20)
        cube_scrambled = True
    visualize_cube()

    solve_daisy(GREEN, ORANGE, WHITE, RED, YELLOW, BLUE)
    solve_white_cross(GREEN, ORANGE, WHITE, RED, YELLOW, BLUE)
    solve_white_face(GREEN, ORANGE, WHITE, RED, YELLOW, BLUE)
    solve_second_layer(GREEN, ORANGE, WHITE, RED, YELLOW, BLUE)
    #solve_yellow_face(GREEN, ORANGE, WHITE, RED, YELLOW, BLUE)
    visualize_cube()
    input("Press Enter to continue...")
    #controls()
