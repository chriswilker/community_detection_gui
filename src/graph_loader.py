import igraph

class GraphLoader():
    def __init__(self, PathHelper):
        self.PathHelper = PathHelper

    def graph_from_file(self, file_path):
        self.file_path = file_path
        self.determine_file_type()
        self.determine_graph()
        return self.graph

    def determine_file_type(self):
        self.file_type = self.PathHelper.file_extension(self.file_path)

    def determine_graph(self):
        if self.file_type == '.pickle':
            self.graph = igraph.Graph.Read_Pickle(self.file_path)
        else:
            raise ValueError(
                'Not able to load a graph from a {} file.'.format(
                    self.file_type
                    )
                )
