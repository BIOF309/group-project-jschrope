# Import necessary packages
#   Don't know why these all red underline... cant be good

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import community

# Load in .txt and .xls files exported from Matlab (will explain them later)
pos_mat = np.genfromtxt('Node_Pos_t1.txt', delimiter=",")  # Holds node positions (among other info)
conn_df = pd.read_excel('conn_list.xls')  # Holds the 'connectivity' of each node
conn_list = np.genfromtxt('adj_mat_index_list.txt')  # Essentially the indices of the adjacency matrix

# Step 1: Load in node_positions
#   'Networkx' allows me to specify node_positions in nd.draw()
#    if they are store into a dictionary...

pos_dict = {}  # Initialize position dictionary

for k in range(len(pos_mat[:, 0])):  # Loop through the number of nodes
        pos_dict[k] = (pos_mat[k, 0], pos_mat[k, 1])  # Assign position values to node keys

# Step 2: Construct Graph Object
G = nx.Graph()  # Initialize graph

#  Use indices of adj_mat to successively add edges to graph

# 'conn_list' structure:

# [ 2, 1, 1
#   3, 4, 1
#     ...
#   175, 171, 1]

# This means at place (2,1) the adj_mat has a value of 1, so that is an edge...
# Now I simply must loop through this list and grab the first two arguments of each row
# that ex. (2,1) will be my input to G.add_edge

for i in range(len(list(conn_list))):
    # print(conn_list[i, :])
    row_i = conn_list[i, :]
    G.add_edge(row_i[0], row_i[1])

#  Visualize output, specify node positions
plt.figure(1)
nx.draw(G, pos=pos_dict, with_labels=True)
plt.show()


# Step 3: Apply Girvan_Newman algorithm to build communities

# Apply girvan_newman algorithm
#    Citation: "Community structure in social and biological networks"
#    M. Girvan, M., E. J. Newman, PNAS, 2002

# Can uncomment the below line and change the input to girvan_newman
# (and to nx.draw()) to G_test to see an example of how the function works
# with a more straightforward network

# G_test = nx.karate_club_graph()

comm_list = community.girvan_newman(G)  # Outputs list of nodes in each community as tuple
""" 
    This function deconstructs a graph object into communities 
    based on the girvan_newman algorithm (see 'references' folder)

    Parameters: 
    arg1 (G): Graph object input

    Returns: 
    c:  generator, holds lists of node labels in each community

"""

split1 = tuple(sorted(c) for c in next(comm_list))
comm1 = split1[0]  # First community (first tuple index)
comm2 = split1[1]  # Second community (second tuple index)

# Visualize the output by assigning different color to the communities
plt.figure(2)
color_map = []  # Initilize colormap

# assign nodes in community 1 as blue, else green
for node in comm1:
        color_map.append('blue')
for node in comm2:
        color_map.append('green')

nx.draw(G, pos=pos_dict, node_color=color_map, with_labels=True)
plt.show()

# Save the plot
#   In the future I want to load in then save each time frame
#   to make a pretty little video of the network communities dynamics
plt.savefig('communities_image.jpg') # just save to current directory