# Finding shortest paths through MIT buildings

import unittest
from graph import Digraph, Node, WeightedEdge

# ------------------------------------------------
# Problem 2: Building up the Campus Map
# ------------------------------------------------

# ---------------------------------
# Problem 2a: Designing your graph
# ---------------------------------
# What do the graph's nodes represent in this problem?
#   Nodes represent buildings on MIT campus
#
# What do the graph's edges represent?
#   They represent the paths conecting the buildings
#
# Where are the distances represented?
#   Distances are represented in the weights associated
#   with each edge

# ---------------------------------
# Problem 2b: Implementing load_map
# ---------------------------------
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """
    # Print info on screen
    print("Loading map from file...")

    # Initialize Digraph
    my_digraph = Digraph()

    # Open file with map data
    with open(map_filename) as file:
        for line in file:
            # Split line into components
            src, dest, total_distance, outdoor_distance = line.split()

            # Create nodes
            src, dest = Node(src), Node(dest)

            # Add nodes to digraph
            try:
                my_digraph.add_node(src)
            # If node already in digraph, skip it
            except ValueError:
                pass

            try:
                my_digraph.add_node(dest)
            # If node already in digraph, skip it
            except ValueError:
                pass

            # Compute weighted edge and add it to digraph
            my_digraph.add_edge(WeightedEdge(src, dest, int(total_distance), int(outdoor_distance)))
    
    # Print digrpah (optional)
    # print(my_digraph)

    # Return digraph
    return my_digraph


# ---------------------------------
# Problem 2c: Testing load_map
# ---------------------------------
# digraph_test = load_map('mit_map.txt')
# print(digraph_test)


# ------------------------------------------------
# Problem 3: Finding the Shorest Path using Optimized Search Method
# ------------------------------------------------


# ---------------------------------
# Problem 3a: Objective function
# ---------------------------------
# What is the objective function for this problem?
#   minimize the total distance traveled
#   (i.e., find shortest path)
#
# What are the constraints?
#   Do not exceed maximum distance outdoors


# ---------------------------------
# Problem 3b: Implement get_best_path
# ---------------------------------
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist, best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    # Check whether 'start' and 'end' exist in the digraph
    if not(digraph.has_node(Node(start)) and digraph.has_node(Node(end))):
        raise ValueError("Non-existent node in the graph")
    
    # Unpack traversed path so far and update it to include start
    current_path, total_dist, outdoor_dist = path
    current_path = current_path + [start]

    # Default case (recursion): If start = end, destination reached
    if start == end:
        # If we are on a better path, update
        if total_dist <= best_dist:
            best_dist = total_dist
            best_path = current_path
            return (best_path, best_dist)

        # else, return None
        return None
    
    # Loop through each node in digraph
    for edge in digraph.get_edges_for_node(Node(start)):
        # If destination not in path, compute new path (avoid cycles)
        if str(edge.get_destination()) not in current_path:
            # Update distances with new edge info
            new_total_distance = total_dist + edge.get_total_distance()
            new_outdoor_distance = outdoor_dist + edge.get_outdoor_distance()
            outdoor_distance_left = max_dist_outdoors - new_outdoor_distance

            # Compute new path only if constraints are respected
            if (outdoor_distance_left >= 0 and new_total_distance <= best_dist):
                # Compute new path recursively
                new_path = get_best_path(digraph, str(edge.get_destination()), end,
                                         [current_path, new_total_distance, new_outdoor_distance],
                                          outdoor_distance_left, best_dist, best_path)

                # Check if new path is better than previous one
                if not(new_path == None):
                    best_path, best_dist = new_path

    # Return best path
    return (best_path, best_dist)


# ---------------------------------
# Problem 3c: Implement directed_dfs
# ---------------------------------
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    path = [[], 0, 0]

    # Find best (i.e., shortest) path between nodes
    best_path, best_dist = get_best_path(digraph, start, end, path, max_dist_outdoors, max_total_dist, None)

    # If no path between nodes, inform the user
    if not(best_path == None) and best_dist <= max_total_dist:
        return best_path
    else:
        raise ValueError(f"There is no path from {start} to {end}")


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================
class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


# Run 'main' function
if __name__ == "__main__":
    unittest.main()