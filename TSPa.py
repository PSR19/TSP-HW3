import math
import random
import time

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to read graph data from a text file
def read_graph_data(filename):
    with open(filename, 'r') as file:
        # Skip the first two lines
        next(file)
        next(file)
        graph_data = []
        for line in file:
            node1, node2, distance = line.strip().split()
            graph_data.append((int(node1), int(node2), float(distance)))
        return graph_data

# TSP algorithm using a heuristic approach
def tsp_heuristic(graph_data, start_time):
    num_nodes = len(graph_data)
    best_cycle = []
    best_cost = float('inf')
    best_solution_time = start_time
    visited_cycles = 0
    
    # Run the algorithm for 15 minutes
    while time.time() - start_time < 900:
        current_cycle = random.sample(range(num_nodes), num_nodes)
        current_cost = sum(euclidean_distance(graph_data[current_cycle[i]], graph_data[current_cycle[(i + 1) % num_nodes]]) for i in range(num_nodes))
        visited_cycles += 1
        if current_cost < best_cost:
            best_cycle = current_cycle
            best_cost = current_cost
            best_solution_time = time.time()
    
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    
    return best_cycle, best_cost, elapsed_time, best_solution_time, visited_cycles

def main():
    start_time = time.time()  # Start time for measuring elapsed time
    # Read graph data
    graph_data = read_graph_data('/Users/pankti/Downloads/1000_euclidianDistance.txt')  # Change filename accordingly

    # Solve TSP using the heuristic approach
    best_cycle, best_cost, elapsed_time, best_solution_time, visited_cycles = tsp_heuristic(graph_data, start_time)

    # Print solution
    print("Best cycle:", ' '.join(map(str, best_cycle)))
    print("Best cost:", round(best_cost, 2))
    print("Elapsed time:", round(elapsed_time, 2), "seconds")
    print("Best solution time:", round(best_solution_time - start_time, 2), "seconds")
    print("Visited cycles:", "{:.1e}".format(visited_cycles))  # Format visited cycles in scientific notation
    print("Cost of the best cycle found:", round(best_cost, 2))  # Display cost of the best cycle found

    # Save solution to a text file
    with open('solutionA_922845686.txt', 'w') as file:
        file.write(' '.join(map(str, best_cycle)))

if __name__ == "__main__":
    main()
