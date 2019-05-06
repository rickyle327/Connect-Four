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

#Defense code block
def defensive_v(grid, i, j):
    for n in range(1,4):
        #Vertical defense
        if j+n == int(height):
            return 0
        elif int(grid[i][j+n]) != oppon:
            return 0
        else:
            continue
    return int(height)*int(width)

def defensive_hleft(grid, i, j):
    for n in range(1,4):
        if i-n < 0:
            return 0
        elif int(grid[i-n][j]) != oppon:
            return 0
        else: 
            continue
    return int(height)*int(width)

def defensive_hright(grid, i, j):
    for n in range(1,4):
        if i+n == int(width):
            return 0
        elif int(grid[i+n][j]) != oppon:
            return 0
        else: 
            continue
    return int(height)*int(width)

def defensive_hmid(grid, i, j):
    for n in range(1,2):
        if i+n == int(width):
            return 0
        elif i-n < 0:
            return 0
        elif int(grid[i+n][j]) != oppon:
            return 0
        elif int(grid[i-n][j]) != oppon:
            return 0
        else: 
            continue
        
    return int(height)*int(width)
    
def defensive_diagdr(grid, i, j):
    for n in range(1,4):
        if j+n == int(height):
            return 0
        elif i+n == int(width):
            return 0
        elif int(grid[i+n][j+n]) != oppon:
            return 0
        else:
            continue

    return int(height)*int(width)

def defensive_diagdl(grid, i, j):
    for n in range(1,4):
        if j+n == int(height):
            return 0
        elif i-n < 0:
            return 0
        elif int(grid[i-n][j+n]) != oppon:
            return 0

    return int(height)*int(width)

def defensive_diagul(grid, i, j):
    for n in range(1,4):
        if j-n < 0:
            return 0
        elif i-n < 0:
            return 0
        elif int(grid[i-n][j-n]) != oppon:
            return 0

    return int(height)*int(width)

def defensive_diagur(grid, i, j):
    for n in range(1,4):
        if j-n == int(height):
            return 0
        elif i+n == int(width):
            return 0
        elif int(grid[i+n][j-n]) != oppon:
            return 0
        else:
            continue

        return int(height)*int(width)

#Priority check for vertical moves
def defensive(grid, i, j):
    movedef = {}
    movedef['move'] = i

    v_def = defensive_v(grid, i, j)
    hleft_def = defensive_hleft(grid, i, j)
    hright_def = defensive_hright(grid, i, j)
    hmid_def = defensive_hmid(grid, i, j)
    dr_def = defensive_diagdr(grid, i, j)
    dl_def = defensive_diagdl(grid, i, j)
    ur_def = defensive_diagur(grid, i, j)
    ul_def = defensive_diagul(grid, i, j)
    if v_def > 0:
        movedef['priority'] = v_def
    elif hleft_def > 0:
        movedef['priority'] = hleft_def
    elif hright_def > 0:
        movedef['priority'] = hright_def
    elif hmid_def > 0:
        movedef['priority'] = hmid_def
    elif dr_def > 0:
        movedef['priority'] = dr_def
    elif dl_def > 0:
        movedef['priority'] = dl_def
    elif ur_def > 0:
        movedef['priority'] = ur_def
    elif ul_def > 0:
        movedef['priority'] = ul_def
    else:
        movedef['priority'] = 0
    
    return movedef


#Priority check for vertical moves
def vertical_priority(grid, i, j):
    for n in range(1,5):
        if j+n == int(height):
            return n-1
        elif int(grid[i][j+n]) != int(player):
            return n-1
        else:
            continue
    return 0

#Generate a vertical moveset
def vertical(grid, i, j):
    v_move = {}
    v_move['move'] = i
    v_move['priority'] = vertical_priority(grid, i, j)
    return v_move

def h_priority_right(grid, i, j):
    for n in range(1,5):
        if i+n == int(width):
            return n-1
        elif int(grid[i+n][j]) != int(player):
            return n-1
        else: 
            continue
    return 0

def h_priority_left(grid, i, j):
    for n in range(1,5):
        if i-n < 0:
            return n-1
        elif int(grid[i-n][j]) != int(player):
            return n-1
        else: 
            continue
    return 0

#Check for a valid horizontal move
def horizontal(grid, i, j):
    h_move = {}
    h_move['move'] = i
    h_left = h_priority_left(grid, i, j)
    h_right = h_priority_right(grid, i, j)
    if h_left > h_right:
        h_move['priority'] = h_left
    elif h_left < h_right:
        h_move['priority'] = h_right
    else:
        h_move['priority'] = (h_left + h_right)*2
    return h_move

#Master moveset function
def valid_smart(grid):
    action = {}
    val_moves = valid_moves(grid)

    final_move = {}
    final_move['priority'] = 0

    for i in val_moves:
        j = 0
        j = toemptyspace(grid, i, j)
        def_move = defensive(grid, i, j)
        v_move = vertical(grid, i, j)
        h_move = horizontal(grid, i, j)

        if def_move['priority'] > final_move['priority']:
            final_move['priority'] = def_move['priority']
            final_move['move'] = def_move['move']
            break
        elif v_move['priority'] > final_move['priority']:
            final_move['priority'] = v_move['priority']
            final_move['move'] = v_move['move']
            continue
        elif h_move['priority'] > final_move['priority']:
            final_move['priority'] = h_move['priority']
            final_move['move'] = h_move['move']
            continue
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
