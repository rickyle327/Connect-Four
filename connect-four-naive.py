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
    if j == int(height) - 1:
        return j
    elif grid[i][j] == 0 and grid[i][j+1] !=0:
        return j
    else:
        return toemptyspace(grid, i, j+1)

#Priority check for vertical moves
def vertical_priority(grid, i, j):
    for n in range(1,5):
        if j+n == int(height):
            return n-1
        if int(grid[i][j+n]) != int(player):
            return n-1
        else:
            continue
    return 0

#Generate a vertical moveset
def vertical(grid, i, j):
    moveset['move'] = i
    moveset['priority'] = vertical_priority(grid, i, j)
    return moveset

#def h_priority_left(grid, i, j, n = 1):
#    if i + n < 0:
#        return n-1
#    elif grid[i-n][j]:


#def horizontal_priority(grid, i, j):
#    final_h = 0

#Check for a valid horizontal move
def horizontal(grid, i, j):
    if i+1 < int(width) and grid[i+1][j] == int(player):
        moveset['priority'] = 1
        moveset['move'] = i   
    elif i > 0 and grid[i-1][j] == int(player):
        moveset['priority'] = 1
        moveset['move'] = i
    else:
        moveset['priority'] = 0
    return moveset

#Left-side diagonal moveset
#def l_diag(grid, i, j):
#    if grid[i+1][j-1] == int(player):
#        moveset['moved'] = True
#        moveset['move'] = i 
#    elif grid[i+1][j+1] == int(player):
#        moveset['moved'] = True
#        moveset['move'] = i
#    else:
#        moveset['moved'] = False
#    return moveset

#Right-side diagonal moveset
#def r_diag(grid, i, j):
#    if grid[i-1][j-1] == int(player):
#        moveset['moved'] = True
#        moveset['move'] = i 
#    elif grid[i-1][j+1] == int(player):
#        moveset['moved'] = True
#        moveset['move'] = i
#    else:
#        moveset['moved'] = False
#    return moveset

#Master diagonal moveset
#def diagonal(grid, i, j):
#    if i+1 < int(width):
#        moveset = l_diag(grid, i, j)
#    elif i > 0:
#        moveset = r_diag(grid, i, j)
#    return moveset

#Master moveset function
def valid_smart(grid):
    action = {}
    val_moves = valid_moves(grid)

    final_move = {}
    final_move['priority'] = 0

    for i in val_moves:
        j = 0
        j = toemptyspace(grid, i, j)
        v_move = vertical(grid, i, j)
        h_move = horizontal(grid, i, j)
#        d_move = diagonal(grid, i, j)

        if v_move['priority'] > final_move['priority']:
            final_move['priority'] = v_move['priority']
            final_move['move'] = v_move['move']
            continue
        elif h_move['priority'] > final_move['priority']:
            final_move['priority'] = h_move['priority']
            final_move['move'] = h_move['move']
            continue
#        elif d_move['moved'] == True:
#            action['move'] = d_move['move']
#            return action
        else:
            continue

    if final_move['priority'] == 0:
        action['move'] = random.choice(valid_moves(grid))
    else:
        action['move'] = final_move['move']
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
