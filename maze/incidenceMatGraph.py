# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', "Deep prabhu"
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph

class IncMatGraph(Graph):
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.incidence_matrix = []
    
    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            self.vertices.append(label)
            for row in self.incidence_matrix:
                row.append(0)
    
    def addVertices(self, vertLabels: List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)
    
    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            if not self.hasEdge(vert1, vert2):
                edge = (vert1, vert2, addWall)
                self.edges.append(edge)
                
                new_column = [0] * len(self.vertices)
                new_column[self.vertices.index(vert1)] = 1
                new_column[self.vertices.index(vert2)] = 1
                
                self.incidence_matrix.append(new_column)
                return True
        return False
    
    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        for i, edge in enumerate(self.edges):
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                self.edges[i] = (vert1, vert2, wallStatus)
                return True
        return False
    
    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        for i, edge in enumerate(self.edges):
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                self.edges.pop(i)
                self.incidence_matrix.pop(i)
                return True
        return False
    
    def hasVertex(self, label: Coordinates) -> bool:
        return label in self.vertices
    
    def hasEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        for edge in self.edges:
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                return True
        return False
    
    def getWallStatus(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        for edge in self.edges:
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                return edge[2]
        return False
    
    def neighbours(self, label: Coordinates) -> List[Coordinates]:
        neighbors = []
        for i, edge in enumerate(self.edges):
            if edge[0] == label:
                neighbors.append(edge[1])
            elif edge[1] == label:
                neighbors.append (edge[0])
        return neighbors
