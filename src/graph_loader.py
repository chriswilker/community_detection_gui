import igraph.Graph as Graph

class GraphLoader():
    def __init__(self, GraphObject):
        self.GraphObject = GraphObject

    def load_graph_from_file(self, file_path, file_type):
        if file_type == 'pickle':
            return self.graph_from_pickle(file_path)

    def graph_from_pickle(self, file_path):
        read_graph_object = Graph.Read_Pickle(file_path)
        return self.GraphObject(read_graph_object)
