import community_detection_gui.src.path_helper as path_helper
import community_detection_gui.src.graph_loader as graph_loader
import community_detection_gui.src.graph_file_opener as graph_file_opener

import community_detection_gui.src.graph_splitter as graph_splitter
import community_detection_gui.src.community_finder as community_finder
import community_detection_gui.src.community_gui as community_gui

PathHelper = path_helper.PathHelper()
GraphLoader = graph_loader.GraphLoader(PathHelper)

GraphSplitter = graph_splitter.GraphSplitter()
CommunityFinder = community_finder.CommunityFinder(GraphSplitter)
CommunityGUI = community_gui.CommunityGUI(CommunityFinder)

GraphFileOpener = graph_file_opener.GraphFileOpener(GraphLoader, CommunityGUI)
GraphFileOpener.load_graph()
