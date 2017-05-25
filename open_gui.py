import community_detection_gui.src.path_helper as path_helper
import community_detection_gui.src.graph_loader as graph_loader
import community_detection_gui.src.graph_file_opener as graph_file_opener

helper = path_helper.PathHelper()
loader = graph_loader.GraphLoader(helper)
file_loader = graph_file_opener.GraphFileOpener(loader)
file_loader.load_graph()
