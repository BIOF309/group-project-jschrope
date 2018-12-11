
# Motivation

Collective cell migration (CCM) observed in cancer metastasis

Overall goal is to understand the underlying physics of CCM through image analysis and mathematical modeling

Most imaging studies of CCM done in-vitro in cell culture of epithelial cell monolayer. In-vivo would be even better...

Zebrafish act as a model organism to study CCM
   
   1. Cluster of cells called the posterior lateral line primordium (pllp) migrates during early development
   
   2. Transparency allows for easy in-vivo confocal imaging
    
# Zebrafish pllp: Side view schematic
    
  ![alt text](images/pllp_side_schematic.jpg)
    
# Zebrafish pllp: Top view 3D projection movie
    
  ![alt text](images/pllp_movie.avi)
    
# Previous/Background Work

My lab has taken movies of different phenotypes of the pllp after making various chemical modifications to the system
    (ex. inhibiting FGF, Wnt pathways)
  
I previously wrote code to extract and track vertex/node movement. Thus I have an adjacency matrix and node positions for each time-frame.

1. Single time frame image

![alt text](images/newtork_image.jpg)


# Project Goal
My goal: Use python (networkx specifically) for network analysis of pllp to investigate physical differences between different pllp phenotypes

My first exercise is splitting network into communities based on the Girvin-Newman algorithm 
    
   1. Load in adjacency matrix and node positions from Matlab
    
   2. Construct "Graph" for each time-frame
    
   3. Calculate 'edge-betweenness'
    
   4. Use that value to build communities based on [https://journals.aps.org/pre/abstract/10.1103/PhysRevE.69.026113]
    
# Progress: Input Files

1. adj_mat.txt
![alt text](images/adj_mat.pdf)

2. node_tracks.txt

![alt text](images/tracks.pdf)

    -- node (x,y) positions given by first two columns

# Progress: Code
% Import the modules/packages that I need
from math import *
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import collections

% Build Graph 'G'

A = np.genfromtxt('adj_mat.txt', delimiter=",", skip_header=1)  # Load in adj_mat

tracks_mat = np.genfromtxt('Node_Pos_t1.txt', delimiter=",")  # Load positions

G = nx.from_numpy_matrix(A, create_using=None)  # Generate graph from adj_mat


num_nodes = len(tracks_mat) # Calculate number of nodes for given time-frame
 
%% Specify node position

pos_dict= {} 

for i in range(len(tracks_mat[:, 0])): # Loop through the number of nodes

   pos_dict[i] = (tracks_mat[i,0],tracks_mat[i,1]) # assign position values to node keys

plt.figure(1)
nx.draw(G, pos=pos_dict)
plt.show()

# Progress: Current Output

![alt text](images/first_try_network.jpg) (current output)

-- Adjacency matrix is clearly messed up. Look into on Matlab side. 
-- Also need to fix aspect ratio. 

# Next steps: Try using node positions and connectivity/edge list
1. Edge list
2. Node positions(as before)

# Girvan-Newman Algorithm to Build Communities

The algorithm's steps for community detection are summarized below:

1.The betweenness of all existing edges in the network is calculated first.

2.The edge with the highest betweenness is removed.

3.The betweenness of all edges affected by the removal is recalculated.

4.Steps 2 and 3 are repeated until no edges remain.

Python makes this easy: girvan_newman(G, most_valuable_edge=None)

# End goal
1. Build communities for each frame
2. Compile into a movie to examine the dynamics of the communities
    ex. Does a certain part of the pllp always constitute a "community"
        Do the community locations change under different phenotypes?
        DO the communities move/drift throughout the movie?
        
    -- I plan to have this done by the end of next week