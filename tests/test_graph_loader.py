import unittest

import community_detection_gui.src.graph_loader as graph_loader

import community_detection_gui.src.path_helper as path_helper
import community_detection_gui.tests.test_files as test_files
import community_detection_gui.src.graph_comparer as graph_comparer

import igraph

class TestGraphLoader(unittest.TestCase):
    def test_load_pickle(self):
        helper = path_helper.PathHelper()
        loader = graph_loader.GraphLoader(helper)

        file_directory = helper.path_to_module_directory(test_files)
        file_path = helper.join_paths(file_directory, 'test graph.pickle')

        # TODO make the graph from scratch that is equivalent to the graph from
        # the file
        compared_graph = igraph.Graph.Read_Pickle(file_path)

        test_graph = loader.graph_from_file(file_path)

        comparer = graph_comparer.GraphComparer()

        self.assertTrue(comparer.equal(compared_graph, test_graph))

if __name__ == '__main__':
    unittest.main()
