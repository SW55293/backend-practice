'''
PSEUDOCODE: TSP(CITIES, PATHS, DIST)
INPUTS
cities: A list of city identifiers (integers 0-n)
paths: A matrix where each point represents the distance between the two cities. For example, paths[cityA][cityB] holds the distance from cityA to cityB. paths[cityA][cityB] = paths[cityB][cityA]
dist: The distance we are trying to find a path shorter than
OUTPUT
True if there is a path shorter than dist. False otherwise.

ALGORITHM
Get the matrix of possible paths using the permutations function. This matrix holds all possible paths through the given cities. For example, permutations([1,2,3]) would result in:
[
    [1, 2, 3],
    [2, 1, 3],
    [3, 2, 1],
    [2, 3, 1],
    [3, 1, 2],
    [1, 3, 2]
]
Copy icon
Where the first path, [2, 1, 3] represents moving from city 2 -> city 1 -> city 3

Loop over each path
Loop over each city in the path keeping a sum of all the distances between each city.
If the total distance in the path is less than the given dist return true
If no short paths were found, return false

'''


import random

def tsp(cities, paths, dist):
    all_perms = permutations(cities)

    # Loop over each path.
    for perms in all_perms:
        # Calculate the total distance of the path.
        total_distance = 0
        for i in range(len(perms) - 1):
            total_distance += paths[perms[i]][perms[i + 1]]

        # If the minimum distance is less than the given distance, return True.
        if total_distance < dist:
            return True

    # If no short paths were found, return False.
    return False

            


# don't touch below this line


def test(num_cities, dist):
    paths = []
    cities = []
    for i in range(num_cities):
        path = []
        for j in range(num_cities):
            if i == j:
                path.append(0)
            elif j < i:
                path.append(paths[j][i])
            else:
                path.append(random.randint(0, 999))
        paths.append(path)
        cities.append(i)
    path_exists = tsp(cities, paths, dist)
    print("Paths:")
    print_matrix(paths)
    print("------------------------------------")
    print(f"Path shorter than {dist} miles exists: {path_exists}")
    print("====================================")


def main():
    random.seed(0)
    for num_cities in range(2, 10):
        dist = random.randint(0, 3999)
        test(num_cities, dist)


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res


def print_matrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        print(mat[i])


main()

