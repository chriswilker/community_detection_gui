import unittest
import community_detection_gui.src.graph_comparer as graph_comparer

import igraph
import copy

class TestGraphComparer(unittest.TestCase):

    def setUp(self):
        self.graph = igraph.Graph()
        self.graph.add_vertices(4)
        self.graph.add_edges([(0,1), (0,3), (1,2), (2,3)])
        self.graph.es[1]['foo'] = 'bar'
        self.graph.vs['hello'] = 'goodbye'
        self.graph['name'] = 'test'
        self.reference_graph = copy.copy(self.graph)

    def test_graphs_equal(self):
        self.assertTrue(compare.graphs_equal(self.graph, self.reference_graph))
        self.graph.es[0]['one'] = 'two'
        self.assertFalse(compare.graphs_equal(self.graph, self.reference_graph))

    def test_graph_edges_equal(self):
        self.assertTrue(
            compare.graph_edges_equal(self.graph, self.reference_graph)
            )
        self.graph.add_edges([(1, 3)])
        self.assertFalse(
            compare.graph_edges_equal(self.graph, self.reference_graph)
            )

    def test_graph_attributes_equal(self):
        self.assertTrue(
            compare.graph_attributes_equal(self.graph, self.reference_graph)
            )
        self.graph.vs['hello'] = 'hello'
        self.assertFalse(
            compare.graph_attributes_equal(self.graph, self.reference_graph)
            )

if __name__ == '__main__':
    unittest.main()
