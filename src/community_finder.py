class CommunityFinder():
    def __init__(self, Splitter):
        self.Splitter = Splitter

    def find_members(
            self, graph, detection_method='Modularity', 
            resolution_parameter=1.0, consider_sign=True
            ):
        self.graph = graph
        self.detection_method = detection_method
        self.resolution_parameter = resolution_parameter
        self.consider_sign = True

        if self.consider_sign:
            self.split_graph()

    def split_graph(self):
        self.positive_graph = self.Splitter.positive_graph(self.graph)
        self.negative_graph = self.Splitter.negative_graph(self.graph)

    def membership_
