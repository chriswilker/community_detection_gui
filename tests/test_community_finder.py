import unittest
import community_detection_gui.src.community_finder as community_finder

import igraph
import copy
import community_detection_gui.src.graph_splitter as graph_splitter
import community_detection_gui.src.graph_comparer as graph_comparer

class TestCommunityFinder(unittest.TestCase):
    def setUp(self):
        self.graph = igraph.Graph()

        self.graph.add_vertices(7)
        self.graph.add_edges([(1, 2), (3, 4), (2, 4), (4, 5), (5, 6)])
        self.graph.es['sign'] = [1, -1, 1, -1, -1]

        self.graph.es['edge sequence attribute'] = (
                'edge sequence attribute value'
                )
        self.graph.es[2]['edge attribute'] = 'edge attribute value'
        self.graph.vs['vertex sequence attribute'] = (
                'vertex sequence attribute value'
                )
        self.graph.vs[5]['vertex attribute'] = 'vertex attribute value'
        self.graph['graph attribute'] = 'graph attribute value'

    def test_split_graph(self):
        splitter = graph_splitter.GraphSplitter()
        finder = community_finder.CommunityFinder(splitter)
        comparer = graph_comparer.GraphComparer()

        expected_positive_graph = copy.copy(self.graph)
        expected_positive_graph.delete_edges([1, 3, 4])

        expected_negative_graph = copy.copy(self.graph)
        expected_negative_graph.delete_edges([0, 2])

        finder.graph = self.graph
        finder.split_graph()

        self.assertTrue(comparer.equal(
            finder.positive_graph, expected_positive_graph
            ))
        self.assertTrue(comparer.equal(
            finder.negative_graph, expected_negative_graph
            ))

if __name__ == '__main__':
    unittest.main()
