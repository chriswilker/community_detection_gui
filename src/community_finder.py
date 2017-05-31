import louvain

class CommunityFinder():
    def membership_list(
            self, graph=False, positive_graph=False, negative_graph=False, 
            detection_method='Modularity', resolution_parameter=1.0
            ):
        self.graph = graph
        self.positive_graph = positive_graph
        self.negative_graph = negative_graph
        self.detection_method = detection_method
        self.resolution_parameter = resolution_parameter

        self.find_membership_list()

        return self.membership

    def find_membership_list(self):
        if self.positive_graph or self.negative_graph:
            self.find_membership_list_from_signed_graphs()
        else:
            self.find_membership_list_from_graph()

    def find_membership_list_from_signed_graphs(self):
        self.membership, quality = louvain.find_partition_multiplex([
            self.layer(self.positive_graph, 1.0), 
            self.layer(self.negative_graph, -1.0)
            ])

    def layer(self, signed_graph, layer_weight):
        return louvain.Layer(
            graph = signed_graph, method = self.detection_method, 
            layer_weight = layer_weight, 
            resolution_parameter = self.resolution_parameter
            )

    def find_membership_list_from_graph(self):
        partition = louvain.find_partition(
            self.graph, method = self.detection_method,
            resolution_parameter = self.resolution_parameter
            );
        self.membership = partition.membership
