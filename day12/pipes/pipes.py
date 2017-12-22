#!/usr/bin/env python3.6
import argparse
import re

class Vertex:
    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.edges = []

    def add_edge(self, vertex_number):
        if vertex_number not in self.edges:
            self.edges.append(vertex_number)


class Graph:
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, vertex_number, edges):
        if vertex_number not in self.vertices:
            self.vertices[vertex_number] = Vertex(vertex_number)
        for edge in edges:
            self.vertices[vertex_number].add_edge(edge)
            if edge not in self.vertices:
                self.vertices[edge] = Vertex(edge)
            self.vertices[edge].add_edge(vertex_number)

    def find_connected_components(self, start_vertex):
        stack = []
        connected_components = set()

        stack.append(start_vertex)
        while stack:
            vertex = stack.pop()
            if vertex not in connected_components:
                connected_components.add(vertex)
                for edge in self.vertices[vertex].edges:
                    stack.append(edge)

        return connected_components


def parse_line(line):
    parse_string = '(\d+) <-> (.*)'

    m = re.search(parse_string, line)
    groups = m.groups()
    vertex_number = int(groups[0])
    edges = [int(edge) for edge in groups[1].split(',')]

    return vertex_number, edges


parser = argparse.ArgumentParser(
        description='Solution for part 1 of day 12')
parser.add_argument('file', metavar='file', type=str)

args = parser.parse_args()

graph = Graph()
with open(args.file) as f:
    for line in f:
        vertex_number, edges = parse_line(line.strip())
        graph.add_vertex(vertex_number, edges)

    connected_components = graph.find_connected_components(0)
    print(len(connected_components))
