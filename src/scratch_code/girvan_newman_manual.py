# Summary

# This is my manual attempt at writing the girvan_newman algorithm myself.
# INPUT: Graph object, G
# OUTPUT: Tuple object, list of nodes in each community

# The issue is that the output comes out to be a
# "generator object" which I cannot for the life of me
# figure out how to work with or visualize...


def edge_to_remove(G): # returns edge to remove, calculated by the edge with highest betweenness centrality value
    """
        This function calculates the edge_betweenness_centrality value of each edge in a network and
        subsequently outputs the edge label with the highest value. This signifies the edge to remove from the network
        according to the Girvan-Newman algorithm (see 'references' folder)

        Parameters:
        arg1 (G): Graph object input

        Returns:
        sorted_edge_list:  list object, contains the list of edges sorted in descending order by their
                           'edge_betweenness_centrality' value

        Other functions used: nx.edge_betweenness_centrality(G)... built into networkx module

    """
    dict1 = nx.edge_betweenness_centrality(G)  # returns dict of values
            #  Key : edge and Value: betweenness centrality value of that edge
    list_of_tuples = dict1.items() # returns tuples of dictionary (key, value)
    sorted_edge_list = sorted(list_of_tuples)
    #list_of_tuples.sort(key=lambda x: x[1], reverse=True) # sort the list based on second value of tuple, descending order

    return sorted_edge_list[0][0]  # in 0th tuple, return 0th element (which is the edge)


def girvan_newman(g):
    """
        This function deconstructs a graph object into communities
        based on the girvan_newman algorithm (see 'references' folder)

        Parameters:
        arg1 (G): Graph object input

        Returns:
        c:  generator, holds lists of node labels in each community

        Other functions used: edge_to_remove(G)

    """

    c = nx.connected_component_subgraphs(g)  # return connective component of graph as subgraph (we only have 1 so returns 1)
    num_graphs = len(list(c)) # gives number of subgraphs (always starts at 1)
    print('Initial number of communities ', num_graphs)

    # now must remove edges based on betweenness centrality value of edges
    while num_graphs == 1:
        g.remove_edge(*edge_to_remove(g)) # ((a,b)) --> (a,b)
        c = nx.connected_component_subgraphs(g)
        num_graphs = len(list(c))
        print('The number of communities are ', num_graphs)

    return c

  """ 
  
  Example: 
    G_test = nx.karate_club_graph()
    comm_node_list = girvan_newman(G_test)
    
  """