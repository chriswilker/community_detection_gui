import unittest
import community_detection_gui.src.vertex_colorer as vertex_colorer

class TestVertexColorer(unittest.TestCase):
    def setUp(self):
        self.colorer = vertex_colorer.VertexColorer()

    def test_determine_group_colors(self):
        self.colorer.membership = [0, 1, 4, 3, 2, 3, 2, 1]
        self.colorer.determine_group_colors()
        group_colors = self.colorer.group_colors

        expected_group_colors = [
            (1.0, 0.0, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), 
            (1.0, 1.0, 0.0, 1.0), (1.0, 0.0, 1.0, 1.0)
            ]

        self.assertEqual(group_colors, expected_group_colors)

    def test_vertex_colors_from_group_colors(self):
        self.colorer.membership = [1, 2, 3, 2, 0]
        self.colorer.group_colors = [
            (1.0, 0.0, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0),
            (1.0, 1.0, 0.0, 1.0)
            ]

        vertex_colors = self.colorer.vertex_colors_from_group_colors()

        expected_vertex_colors = [
            (0.0, 1.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0), (1.0, 1.0, 0.0, 1.0), 
            (0.0, 0.0, 1.0, 1.0), (1.0, 0.0, 0.0, 1.0)
            ]

        self.assertEqual(expected_vertex_colors, vertex_colors)

    def test_vertex_colors(self):
        membership = [2, 5, 3, 4, 3, 1, 3, 0, 2]
        vertex_colors = self.colorer.vertex_colors(membership)

        expected_vertex_colors = [
            (0.0, 0.0, 1.0, 1.0), (0.0, 1.0, 1.0, 1.0), (1.0, 1.0, 0.0, 1.0),
            (1.0, 0.0, 1.0, 1.0), (1.0, 1.0, 0.0, 1.0), (0.0, 1.0, 0.0, 1.0),
            (1.0, 1.0, 0.0, 1.0), (1.0, 0.0, 0.0, 1.0), (0.0, 0.0, 1.0, 1.0)
            ]

        self.assertEqual(vertex_colors, expected_vertex_colors)

if __name__ == '__main__':
    unittest.main()
