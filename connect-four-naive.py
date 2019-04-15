import random
import sys
import json

sys.stderr.write("Connect Four Group 12 - Python\n")

player = int(sys.argv[2]) 
width = int(sys.argv[4])
height = int(sys.argv[6]) 

sys.stderr.write("player = " + str(player) + '\n')
sys.stderr.write(" width = " + str(width) + '\n')
sys.stderr.write("height = " + str(height) + '\n')

def valid_moves(state):
    """Returns the valid moves for the state as a list of integers."""
    grid = state['grid']
    moves = []
    for i in range(width):
        if grid[i][0] == 0:
            moves.append(i)
    return moves

# Code block for adding AI behaviour (for now this is just naive)
def player_actions(state):
    action = {}
    action['move'] = random.choice(valid_moves(state))
    return action

# Loop reading the state from the driver and writing a random valid move.
for line in sys.stdin:
    sys.stderr.write(line)
    state = json.loads(line)
    action = player_actions(state)
    msg = json.dumps(action)
    sys.stderr.write(msg + '\n')
    sys.stdout.write(msg + '\n')
    sys.stdout.flush()

sys.stdin.close()
sys.stdout.close()
sys.stderr.close()
