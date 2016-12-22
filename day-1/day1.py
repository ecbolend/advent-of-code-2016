#
# Advent of Code 2016 - Day X
# 
# Eric Bolender  
#

# imports
from enum import Enum

# constants
INPUT = "R1, R1, R3, R1, R1, L2, R5, L2, R5, R1, R4, L2, R3, L3, R4, L5, R4, R4, R1, L5, L4, R5, R3, L1, R4, R3, L2, L1, R3, L4, R3, L2, R5, R190, R3, R5, L5, L1, R54, L3, L4, L1, R4, R1, R3, L1, L1, R2, L2, R2, R5, L3, R4, R76, L3, R4, R191, R5, R5, L5, L4, L5, L3, R1, R3, R2, L2, L2, L4, L5, L4, R5, R4, R4, R2, R3, R4, L3, L2, R5, R3, L2, L1, R2, L3, R2, L1, L1, R1, L3, R5, L5, L1, L2, R5, R3, L3, R3, R5, R2, R5, R5, L5, L5, R2, L3, L5, L2, L1, R2, R2, L2, R2, L3, L2, R3, L5, R4, L4, L5, R3, L4, R1, R3, R2, R4, L2, L3, R2, L5, R5, R4, L2, R4, L1, L3, L1, L3, R1, R2, R1, L5, R5, R3, L3, L3, L2, R4, R2, L5, L1, L1, L5, L4, L1, L1, R1"

LEFT = "L"
RIGHT = "R"

# Defines Direction Enum
class Direction(Enum):
    north = 1, 3, 4
    south = 2, 4, 3
    east = 3, 2, 1
    west = 4, 1, 2

    def __new__(cls, value, myLeft, myRight):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.myLeft = myLeft
        obj.myRight = myRight
        return obj

# Define Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def taxicabDistance(self, point):
        if not(isinstance(point, Point)):
            return -1

        return abs(self.x - point.x) + abs(self.y - point.y)

# global

currDirection = Direction.north
origin = Point(0, 0)
other = Point(0, 0)

# main function
def main():
    parse()

# parse the input
def parse():
    list = INPUT.split(",")

    # loop over list elements
    for i in list:
        dir = i.strip()[0]
        mag = i.strip()[1:]
        
        # calculate
        calculate(dir, int(mag))

    print("distance: ", origin.taxicabDistance(other))

# calculate the individual directions
def calculate(dir, mag):
    global currDirection, other
    
    # first change direction
    if dir == LEFT:
        currDirection = Direction(currDirection.myLeft)
    elif dir == RIGHT:
        currDirection = Direction(currDirection.myRight)

    x = other.x
    y = other.y

    if currDirection == Direction.north:
        other.setLocation(x, y + mag)
    elif currDirection == Direction.south:
        other.setLocation(x, y - mag)
    elif currDirection == Direction.east:
        other.setLocation(x + mag, y)
    elif currDirection == Direction.west:
        other.setLocation(x - mag, y)

if __name__ == "__main__":
    main()
