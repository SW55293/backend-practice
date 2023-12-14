'''
INSTRUCTIONS FOR WRITING THE FUNCTION
1. Create an empty list to store the file paths.
2. For each "node" in the current dictionary:
3. If the node maps to None, add the full path for that node to the list.
Otherwise, extend the file list with the results of calling list_files on the node. Be sure to update the current path to include the current node.
4. Return the list of file paths.

'''
def list_files(current_node, current_path=""):
    # Create an empty list to store the file paths.
    new_paths = []

    for node in current_node:
        # get the current node, single node
        node_values = current_node[node]
        
        # If the node maps to None, add the full path for that node to the list.
        if node_values is None:
            new_paths.append(current_path + "/" + node)
        else:
            # Otherwise, extend the file list with the results of calling list_files
            # on the node. Be sure to update the current path to include the current node.
            new_paths.extend(list_files(node_values, current_path + "/" + node))

    return new_paths
    
