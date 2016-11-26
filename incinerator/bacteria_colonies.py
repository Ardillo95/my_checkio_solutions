import itertools

"""
    Get all positions that match: abs(x) + abs(y) = size.
    
    This is the same as obtaining all neighbours separated a distance = size
    from a central point
"""
def get_positions(size):
    
    positions = set()
    to_permut = list(range(-size, size+1))
    
    # If even size, add +-size/2 to to_permut (can appear twice in one position)
    if size%2 == 0:
        to_permut.extend([int(- size/2), int(- size/2)])
    
    possible_positions = itertools.permutations(to_permut, 2)
    for p0, p1 in possible_positions:
        if abs(p0) + abs(p1) == size:
            positions.add((p0, p1))
    
    # for size = 1: positions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    return positions

def bacteria_colonies(grid):
    N, M = len(grid), len(grid[0])
    colonies = []
    
    for i in range(N-1):
        for j in range(1, M-1):
            studying = True         # Flag to know we are studying the colony
            size = 2                # default size
            
            # If we find a '1'
            if grid[i][j]:
                # If this '1' is not surrounded by more one, not a colony
                for position in get_positions(size-1):
                    if not grid[i + position[0]][j + position[1]]:
                        studying = False
                
                # Each loop will study a new ampliation
                while studying:
                    ones = True # Flag to check if we find an ampliation of '1's
                    zeros = False # same with zeros
                    
                    # For each new neighbour
                    for index, (x, y) in enumerate(get_positions(size)):
                        
                        # If we are out of indexes, neighbour counts as '0'
                        if i+x in [-1, N] or j+y in [-1, M]:
                            neighbour = 0
                        else:
                            neighbour = grid[i+x][j+y]
                        
                        # Check if not all neighbours are '0's or '1's
                        if zeros and neighbour: # Not all neighbours are '0's
                            zeros = False
                            break
                        elif not neighbour:     # Not all neighbours are '1's
                            ones = False
                            if index == 0:      # First '0' neighbour
                                zeros = True
                    
                    # Check if apliation of '0's or '1's
                    if zeros:                   # If ampliations of '0's
                        colonies.append(((i, j), size))
                        studying = False
                    elif ones:                  # If ampliations of '1's
                        size += 1
                    else:                       # Not a colony
                        studying = False
    
    max_size = 0
    result = (0, 0)                             # Default solution
    
    for colony in colonies:
        if colony[1] >= max_size:
            max_size = colony[1]
            result = colony[0]
    
    return result
