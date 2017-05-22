import community_detection_gui.src.load_graph_gui as load_graph_gui
import community_detection_gui.src.graph_loader as graph_loader

import igraph

loader = graph_loader.GraphLoader(igraph.Graph)
load_graph_gui.load_graph_gui(loader)
