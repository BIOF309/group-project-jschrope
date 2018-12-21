import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Load in .txt and .xls files exported from Matlab (will explain them later)
pos_mat = np.genfromtxt('Node_Pos_t1.txt', delimiter=",")  # Holds node positions (among other info)
conn_df = pd.read_excel('conn_list.xls')  # Holds the 'connectivity' of each node
conn_list = np.genfromtxt('filename.txt')  # Essentially the indices of the adjacency matrix

# Step 1: Load in node_positions
#   'Networkx' allows me to specify node_positions in nd.draw()
#    if they are store into a dictionary...

pos_dict = {}  # Initialize position dictionary

for k in range(len(pos_mat[:, 0])): # Loop through the number of nodes
        pos_dict[k] = (pos_mat[k,0],pos_mat[k,1]) # assign position values to node keys

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

for i in range(len(conn_list)):
    # print(conn_list[i, :])
    row_i = conn_list[i, :]
    G.add_edge(row_i[0], row_i[1])

#  Visualize output, specify node positions
plt.figure(3)
nx.draw(G, pos=pos_dict)
plt.show()