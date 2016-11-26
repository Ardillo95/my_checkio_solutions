def open_labyrithm(maze_map):
    
    queue = [((1, 1), '')]
    visited = set((1, 1))
    
    while True:
        
        for position, path in queue:
                
            if position == (10, 10):        # destination reched
                return path
            
            N, E = (position[0] - 1, position[1]), (position[0], position[1] + 1)
            S, W = (position[0] + 1, position[1]), (position[0], position[1] - 1)
            
            # Checking if no walls in all posibles moves (N, E, S, W) and if
            # this new position is not visited yet
            if not maze_map[N[0]][N[1]] and N not in visited:
                queue.append((N, path + 'N'))
                visited.add(N)
            if not maze_map[E[0]][E[1]] and E not in visited:
                queue.append((E, path + 'E'))
                visited.add(E)
            if not maze_map[S[0]][S[1]] and S not in visited:
                queue.append((S, path + 'S'))
                visited.add(S)
            if not maze_map[W[0]][W[1]] and W not in visited:
                queue.append((W, path + 'W'))
                visited.add(W)
            
            # Wrong path, steping back to another option
            queue.remove((position, path))
