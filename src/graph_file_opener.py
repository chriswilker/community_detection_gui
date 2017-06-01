import tkFileDialog

class GraphFileOpener():
    def __init__(self, GraphLoader, CommunityGUI):
        self.GraphLoader = GraphLoader
        self.CommunityGUI = CommunityGUI

    def load_graph(self):
        self.open_file()
        if self.graph_file_path:
            graph = self.GraphLoader.graph_from_file(self.graph_file_path)

            self.CommunityGUI.set_graph(graph)
            self.CommunityGUI.load_gui()

    def open_file(self):
        self.graph_file_path = tkFileDialog.askopenfilename(
            filetypes=[('All files', '*')]
            )
