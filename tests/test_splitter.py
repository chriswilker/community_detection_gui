import unittest
import community_detection_gui.src.splitter as splitter
import community_detection_gui.src.compare as compare

class TestSplitter(unittest.TestCase):
    def setUp(self):
        graph = igraph.Graph()
        graph.add_vertices(4)
        graph.add_edges([(0, 2), (1, 2), (2, 3), (1, 4)])
        graph.es['sign'] = [1, -1, 1, -1]

    def test_positive_graph(self):
        expected_positive_graph = igraph.Graph()
        expected_positive_graph.add_vertices(2)
        expected_positive_graph.add_edges([(0, 2), (2, 3)])
        expected_positive_graph.es['sign'] = [1, 1]

        positive_graph = splitter.positive_graph(graph)

    def test_negative_graph(self):
        expected_negative_graph = igraph.Graph()
        expected_negative_graph.add_vertices(2)
        expected_negative_graph.add_edges([(1, 2), (1, 4)])
        expected_negative_graph.es['sign'] = [-1, -1]

        negative_graph = splitter.negative_graph(graph)

        self.assertTrue(
            compare.graphs_equal(negative_graph, expected_negative_graph)
            )

if __name__ == '__main__':
    unittest.main()
