import unittest

import community_detection_gui.src.graph_loader as graph_loader

import community_detection_gui.src.get_path as get_path
import community_detection_gui.tests.test_files as test_files
import community_detection_gui.src.compare as compare

import igraph

class TestGraphLoader(unittest.TestCase):
    def test_load_pickle(self):
        test_loader = graph_loader.GraphLoader(igraph.Graph)

        file_directory = get_path.path_to_module_directory(test_files)
        file_path = get_path.join_paths(file_directory, 'test_graph.pickle')

        compared_graph = igraph.Graph.Read_Pickle(file_path)
        test_graph = test_loader.load_graph_from_file(file_path, 'pickle')

        self.assertTrue(compared_graph, test_graph)

if __name__ == '__main__':
    unittest.main()
