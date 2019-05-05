import random
import sys
import json

#Team 12
sys.stderr.write("Connect Four Group 12 - Python\n")

player = sys.argv[2] 
width = sys.argv[4]
height = sys.argv[6] 

#Function to check other player
def get_otherplayer(player):
    if int(player) == 1:
        return 2
    else:
        return 1

sys.stderr.write("player = " + player)
sys.stderr.write('\n')
sys.stderr.write(" width = " + width)
sys.stderr.write('\n')
sys.stderr.write("height = " + height)
sys.stderr.write('\n')

moveset = {}
oppon = get_otherplayer(player)

#Check available moves on current grid
def valid_moves(grid):
    moves = []
    for i in range(int(width)):
        if grid[i][0] == 0:
            moves.append(i)
    return moves

#Go to the space where the piece will be dropped

def toemptyspace(grid, i, j):
    if grid[i][j] == 0:
        return j
    else:
        return toemptyspace(grid, i, j+1)
    
#Check for a valid vertical move
def vertical(grid, i, j):
    if j > 0 and grid[i][j-1] == 0:
        moveset['moved'] = True
        moveset['move'] = i
    else:
        moveset['moved'] = False
    return moveset

#Check for a valid horizontal move
def horizontal(grid, i, j):
    if i < int(width) and grid[i+1][j] == int(player) and grid[i+1][j+1] == 0:
        moveset['moved'] = True
        moveset['move'] = i   
    elif i > 0 and grid[i-1][j] == int(player) and grid[i+1][j+1] == 0:
        moveset['moved'] = True
        moveset['move'] = i
    else:
        moveset['moved'] = False
    return moveset


def diagonal(grid, i, j):
    if i < int(width):
        if j > 0 and grid[i+1][j-1] == int(player):
            moveset['moved'] = True
            moveset['move'] = i


def valid_smart(grid):
    action = {}
    val_moves = valid_moves(grid)
    for i in val_moves:
        j = toemptyspace(grid, i, j)
        v_move = vertical(grid, i, j)
        h_move = horizontal(grid, i, j)
        
    action['move'] = random.choice(valid_moves(grid))
    return action
# Read state from driver, place moves.
for line in sys.stdin:
    sys.stderr.write(line)
    state = json.loads(line)
    grid = state['grid']
    action = valid_smart(grid)
    msg = json.dumps(action)
    sys.stderr.write(msg + '\n')
    sys.stdout.write(msg + '\n')
    sys.stdout.flush()

sys.stdin.close()
sys.stdout.close()
sys.stderr.close()
