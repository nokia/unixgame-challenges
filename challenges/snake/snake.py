# Copyright 2019-2022 Nokia
#
# Licensed under the Creative Commons Attribution 2.0 Generic license
# SPDX-License-Identifier: CC-BY-2.0
 
 
# # usage: python snake.py < solution.txt
# prints the full steps, ending with True if the sequence of steps ends on the goal
# or False otherwise
import fileinput

SIZE = 4 # 4x4 grid

grid = [ [ '.' for i in range(SIZE) ] for j in range(SIZE) ]

# grid[y][x]
grid[0][1] = 'X'
grid[3][3] = 'X' # X, a wall
grid[0][3] = 'F' # Flag, the goal

goal_pos = (3,0)
pos = (1,3)

#                0  1  2  3
# orientation = [E, S, W, N]
orientation = 0

MOVES = [
    lambda x,y: (min(x+1,SIZE), y),             #E
    lambda x,y: (x,             min(y+1,SIZE)), #S
    lambda x,y: (max(0,x-1),    y),             #W
    lambda x,y: (x,             max(0,y-1))     #N
]

def print_grid(grid, oldpos, newpos):
    grid[oldpos[1]][oldpos[0]] = 'F' if oldpos == goal_pos else '.'
    grid[newpos[1]][newpos[0]] = ['>', 'v', '<', '^'][orientation]
    print('\n'.join([ ''.join(row) for row in grid ]))

print_grid(grid, pos, pos)
for line in fileinput.input():
    oldpos = pos
    if line == "move forward\n":
        (newx, newy) = MOVES[orientation](pos[0], pos[1])
        if grid[newy][newx] != 'X':
            pos = (newx, newy)
    elif line == "turn left\n":
        orientation = 3 if orientation == 0 else orientation-1
    elif line == "turn right\n":
        orientation = (orientation+1) % 4
    else:
        raise ValueError(f"invalid line: '{line}'")
    print('')
    print(line)
    print_grid(grid, oldpos, pos)
print(pos == goal_pos)