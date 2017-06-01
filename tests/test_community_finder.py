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

        splitter = graph_splitter.GraphSplitter()
        self.finder = community_finder.CommunityFinder(splitter)
        self.comparer = graph_comparer.GraphComparer()

    def test_signed_modularity_membership_list(self):
        expected_membership_list = [1, 0, 0, 2, 0, 3, 4]

        membership_list = self.finder.membership_list(
            self.graph, consider_sign = True, detection_method = 'Modularity', 
            resolution_parameter = 1.0 
            )

        self.assertEqual(expected_membership_list, membership_list)

    def test_unsigned_modularity_membership_list(self):
        expected_membership_list = [3, 2, 2, 1, 1, 0, 0]

        membership_list = self.finder.membership_list(
            self.graph, consider_sign = False, detection_method = 'Modularity', 
            resolution_parameter = 1.0
            )

        self.assertEqual(expected_membership_list, membership_list)

if __name__ == '__main__':
    unittest.main()
