#!/usr/bin/env python
# coding: utf-8

# In[ ]:


""" 
Graph Theory

"""

import numpy
import random

class Graph:
    """ Class for graph implementations. """
    
    def __init__(self, node_count, weighted = False, directed = False):
        """ Initialize the graph structure with basic details"""
        
        self.node_count = node_count
        self.weighted = weighted
        self.directed = directed
        
        self.graph = [[None for column in range(node_count)] for row in range(node_count)] 
            
    
    def create_edge(self, source, destination, weight = 1):
        """ function to create edge between node(source, destination)
            default weight is 1. If no edge exists, the field is None
        """
        self.graph[source][destination] = weight
        if not self.directed: self.graph[destination][source] = weight
    
        return
    
    
    def get_graph(self, graph_type = "matrix"):
        """ get the graph in either matrix or adjecancy list format """
        
        if graph_type == "matrix":
            return self.graph
        
        adjacency_list = []
        for row in range(self.node_count):
            each_node = []
            for column in range(self.node_count):
                if self.graph[row][column]:
                    each_node.append({column:self.graph[row][column]})
            
            adjacency_list.append(each_node)
        
        return adjacency_list
            
    
    def __str__(self):
        """ returns the graph so far """
        ret_string = ""
        
        for row in self.graph:
            ret_string += str(row) + "\n"
        return ret_string
    

