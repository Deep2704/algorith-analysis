# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List

from maze.util import Coordinates
from maze.graph import Graph

class EdgeListGraph(Graph):
    def __init__(self):
        self.vertices = []
        self.edges = []
    
    def addVertex(self, label: Coordinates):
        if label not in self.vertices:
            self.vertices.append(label)
    
    def addVertices(self, vertLabels: List[Coordinates]):
        for label in vertLabels:
            if label not in self.vertices:
                self.vertices.append(label)
    
    def addEdge(self, vert1: Coordinates, vert2: Coordinates, addWall: bool = False) -> bool:
        if vert1 in self.vertices and vert2 in self.vertices:
            if not self.hasEdge(vert1, vert2):
                self.edges.append((vert1, vert2, addWall))
                return True
        return False
    
    def updateWall(self, vert1: Coordinates, vert2: Coordinates, wallStatus: bool) -> bool:
        for i, edge in enumerate(self.edges):
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                self.edges[i] = (vert1, vert2, wallStatus)
                return True
        return False
    
    def removeEdge(self, vert1: Coordinates, vert2: Coordinates) -> bool:
        for edge in self.edges:
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                self.edges.remove(edge)
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
        for edge in self.edges:
            if edge[0] == label:
                neighbors.append(edge[1])
            elif edge[1] == label:
                neighbors.append(edge[0])
        return neighbors
