import random
import sys
import json

#Team 12
sys.stderr.write("Connect Four Group 12 - Python\n")

player = sys.argv[2] 
width = sys.argv[4]
height = sys.argv[6] 

sys.stderr.write("player = " + player)
sys.stderr.write('\n')
sys.stderr.write(" width = " + width)
sys.stderr.write('\n')
sys.stderr.write("height = " + height)
sys.stderr.write('\n')

#Check available moves on current grid
def valid_moves(grid):
    moves = []
    for i in range(int(width)):
        if grid[i][0] == 0:
            moves.append(i)
    return moves


def valid_smart(grid):
    action = {}
    for i in range(int(width)):
        for j in range(1,int(height)):
            if grid[i][j] == int(player) and grid[i][j-1] == 0:
                action['move'] = i
                return action

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
