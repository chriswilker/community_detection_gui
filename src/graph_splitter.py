import igraph
import copy

class GraphSplitter():
    def positive_graph(self, graph):
        self.graph = graph
        return self.graph_with_only_edges_of_sign(1)

    def negative_graph(self, graph):
        self.graph = graph
        return self.graph_with_only_edges_of_sign(-1)

    def graph_with_only_edges_of_sign(self, desired_edge_sign):
        modified_edges_graph = copy.copy(self.graph)
        
        i = 0
        while i < len(modified_edges_graph.es):
            current_edge = modified_edges_graph.es[i]
            if int(current_edge['sign']) != desired_edge_sign:
                modified_edges_graph.delete_edges(i)
            else:
                i += 1

        return modified_edges_graph
