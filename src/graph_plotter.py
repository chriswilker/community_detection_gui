import igraph

class GraphPlotter():
    def __init__(self, VertexColorer, EdgeColorer):
        self.VertexColorer = VertexColorer
        self.EdgeColorer = EdgeColorer

    def plot(self, *arguments, **keyword_arguments):
        self.arguments = arguments
        self.keyword_arguments = keyword_arguments

        self.determine_plot_colors()
        self.remove_extraneous_keyword_arguments()

        igraph.plot(*self.arguments, **self.keyword_arguments)

    def determine_plot_colors(self):
        if self.keyword_arguments['consider_sign']:
            self.color_edges()

        if self.keyword_arguments['membership']:
            self.color_vertices()

    def color_edges(self):
        graph = self.arguments[0]
        edge_colors = self.EdgeColorer.edge_colors(graph)
        self.keyword_arguments['edge_color'] = edge_colors

    def color_vertices(self):
        membership = self.keyword_arguments['membership']
        vertex_colors = self.VertexColorer.vertex_colors(membership)
        self.keyword_arguments['vertex_color'] = vertex_colors

    def remove_extraneous_keyword_arguments(self):
        self.keyword_arguments.pop('membership', None)
        self.keyword_arguments.pop('consider_sign', None)
