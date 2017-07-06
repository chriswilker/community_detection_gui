import csv

class CommunityCSVGenerator():
    def generate_community_csv(self, csv_file_path, graph, membership_list):
        self.graph = graph
        self.membership_list = membership_list

        row_list = self.row_list(
            self.node_label_column(), self.node_community_column(),
            self.node_community_size_column()
            )

        self.create_csv_file(row_list, csv_file_path)

    def node_label_column(self):
        node_labels = ['node']
        for vertex in self.graph.vs:
            node_labels.append(vertex['label'])
        return node_labels

    def node_community_column(self):
        node_community_column = ['community']
        for i in self.membership_list:
            node_community_column.append(i)
        return node_community_column

    def node_community_size_column(self):
        community_sizes = []
        community_values = range(max(self.membership_list) + 1)
        for i in community_values:
            number_nodes_in_community = 0
            for j in self.membership_list:
                if (i == j):
                    number_nodes_in_community += 1
            community_sizes.append(number_nodes_in_community)

        node_community_size_column = ['community_size']
        for i in self.membership_list:
            node_community_size_column.append(community_sizes[i])
        return node_community_size_column

    def row_list(self, *columns):
        row_list = []
        row_indexes = range(len(columns[0]))
        for i in row_indexes:
            column_value_list = []
            for j in columns:
                column_value_list.append(j[i])
            row_list.append(column_value_list)
        return row_list

    def create_csv_file(self, row_list, csv_file_path):
        with open(csv_file_path, 'wb') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)
