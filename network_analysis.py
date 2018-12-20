# Import the modules/packages that I need
from math import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import collections


# Build Graph 'G'
A = np.genfromtxt('adj_mat.txt', delimiter=",", skip_header=1)  # Load in adj_mat
adj_mat = A[A > 0]
tracks_mat = np.genfromtxt('Node_Pos_t1.txt', delimiter=",")  # Load positions
G = nx.from_numpy_matrix(adj_mat, create_using=None)  # Generate graph from adj_mat

num_nodes = len(tracks_mat) # Calculate number of nodes for given time-frame

##  Now must specifiy node positions...
#       I currently have a network graph with the correct 'connectivity' but the
#       node positions are randomly generated each time by default

# Create position dictionary
pos_dict= {}
#G.add_nodes_from(num_nodes)


for i in range(len(tracks_mat[:, 0])): # Loop through the number of nodes
        pos_dict[i] = (tracks_mat[i,0],tracks_mat[i,1]) # assign position values to node keys
        #for j in range(conn):
        #G.add_edge([i,conn(i)]

print(pos_dict)

plt.figure(1)
nx.draw(G, pos=pos_dict)
#plt.show()

#plt.savefig('books_read.png')
plt.savefig('first_try_network.jpg')

## Plot degree distribution
# (find online, use collections)

## Calculate edge betweeness centrality
edgebtwn = nx.edge_betweenness_centrality(G, k=None, normalized=True, weight=None, seed=None)
type(edgebtwn)
# we just want the numbers from this output dictionary
items = edgebtwn.values()
print(items)


# Histogram of edge_betweenness centrality
#plt.figure(2)
#plt.hist(items)


# From datacamp...

# Zip lists: zipped_lists
# zipped_lists = zip(feature_names,row_vals) # zip up two lists


# Create a dictionary: rs_dict
# rs_dict = dict(zipped_lists) # convert to dictionary

# Print the dictionary
# print(rs_dict)


# This is making a dictionary then converting it to dataframe. dont need conversion but looks like easy way to make dictionary
# Create a DataFrame with labels and species as columns: df
# df = pd.DataFrame({'labels': labels, 'species': species})