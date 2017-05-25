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

    def test_exception_with_incorrect_file_type(self):
        helper = path_helper.PathHelper()
        loader = graph_loader.GraphLoader(helper)

        file_directory = helper.path_to_module_directory(test_files)
        file_path = helper.join_paths(file_directory, 'not a graph.txt')

        value_error_raised = False
        try:
            loader.graph_from_file(file_path)
        except ValueError:
            value_error_raised = True
        self.assertTrue(value_error_raised)

if __name__ == '__main__':
    unittest.main()
