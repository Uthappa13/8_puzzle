from queue import Queue

# Function to find the soluton to the 8 game puzzle
def PuzzleSolution(initial_state):
    visited = set()
    queue = Queue()
    queue.put((initial_state, [initial_state], 1, 1))  # (state, path)

    nodes_info = []
    node_index = 2
    parent_index = 1

    goal_state = (1, 4, 7, 2, 5, 8, 3, 6, 0)

    while not queue.empty():
        # Get the current node from the queue
        current_state, path, node_i, parent_i = queue.get()

        if current_state in visited:
            continue

        visited.add(current_state)

        nodes_info.append((node_i, parent_i, current_state))
        parent_i = node_i

        # compare the current node with the goal node
        if current_state == goal_state:
            visited.add(goal_state)
            return path, visited, nodes_info

        # find the location of the blank tile
        blank_tile = current_state.index(0)
        blank_tile_2d = (blank_tile % 3, blank_tile // 3)
        next_states = []

        # define the action to move the blank tile left
        def MoveTileLeft(current_state):
            new_node = list(current_state)
            if blank_tile_2d[1] > 0:
                new_node[blank_tile], new_node[blank_tile-3] = new_node[blank_tile-3], new_node[blank_tile]
                return tuple(new_node)
            else:
                return None

        # define the action to move the blank tile right
        def MoveTileRight(current_state):
            new_node = list(current_state)
            if blank_tile_2d[1] < 2:
                new_node[blank_tile], new_node[blank_tile+3] = new_node[blank_tile+3], new_node[blank_tile]
                return tuple(new_node)
            else:
                return None

        # define the action to move the blank tile up
        def MoveTileUp(current_state):
            new_node = list(current_state)
            if blank_tile_2d[0] > 0:
                new_node[blank_tile], new_node[blank_tile-1] = new_node[blank_tile-1], new_node[blank_tile]
                return tuple(new_node)
            else:
                return None

        # define the action to move the blank tile down
        def MoveTileDown(current_state):
            new_node = list(current_state)
            if blank_tile_2d[0] < 2:
                new_node[blank_tile], new_node[blank_tile+1] = new_node[blank_tile+1], new_node[blank_tile]
                return tuple(new_node)
            else:
                return None
            
        # find the child nodes for the current node
        left_move = MoveTileLeft(current_state)
        if left_move != None:
            next_states.append(left_move)

        right_move = MoveTileRight(current_state)
        if right_move != None:
            next_states.append(right_move)

        up_move = MoveTileUp(current_state)
        if up_move != None:
            next_states.append(up_move)

        down_move = MoveTileDown(current_state)
        if down_move != None:
            next_states.append(down_move)

        for next_state in next_states:
            if next_state not in visited:
                queue.put((next_state, path + [next_state], node_index, parent_index))
                node_index += 1
        
        parent_index += 1

    return None, None, None

# function to accept the initial state for the 8 game puzzle
def InputInitialState():
    while True:
        user_input = input("Enter the initial state (0-8) in a column-wise fashion, "
                           "separated by spaces  \n")
        try:
            initial_state = tuple(map(int, user_input.strip().split()))
            
            if len(initial_state) != 9 or not set(initial_state) == set(range(9)):
                raise ValueError("Invalid input. Ensure you've entered exactly 9 digits (0-8), each exactly once.")
            
            return initial_state
        except ValueError as e:
            print(e)
            continue

# function call
initial_state = InputInitialState()
path, visited, nodes_info = PuzzleSolution(initial_state)

# write to the text files once the path has been found
if path:
    print("Solution found for the 8 puzzle game")
    file1 = open('nodePath.txt', 'w')
    for step in path:
        output = ' '.join(map(str, step))
        file1.write(output + '\n')
    
    file2 = open('Nodes.txt', 'w')
    for node in visited:
        output = ' '.join(map(str, node))
        file2.write(output + '\n')

    file3 =  open('NodesInfo.txt', 'w')
    file3.write('Node_Index' + '\t' + 'Parent_Node_Index' + '\t' + 'Node' + '\n')
    for index, parent_index, node in nodes_info:
        output = ' '.join(map(str, node))
        file3.write(f"{index}\t\t\t{parent_index}\t\t\t\t\t{output}\n")
else:
    print("No solution exists for the 8 puzzle game")