import igraph
import copy

class GraphPlotter():
    def __init__(self, VertexColorer, EdgeColorer):
        self.VertexColorer = VertexColorer
        self.EdgeColorer = EdgeColorer

    def plot(self, *arguments, **keyword_arguments):
        # Use a copy of the given graph, so that removing duplicate edges does 
        # not modify the given graph.
        self.arguments = copy.copy(arguments)
        self.keyword_arguments = keyword_arguments

        self.remove_duplicate_edges_if_necessary()
        self.determine_plot_colors()
        self.remove_extraneous_keyword_arguments()

        igraph.plot(*self.arguments, **self.keyword_arguments)

    def remove_duplicate_edges_if_necessary(self):
        graph = self.arguments[0]
        if self.keyword_arguments['remove duplicate edges']:
            for i in range(len(graph.vs)):
                for j in range(len(graph.vs)):
                    if i != j:
                        while len(
                                self.edges_between_vertices(graph, i, j)
                                ) >= 2:
                            graph.delete_edges(graph.get_eid(i, j))

    def edges_between_vertices(
            self, graph, first_vertex_index, second_vertex_index
            ):
        edges_from_first = graph.es.select(_from = first_vertex_index)
        return edges_from_first.select(_to = second_vertex_index)

    def determine_plot_colors(self):
        if self.keyword_arguments['consider sign']:
            self.color_edges()

        if self.keyword_arguments['membership']:
            self.color_vertices()

    def color_edges(self):
        if not 'edge_color' in self.keyword_arguments.keys():
            graph = self.arguments[0]
            edge_colors = self.EdgeColorer.edge_colors(graph)
            self.keyword_arguments['edge_color'] = edge_colors

    def color_vertices(self):
        if not 'vertex_color' in self.keyword_arguments.keys():
            membership = self.keyword_arguments['membership']
            vertex_colors = self.VertexColorer.vertex_colors(membership)
            self.keyword_arguments['vertex_color'] = vertex_colors

    def remove_extraneous_keyword_arguments(self):
        self.keyword_arguments.pop('remove duplicate edges', None)
        self.keyword_arguments.pop('membership', None)
        self.keyword_arguments.pop('consider sign', None)
