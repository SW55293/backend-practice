'''
ALGORITHM
Loop over each city in the actual path
Sum the distance between each city in the actual path
If the sum is less than dist, return True, otherwise return False
'''

def verify_tsp(paths, dist, actual_path):
    total_dist = 0
    for x in range(len(actual_path)-1):
        total_dist = paths[actual_path[x]][actual_path[x+1]]
        
    total_dist += paths[actual_path[-1]][actual_path[0]]

    return total_dist < dist