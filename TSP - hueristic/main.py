import networkx as nx
import random
import matplotlib.pyplot as plt


# generating a random graph with networkx library with random weights ranging from 1 to 100
def generate_complete_graph(num_nodes, weight_range=(1,100)):

    # inbuilt function to generate graph with give no of nodes
    G = nx.complete_graph(num_nodes)

    #  assigning random weights
    for u,v in G.edges() :
        G.edges[u,v]['weight'] = random.randint(*weight_range)
    return G

# checking values:
# print(generate_complete_graph(5))
# print(generate_complete_graph(5).edges())

# visualize the next step(animation)
# tour = path taken till now
# current node and pos(where in graph
def plot_graph_step (G, tour, current_node, pos):

    # clearing the current figure
    plt.clf()

    # visualize the graph
    nx.draw(G, pos ,with_labels=True, node_color= 'lightblue', node_size = 500)

    path_edges = list((zip(tour,tour[1:])))
    # for ex tour = [1,2,3]
    # list(zip(tour,tour[1:])) = [(1,2),(1,3),(2,3)]

    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    # highlight curretn node
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color= 'green', node_size=500)

    # set labels
    edge_label = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_label)

    plt.pause(0.5)

def plot_graph(G, tour, pos):
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    path_edges = list((zip(tour, tour[1:])))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    nx.draw_networkx_nodes(G, pos, node_color='green', node_size=500)

    edge_label = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_label)

    plt.pause(0.5)
    plt.show()

# save cost value
def calculate_tour_cost(G,tour):
        return sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

# main implementation of TSP heuristic
def nearest_neighbour_tsp(G,start_node = None):

    # setting up random value as start node in not given
    if start_node == None:
        start_node = random.choice(list(G.nodes))

    # display graph
    pos = nx.spring_layout(G)
    plt.ion()
    plt.show()

    # all nodes at start are unvisited
    unvisited = set(G.nodes)
    # except start node
    unvisited.remove(start_node)

    # tour is empty ar the beginning
    # but we start from start node
    tour = [start_node]
    current_node = start_node

    # showing initial grapgh
    plot_graph_step(G, tour, current_node, pos)

    while unvisited:
        # finding next node with least weight
        next_node = min(unvisited, key=lambda node: G[current_node][node]['weight'])
        # thus removing it from unvisited set
        unvisited.remove(next_node)
        # then adding it to the tour
        tour.append(next_node)
        current_node = next_node

        plot_graph_step(G, tour, current_node, pos)

    # come back to start node thus adding it to tour
    tour.append(start_node)
    plot_graph_step(G, tour, current_node, pos)

    print("tour:", tour)
    tour_cost = calculate_tour_cost(G,tour)
    print("tour cost:", tour_cost)

    plt.ioff()
    plt.close()

    return tour, tour_cost

if __name__ == '__main__':

    n = int(input("enter no of nodes:"))
    G = generate_complete_graph(n)

    tour_total = []

    for i in range (0,n):
        path, cost = nearest_neighbour_tsp(G, start_node=i)
        tour_total.append({'path':path, 'cost':cost})

    
    min = 999999
    index = -1

    for i in range(0, len(tour_total)):
        if tour_total[i]['cost'] < min:
            min = tour_total[i]['cost']
            index = i

    print("min cost:", min)
    print(tour_total[index]['path'])
    pos = nx.spring_layout(G)
    plot_graph(G, tour_total[index]['path'], pos)
