import igraph.drawing.colors as colors

class VertexColorer():
    def vertex_colors(self, membership):
        self.membership = membership

        self.determine_group_colors()
        return self.vertex_colors_from_group_colors()

    def determine_group_colors(self):
        group_colors_palette = colors.ClusterColoringPalette(
            max(self.membership) + 1
            )

        self.group_colors = []
        for rgbw_tuple in group_colors_palette:
            self.group_colors.append(rgbw_tuple)


    def vertex_colors_from_group_colors(self):
        return [self.group_colors[group] for group in self.membership]
