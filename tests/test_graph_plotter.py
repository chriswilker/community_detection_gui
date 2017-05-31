import unittest
import community_detection_gui.src.graph_plotter as graph_plotter

class TestGraphPlotter(unittest.TestCase):
    def setUp(self):
        self.plotter = graph_plotter.GraphPlotter()

    def test_plot(self):
        self.plotter.plot(graph, membership=False, layout="kk", positive_graph=False, negative_graph=False


if __name__ == '__main__':
    unittest.main()
