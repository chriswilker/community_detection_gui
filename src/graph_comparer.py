class GraphComparer():
    def equal(self, first_graph, second_graph):
        return (
            self.edges_equal(first_graph, second_graph) 
            and self.vertices_equal(first_graph, second_graph) 
            and self.attributes_equal(first_graph, second_graph)
            )

    def edges_equal(self, first_graph, second_graph):
        return (
            self.edge_lists_equal(first_graph, second_graph) 
            and self.edge_sequence_attributes_equal(first_graph, second_graph) 
            and self.edge_attributes_equal(first_graph, second_graph)
            )

    def edge_lists_equal(self, first_graph, second_graph):
        edges_are_equal = False
        if (len(first_graph.es) == len(second_graph.es)):
            edges_are_equal = (
                first_graph.get_edgelist() 
                == second_graph.get_edgelist()
                )
        return edges_are_equal

    def edge_sequence_attributes_equal(self, first_graph, second_graph):
        return self.sequence_attributes_equal(
            first_graph.es, second_graph.es
            )

    def sequence_attributes_equal(self, first_sequence, second_sequence):
        if (
                len(first_sequence.attributes()) 
                == len(second_sequence.attributes())
                ):
            return first_sequence.attributes() == second_sequence.attributes()
        return False

    def edge_attributes_equal(self, first_graph, second_graph):
        return self.sequence_value_attributes_equal(
            first_graph.es, second_graph.es
            )

    def sequence_value_attributes_equal(self, first_sequence, second_sequence):
        if len(first_sequence) == len(second_sequence):
            for i, value in enumerate(first_sequence):
                if not (
                        self.sequence_attributes_equal(
                            value, second_sequence[i]
                            )
                        ):
                    return False
            return True
        return False

    def vertices_equal(self, first_graph, second_graph):
        return (self.number_vertices_equal(first_graph, second_graph)
                and self.vertex_sequence_attributes_equal(first_graph, second_graph) 
                and self.vertex_attributes_equal(first_graph, second_graph)
                )

    def number_vertices_equal(self, first_graph, second_graph):
        return len(first_graph.vs) == len(second_graph.vs)

    def vertex_sequence_attributes_equal(self, first_graph, second_graph):
        return self.sequence_attributes_equal(
            first_graph.vs, second_graph.vs
            )

    def vertex_attributes_equal(self, first_graph, second_graph):
        return self.sequence_value_attributes_equal(
            first_graph.vs, second_graph.vs
            )

    def attributes_equal(self, first_graph, second_graph):
        return first_graph.attributes() == second_graph.attributes()
