import tkFileDialog

class GraphFileOpener():
    def __init__(self, GraphLoader):
        self.GraphLoader = GraphLoader

    def load_graph(self):
        self.open_file()
        if self.graph_file_path:
            graph = self.GraphLoader.graph_from_file(self.graph_file_path)

            # TODO add link to the next GUI.
            print('next GUI not implemented')

    def open_file(self):
        self.graph_file_path = tkFileDialog.askopenfilename(
            filetypes=[('All files', '*')]
            )
