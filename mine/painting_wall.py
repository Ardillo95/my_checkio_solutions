"""
Given the operations of the actual step, this function return the operations and
the coverage of the next step.

Parameters:
  - actual:         list operations of the actual step
  - operations:     list of the remaining operations
  
Return:
  - actual:         list of operations of the next step
  - coverage:       coverage of the next step.
"""
def get_coverage(actual, operations):
    
    # Getting the next operation to add and his boundaries
    operation = operations[0]
    a, b = operation[0], operation[1]
    
    # pop operations from area in order to replace with new ones (if join)
    to_pop = []
    
    # For each area in actual:
    for index, area in enumerate(actual):
        c, d = area[0], area[1]                     # Borders of the area
        # If we can join area with operation, create the new area [a, b] 
        # and add index to pop 
        if c <= a <= d or c <= b <= d:
            a = min(a, c)
            b = max(b, d)
            to_pop.append(index)
        # If area inside operation, pop area
        if a <= c and b >= d:
            to_pop.append(index)
    
    # pop areas and replace them with new joined areas
    actual = [x for i, x in enumerate(actual) if  i not in to_pop]
    actual.append([a, b])
    
    # If first step, remove default value
    if [0, 0] in actual:
        actual.remove([0, 0])
            
    # coverage = sum of area[b] - area[a] for all areas in actual
    coverage = sum([area[1] for area in actual]) - \
               sum([area[0] for area in actual]) + 1 * len(actual)
    
    return actual, coverage

"""
Calculate the minimum number of operations.

Parameters:
  - required: area to paint
  - operations: list of operations avariable
  
Return:
  - Minimun number of operations.
  - '-1' if not possible
"""
def painting_wall(required, operations):
    
    n_operations = len(operations)          # number of steps
    data = []                               # list of coverage for each step
    actual_coverage = [[0, 0]]              # default value: [0, 0]
    
    for __ in range(n_operations):
        # get next step and coverage
        actual_coverage, coverage = get_coverage(actual_coverage, operations)
        data.append(coverage)
        operations.pop(0)
    
    # if required is lower than one of the coverages, return the step number
    for index, coverage in enumerate(data):
        if required <= coverage:
            return index + 1
    
    return -1
