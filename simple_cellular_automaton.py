'''
input_rule = integer from 0 to 255 (converted into a rule using bit interpretation)
num_timesteps = # of time-steps/iterations of rule application (i.e. output height)
num_cells = # of cells (i.e. output width)
'''

# Import Modules
import sys

# Define Variables
input_rule = sys.argv[1] # integer from 0 to 255
num_cells = sys.argv[2] # number of time steps
num_timesteps = sys.argv[3] # number of cells


def get_rule(input_rule):
    ''' Creates a dictionary which converts integers into their bit representations.
    The dictionary can be used to determine the state of a cell.

    Input
    -----
    input_rule : int
      An integer in the range from 0-255.

    Returns
    -------
    dict
      Each key is a possible state combination of a cell and its neighbors.
      Each value is the output of the cell; ON = 1 and OFF = 0,
      determined by mapping the states onto the corresponding bit.
    '''
    # Interpret Rule: 0 -> OFF; 1 -> ON
    rule = '{0:08b}'.format(int(input_rule)) # format integer as bit string
    # Create Dictionary (for rule interpretation)
    key_list = ['111','110','101','100','011','010','001','000'] # all 8 possible key combinations
    rule_dict = {}
    rule_val = 0
    for key in key_list:
        rule_dict[key] = rule[rule_val]
        rule_val += 1
    return rule_dict

def grow_cellular_automaton(input_rule, num_cells, num_timesteps):
    '''Grows the cellular automaton.
    
    Input
    -----
    rule : int
      An integer in the range from 0-255.
    num_cells : int
      The number of cells (columns) of the cellular automaton.
    num_timesteps : int
      The number of time steps (rows) that the cellular automaton grows.

    Output
    ------
    text file
      The output is a text file that shows how the initial state evolves when following the rule.
    '''
    # Get Dictionary
    rule_dict = get_rule(input_rule)

    # Title pbm file
    print 'P1 ' + num_cells + ' ' + num_timesteps
    
    # Create baseline state with single 'on' cell in center
    if int(num_cells)%2 == 1:
        cell_state = '0'*(int(num_cells)/2) + '1' + '0'*(int(num_cells)/2)
    else:
        cell_state = '0'*(int(num_cells)/2) + '1' + '0'*((int(num_cells)/2)-1)
    print cell_state

    new_state = []
    fname = 'cell_automaton_rule-%s_cells-%s_timesteps-%s.txt' % (input_rule, num_cells, num_timesteps)
    dfile = open(fname,'w')

    for time in range(int(num_timesteps)): # Determine cell states in each column/timestep
        for cell in range(len(cell_state)): # Determine each cell state in row
            if cell == 0: # Left edge case, where off grid => off
                key = '0' + cell_state[cell:cell+2]
            elif cell == len(cell_state)-1: # Right edge case, where off grid => off
                key = cell_state[cell-1:cell+1] + '0'
            else:
                key = cell_state[cell-1:cell+2]
            new_state.append(rule_dict[key])
        cell_state = ''.join(new_state)
        new_state = []
        for char in cell_state:
            dfile.write(char+' ')
        dfile.write('\n')
        print cell_state

# Run Function
grow_cellular_automaton(input_rule, num_cells, num_timesteps)
