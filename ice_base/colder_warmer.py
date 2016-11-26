directions = []
POSITIVE_MOVE, NEGATIVE_MOVE = 1, -1
swap = False

def colder_warmer(steps):
    
    global swap
    
    # If first move, we study analysis directions (direction to largest distance)
    if len(steps) == 1:
        
        if steps[0][1] < 5:     directions.append(POSITIVE_MOVE)    #East
        else:                   directions.append(NEGATIVE_MOVE)    #West
        
        if steps[0][0] < 5:     directions.append(POSITIVE_MOVE)    #North
        else:                   directions.append(NEGATIVE_MOVE)    #South
        
        return [steps[0][0] + 2 * directions[1], steps[0][1]]
            
    act_dx,   act_dy,   act_result  =   steps[-1][0], steps[-1][1], steps[-1][2]
    last_dx,  last_dy,  last_result =   steps[-2][0], steps[-2][1], steps[-2][2]
    
    # Finding the correct row
    if not swap:
        
        if act_result == 1:
            if act_dx in [1, 8]:    return [act_dx+1 * directions[1], act_dy]
            if last_dx in [1, 8]:
                swap = True
                return [act_dx, act_dy+2 * directions[0]]
            return [act_dx+2 * directions[1], act_dy]
            
        elif act_result == 0:
            swap = True
            if last_result == -1:
                return [steps[-3][0], act_dy+2 * directions[0]]
            return [act_dx-1 * directions[1], act_dy+2 * directions[0]]
        
        else:
            directions[1] *= -1
            if act_dx in [1, 8]:    return [act_dx+2 * directions[1], last_dy]
            return [act_dx+4 * directions[1], last_dy]
            
    # Finding the correct column
    if act_result == 1:
        if act_dy in [1, 8]:    return [act_dx, act_dy+1 * directions[0]]
        return [act_dx, act_dy+2 * directions[0]]
    
    elif last_result == 0:
        return [act_dx, act_dy-1 * directions[0]]
    
    else:
        directions[0] *= -1
        if act_dy in [1, 8]:    return [act_dx, act_dy+2 * directions[0]]
        return [act_dx, act_dy+4 * directions[0]]
