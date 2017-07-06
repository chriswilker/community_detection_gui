import unittest
import community_detection_gui.src.community_csv_generator as generator

import community_detection_gui.src.community_finder as community_finder
import community_detection_gui.src.graph_splitter as graph_splitter

class TestCommunityCSVGenerator(unittest.TestCase):
    def setUp(self):
        splitter = graph_splitter.GraphSplitter()
        finder = community_finder.CommunityFinder(splitter)
        self.generator = generator.CommunityCSVGenerator(finder)

if __name__ == '__main__':
    unittest.main()
