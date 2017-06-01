import unittest
import community_detection_gui.src.graph_plotter as graph_plotter

import igraph
import community_detection_gui.src.vertex_colorer as vertex_colorer
import community_detection_gui.src.edge_colorer as edge_colorer

class TestGraphPlotter(unittest.TestCase):
    def setUp(self):
        VertexColorer = vertex_colorer.VertexColorer()
        EdgeColorer = edge_colorer.EdgeColorer()
        self.plotter = graph_plotter.GraphPlotter(VertexColorer, EdgeColorer)

        graph = igraph.Graph()

        graph.add_vertices(7)
        graph.add_edges([(1, 3), (6, 2), (3, 0), (0, 1), (3, 4), (5, 2)])
        graph.es['sign'] = [-1, -1, 1, -1, -1, -1]

        self.plotter.arguments = [graph]

        self.negative_color = (1.0, 0.0, 0.0, 1.0)
        self.positive_color = (0.0, 1.0, 0.0, 1.0)

        self.plotter.keyword_arguments = {}

    def test_color_edges(self):
        self.plotter.color_edges()

        expected_edge_colors = [
            self.negative_color, self.negative_color, self.positive_color, 
            self.negative_color, self.negative_color, self.negative_color,
            ]

        self.assertEqual(
            self.plotter.keyword_arguments['edge_color'], expected_edge_colors
            )

    def test_color_vertices(self):
        self.plotter.keyword_arguments['membership'] = [2, 5, 3, 4, 3, 1, 0]

        self.plotter.color_vertices()

        expected_vertex_colors = [
            (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 1.0, 0.0, 1.0),
            (1.0, 0.0, 1.0, 1.0), (1.0, 1.0, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0),
            (1.0, 0.0, 0.0, 1.0)
            ]

        self.assertEqual(
            self.plotter.keyword_arguments['vertex_color'], 
            expected_vertex_colors
            )

    def test_determine_plot_colors(self):
        self.plotter.keyword_arguments['membership'] = [2, 5, 3, 4, 3, 1, 0]
        self.plotter.keyword_arguments['consider_sign'] = True

        self.plotter.determine_plot_colors()

        expected_edge_colors = [
            self.negative_color, self.negative_color, self.positive_color, 
            self.negative_color, self.negative_color, self.negative_color,
            ]

        expected_vertex_colors = [
            (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 1.0, 0.0, 1.0),
            (1.0, 0.0, 1.0, 1.0), (1.0, 1.0, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0),
            (1.0, 0.0, 0.0, 1.0)
            ]

        self.assertEqual(
            self.plotter.keyword_arguments['edge_color'], expected_edge_colors
            )

        self.assertEqual(
            self.plotter.keyword_arguments['vertex_color'], 
            expected_vertex_colors
            )

if __name__ == '__main__':
    unittest.main()
