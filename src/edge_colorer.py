import igraph.drawing.colors as colors

class EdgeColorer():
    def edge_colors(self, graph):
        self.graph = graph
        
        self.determine_sign_colors()
        self.determine_edge_sign_membership()
        return self.edge_colors_from_signs()

    def determine_sign_colors(self):
        sign_colors_palette = colors.ClusterColoringPalette(2)

        self.sign_colors = []
        for rgbw_tuple in sign_colors_palette:
            self.sign_colors.append(rgbw_tuple)

    def determine_edge_sign_membership(self):
        self.edge_sign_membership = []
        for edge in self.graph.es:
            edge_sign = int(edge['sign'])
            if edge_sign == -1:
                self.edge_sign_membership.append(0)
            elif edge_sign == 1:
                self.edge_sign_membership.append(1)

    def edge_colors_from_signs(self):
        return [
            self.sign_colors[sign_group] for sign_group in self.edge_sign_membership
            ]
