import math
import random
import time

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
def tsp_heuristic(graph_data):
    num_nodes = len(graph_data)
    best_cycle = []
    best_cost = float('inf')
    start_time = time.time()
    best_solution_time = start_time
    num_cycles_evaluated = 0
    
    # Run the algorithm for 15 minutes
    while time.time() - start_time < 900:
        current_cycle = random.sample(range(num_nodes), num_nodes)
        current_cost = sum(graph_data[current_cycle[i]][2] for i in range(num_nodes))
        num_cycles_evaluated += 1
        if current_cost < best_cost:
            best_cycle = current_cycle
            best_cost = current_cost
            best_solution_time = time.time()
    
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    
    return best_cycle, best_cost, elapsed_time, best_solution_time, start_time, num_cycles_evaluated

def main():
    # Read graph data
    graph_data = read_graph_data('/Users/pankti/Downloads/1000_randomDistance.txt')  # Change filename accordingly

    # Solve TSP using the heuristic approach
    best_cycle, best_cost, elapsed_time, best_solution_time, start_time, num_cycles_evaluated = tsp_heuristic(graph_data)

    # Print solution
    print("Best cycle:", ' '.join(map(str, best_cycle)))
    print("Best cost:", round(best_cost, 2))
    print("Elapsed time:", round(elapsed_time, 2), "seconds")
    print("Best solution time:", round(best_solution_time - start_time, 2), "seconds")
    print(f"Number of cycles evaluated: {num_cycles_evaluated:.0e}")
    print(f"Cost of the best cycle found: {best_cost:.2f}")

    # Save solution to a text file
    with open('solutionB_922845686.txt', 'w') as file:
        file.write(' '.join(map(str, best_cycle)))

if __name__ == "__main__":
    main()
