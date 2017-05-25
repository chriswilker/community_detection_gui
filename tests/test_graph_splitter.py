import unittest
import community_detection_gui.src.graph_splitter as graph_splitter

import community_detection_gui.src.graph_comparer as graph_comparer
import igraph
import copy


class TestGraphSplitter(unittest.TestCase):
    def setUp(self):
        self.graph = igraph.Graph()

        self.graph.add_vertices(5)
        self.graph.add_edges([(0, 2), (1, 2), (2, 3), (1, 4)])
        self.graph.es['sign'] = [1, -1, 1, -1]

        self.graph.es['edge sequence attribute'] = (
                'edge sequence attribute value'
                )
        self.graph.es[3]['edge attribute'] = 'edge attribute value'
        self.graph.vs['vertex sequence attribute'] = (
                'vertex sequence attribute value'
                )
        self.graph.vs[2]['vertex attribute'] = 'vertex attribute value'
        self.graph['graph attribute'] = 'graph attribute value'

    def test_positive_graph(self):
        expected_positive_graph = copy.copy(self.graph)
        expected_positive_graph.delete_edges([1, 3])

        splitter = graph_splitter.GraphSplitter()
        positive_graph = splitter.positive_graph(self.graph)

        comparer = graph_comparer.GraphComparer()
        self.assertTrue(comparer.equal(positive_graph, expected_positive_graph))

    def test_negative_graph(self):
        expected_negative_graph = copy.copy(self.graph)
        expected_negative_graph.delete_edges([0, 2])

        splitter = graph_splitter.GraphSplitter()
        negative_graph = splitter.negative_graph(self.graph)

        comparer = graph_comparer.GraphComparer()
        self.assertTrue(comparer.equal(expected_negative_graph, negative_graph))

if __name__ == '__main__':
    unittest.main()
