class GraphComparer():
    def graphs_equal(first_graph, second_graph):
        return (graph_edges_equal(first_graph, second_graph)
            and graph_attributes_equal(first_graph, second_graph)
            and (len(first_graph.vs) == len(second_graph.vs)))

    def graph_edges_equal(first_graph, second_graph):
        edges_are_equal = False
        if (len(first_graph.es) == len(second_graph.es)):
            edges_are_equal = (
                first_graph.edge_list() == second_graph.edge_list())
        return edges_are_equal

    def graph_attributes_equal(first_graph, second_graph):
        for i, first_graph_edge in enumerate(first_graph.es):
            if (first_graph_edge.attributes() != second_graph.es[i].attributes()):
                return False
        for i, first_graph_vertex in enumerate(first_graph.vs):
            if (first_graph_vertex.attributes() != second_graph.vs[i].attributes()):
                return False
        if (first_graph.es.attributes() != second_graph.es.attributes()):
            return False
        elif (first_graph.vs.attributes() != second_graph.vs.attributes()):
            return False
        elif (first_graph.attributes() != second_graph.attributes()):
            return False
        return True
