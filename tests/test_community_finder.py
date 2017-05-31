import unittest
import community_detection_gui.src.community_finder as community_finder

import igraph
import copy
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

        self.positive_graph = copy.copy(self.graph)
        self.positive_graph.delete_edges([1, 3, 4])

        self.negative_graph = copy.copy(self.graph)
        self.negative_graph.delete_edges([0, 2])

        self.finder = community_finder.CommunityFinder()
        self.comparer = graph_comparer.GraphComparer()

    def test_signed_modularity_membership_list(self):
        expected_membership_list = [1, 0, 0, 2, 0, 3, 4]

        membership_list = self.finder.membership_list(
            positive_graph = self.positive_graph, 
            negative_graph = self.negative_graph, 
            detection_method = 'Modularity', resolution_parameter = 1.0, 
            )

        self.assertEqual(expected_membership_list, membership_list)

    def test_unsigned_modularity_membership_list(self):
        expected_membership_list = [3, 2, 2, 1, 1, 0, 0]

        membership_list = self.finder.membership_list(
            graph = self.graph, detection_method = 'Modularity', 
            resolution_parameter = 1.0
            )

        self.assertEqual(expected_membership_list, membership_list)

if __name__ == '__main__':
    unittest.main()
