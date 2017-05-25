import unittest
import community_detection_gui.src.graph_comparer as graph_comparer

import igraph
import copy

class TestGraphComparer(unittest.TestCase):

    def setUp(self):
        self.graph = igraph.Graph()
        self.graph.add_vertices(4)
        self.graph.add_edges([(0,1), (0,3), (1,2), (2,3)])
        self.graph.es['edge sequence attribute'] = (
                'edge sequence attribute value'
                )
        self.graph.es[1]['edge attribute'] = 'edge attribute value'
        self.graph.vs['vertex sequence attribute'] = (
                'vertex sequence attribute value'
                )
        self.graph.vs[2]['vertex attribute'] = 'vertex attribute value'
        self.graph['graph attribute'] = 'graph attribute value'


    def test_compare_graph_and_graph_copy(self):
        graph_copy = copy.copy(self.graph)

        comparer = graph_comparer.GraphComparer()

        self.assertTrue(comparer.equal(self.graph, graph_copy))
        self.assertTrue(comparer.edges_equal(self.graph, graph_copy))
        self.assertTrue(comparer.edge_lists_equal(self.graph, graph_copy))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, graph_copy))
        self.assertTrue(comparer.edge_attributes_equal(self.graph, graph_copy))
        self.assertTrue(comparer.vertices_equal(self.graph, graph_copy))
        self.assertTrue(comparer.number_vertices_equal(self.graph, graph_copy))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, graph_copy))
        self.assertTrue(comparer.vertex_attributes_equal(self.graph, graph_copy))
        self.assertTrue(comparer.attributes_equal(self.graph, graph_copy))

    def test_add_edge(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.add_edges([(1, 3)])

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertFalse(comparer.edges_equal(self.graph, changed_graph))
        self.assertFalse(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_add_edge_sequence_attribute(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.es['new edge sequence attribute'] = -3

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertFalse(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertFalse(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_change_edge_sequence_attribute_value(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.es['edge sequence attribute'] = -3

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertFalse(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_add_edge_attribute(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.es[0]['new edge attribute'] = 'new edge attribute value'

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertFalse(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertFalse(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_change_edge_attribute_value(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.es[0]['edge attribute'] = (
                'edge attribute replacement value'
                )

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertFalse(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_add_vertices(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.add_vertices(2)

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertTrue(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertices_equal(self.graph, changed_graph))
        self.assertFalse(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_add_vertex_sequence_attribute(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.vs['new vertex sequence attribute'] = 1

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertTrue(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_change_vertex_sequence_attribute_value(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.vs['vertex sequence attribute'] = 3

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertTrue(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_add_vertex_attribute(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.vs[2]['new vertex attribute'] = (
                'new vertex attribute value'
                )

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertTrue(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_change_vertex_attribute_value(self):
        changed_graph = copy.copy(self.graph)
        changed_graph.vs[2]['vertex attribute'] = (
                'vertex attribute replacement value'
                )

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertTrue(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.attributes_equal(self.graph, changed_graph))

    def test_add_graph_attribute(self):
        changed_graph = copy.copy(self.graph)
        changed_graph['new graph attribute'] = 'new graph attribute value'

        comparer = graph_comparer.GraphComparer()

        self.assertFalse(comparer.equal(self.graph, changed_graph))
        self.assertTrue(comparer.edges_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_lists_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.edge_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.number_vertices_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_sequence_attributes_equal(self.graph, changed_graph))
        self.assertTrue(comparer.vertex_attributes_equal(self.graph, changed_graph))
        self.assertFalse(comparer.attributes_equal(self.graph, changed_graph))

if __name__ == '__main__':
    unittest.main()
