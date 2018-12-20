import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import community


# Load in .txt and .xls files exported from Matlab (will explain them later)
pos_mat = np.genfromtxt('Node_Pos_t1.txt', delimiter=",")  # Holds node positions (among other info)
conn_df = pd.read_excel('conn_list.xls')  # Holds the 'connectivity' of each node
conn_list = np.genfromtxt('filename.txt')  # Essentially the indices of the adjacency matrix


### Step 1: Load in node_positions
# 'Networkx' allows me to specify node_positions if they
#  are store into a dictionary

pos_dict = {}  # Initialize position dictionary

for k in range(len(pos_mat[:, 0])): # Loop through the number of nodes
        pos_dict[k] = (pos_mat[k,0],pos_mat[k,1]) # assign position values to node keys

# Now when I create my network/graph, I can visualize it with...
    # nx.draw(Graph, pos = pos_dict)
    # plt.show()

#######################################################################################
# Now I tried to build the network/graph in a few different ways, the third is still
# not entirely correct... below are my three attempts with detailed explanation:
#######################################################################################

### Attempt 1: Simply build from 'adj_mat.txt'

A = np.genfromtxt('adj_mat.txt', delimiter=",", skip_header=1)  # Load in adj_mat
adj_mat = A > 0 # my adj_mat has values that correspond to edge length attribute.
                # These don't matter, we just want 1's
G1 = nx.from_numpy_matrix(adj_mat, create_using=None)  # Generate graph from adj_mat

#plt.figure(1)
#nx.draw(G1, pos=pos_dict)
#plt.show()

# ISSUE 1: No idea the output is weird... this should work

#######################################################################################

### Attempt 2: Load in "connectivity list" as .txt file from Matlab
# 'conn_list.txt' : specifies the nodes that node_i is connected to,
#                   where node_i is given by the row number
# Ex:
#       2, 3, 6,
#         ...
#       172 174 180

# Thus node 1 (or 0 in python...) is connected to nodes 2,3,6

G2 = nx.Graph()  # Initialize graph

for i in range(len(conn_df)):  # Loop through each node_i (each row of conn_df)
    row_i = conn_df.loc[i, :].values  # get values of connectivity

    # However some nodes have connectivity of degree 3, others 4
    # so the size of each row_i list is variable. If degree
    # is 3 then the 4th value is "NaN"

    for j in range(2):  # range(len(row_i)): # Attempt to loo through length of row_i
        G2.add_edge(i, row_i[j])

#plt.figure(2)
#nx.draw(G2, pos=pos_dict)
#plt.show()

# ISSUE: 'len' function still counts "NaN" meaning everything has len = 4,
#         even when only 3 value present... This is why i'm, only looping thru first two
#         arguments write now, some rows only have 2 args.

#         I could easily figure out a way to get around this but
#         realized there's an easier way to do this...

#######################################################################################

### Attempt 3: Load in the indices of 'adj_mat.txt' (not the whole sparse matrix)

# What I mean is..

# [ 2, 1, 1
#   3, 4, 1
#     ...
#   175, 171, 1]

# This means at place (2,1) the adj_mat has a value of 1, so that is an edge...
# Now I simply must loop through this list and grab the first two arguments of each row
# that ex. (2,1) will be my input to G.add_edge

G3 = nx.Graph()  # Initialize graph

for i in range(len(conn_list)):
    # print(conn_list[i, :])
    row_i = conn_list[i, :]
    G3.add_edge(row_i[0], row_i[1])

#plt.figure(3)
#nx.draw(G3, pos=pos_dict)
#plt.show()

#######################################################################################

# Save the plot
#   In the future I want to load in then save each time frame
#   to make a pretty little video of the network
plt.savefig('network_image.jpg') # just save to current directory

###
def edge_to_remove(G): # returns edge to remove, calculated by the edge with highest betweenness centrality value
    dict1 = nx.edge_betweenness_centrality(G) # returns dict of values
            # Key : edge and Value: betweenness centrality value of that edge
    list_of_tuples = dict1.items() # returns tuples of dictionary (key, value)
    sorted_edge_list = sorted(list_of_tuples)
    #list_of_tuples.sort(key=lambda x: x[1], reverse=True) # sort the list based on second value of tuple, descending order

    return sorted_edge_list[0][0]  # in 0th tuple, return 0th element (which is the edge)


def gn(g):
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

# Now call function
G_test = nx.karate_club_graph()
comm_list = community.girvan_newman(G3)
split1 = tuple(sorted(c) for c in next(comm_list))
comm1 = split1[0]
comm2 = split1[1]


plt.figure(4)

color_map = []
for node in comm1:
        color_map.append('blue')
for node in comm2:
        color_map.append('green')
nx.draw(G3, pos=pos_dict, node_color=color_map, with_labels=False)
plt.show()


