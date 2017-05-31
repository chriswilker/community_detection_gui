import unittest
import community_detection_gui.src.edge_colorer as edge_colorer

import igraph

class TestEdgeColorer(unittest.TestCase):
    def setUp(self):
        self.colorer = edge_colorer.EdgeColorer()

        self.graph = igraph.Graph()

        self.graph.add_vertices(4)
        self.graph.add_edges([(1, 3), (1, 2), (2, 3), (3, 0), (0, 1)])
        self.graph.es['sign'] = [1, -1, 1, -1, -1]

        self.negative_color = (1.0, 0.0, 0.0, 1.0)
        self.positive_color = (0.0, 1.0, 0.0, 1.0)

    def test_determine_sign_colors(self):
        self.colorer.determine_sign_colors()
        sign_colors = self.colorer.sign_colors

        expected_sign_colors = [self.negative_color, self.positive_color]

        self.assertEqual(expected_sign_colors, sign_colors)

    def test_determine_edge_sign_membership(self):
        self.colorer.graph = self.graph
        self.colorer.determine_edge_sign_membership()
        edge_sign_membership = self.colorer.edge_sign_membership

        expected_edge_sign_membership = [1, 0, 1, 0, 0]

        self.assertEqual(edge_sign_membership, expected_edge_sign_membership)

    def test_edge_colors_from_signs(self):
        self.colorer.graph = self.graph
        self.colorer.sign_colors = [self.negative_color, self.positive_color]
        self.colorer.edge_sign_membership = [1, 0, 1, 0, 0]
        edge_colors = self.colorer.edge_colors_from_signs()

        expected_edge_colors = [
            self.positive_color, self.negative_color, self.positive_color, 
            self.negative_color, self.negative_color
            ]

        self.assertEqual(edge_colors, expected_edge_colors)

    def test_edge_colors(self):
        edge_colors = self.colorer.edge_colors(self.graph)

        expected_edge_colors = [
            self.positive_color, self.negative_color, self.positive_color, 
            self.negative_color, self.negative_color
            ]

        self.assertEqual(edge_colors, expected_edge_colors)

if __name__ == '__main__':
    unittest.main()
