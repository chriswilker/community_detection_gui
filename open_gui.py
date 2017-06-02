import community_detection_gui.src.path_helper as path_helper
import community_detection_gui.src.graph_loader as graph_loader

import community_detection_gui.src.graph_splitter as graph_splitter
import community_detection_gui.src.community_finder as community_finder

import community_detection_gui.src.vertex_colorer as vertex_colorer
import community_detection_gui.src.edge_colorer as edge_colorer
import community_detection_gui.src.graph_plotter as graph_plotter
import community_detection_gui.src.plot_gui as plot_gui

import community_detection_gui.src.community_gui as community_gui

import community_detection_gui.src.graph_file_opener as graph_file_opener

PathHelper = path_helper.PathHelper()
GraphLoader = graph_loader.GraphLoader(PathHelper)

GraphSplitter = graph_splitter.GraphSplitter()
CommunityFinder = community_finder.CommunityFinder(GraphSplitter)

VertexColorer = vertex_colorer.VertexColorer()
EdgeColorer = edge_colorer.EdgeColorer()
GraphPlotter = graph_plotter.GraphPlotter(VertexColorer, EdgeColorer)
PlotGUI = plot_gui.PlotGUI(GraphPlotter)

CommunityGUI = community_gui.CommunityGUI(CommunityFinder, PlotGUI)

GraphFileOpener = graph_file_opener.GraphFileOpener(GraphLoader, CommunityGUI)

GraphFileOpener.load_graph()
