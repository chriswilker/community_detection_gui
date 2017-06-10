Introduction
============

* Enables straightforward community detection using a GUI.
* Uses the [louvain package](https://github.com/vtraag/louvain-igraph) to determine communities.

Prerequisites
=============

* [Python 2.7.13](https://www.python.org/downloads/) - later Python 2.7 versions will likely also work, but this is the last Python version tested.
* [python-igraph](http://igraph.org/python/)
* [Pycairo](https://www.cairographics.org/pycairo/)
* [louvain](https://github.com/vtraag/louvain-igraph)

Using the GUI
=============

* Clone or download the community_detection_gui repository into a directory on your Python 2.7 path.
* Make sure that the top-level directory is named "community_detection_gui". If the name is different, the package won't work.
* Open the GUI by running the file open_gui.py in the top-level directory using Python 2.7.

Important Information
=====================
* If attempting to save a plot, the file extension may need to be manually specified on certain operating systems (such as Windows). For example, when saving a plot, save it as "plot.png" instead of as "plot", even if the type "PNG (\*.png)" is already selected in the file browser. Otherwise the file might not be saved.

More Details
============
* Plots are loaded using the igraph load method, which attempts to automatically detect the graph type based on the file extension. Some working file types are .paj, .pickle, .gml, .graphml, and .graphmlz. Information about supported file types available on the [igraph and the outside world](http://igraph.org/python/doc/tutorial/tutorial.html#igraph-and-the-outside-world) section of the igraph tutorial.
* Plots can be saved as .png, .svg, .pdf, or .ps image files. 
* Information about the plot layout algorithms listed in the "Plot Graph" window may be found on the [layouts and plotting](http://igraph.org/python/doc/tutorial/tutorial.html#layouts-and-plotting) section of the igraph tutorial.
* Information about the vertex attributes determined in the "Plot Graph" window may be found on the [vertex attributes](http://igraph.org/python/doc/tutorial/tutorial.html#vertex-attributes-controlling-graph-plots) and [edge attributes](http://igraph.org/python/doc/tutorial/tutorial.html#edge-attributes-controlling-graph-plots) sections of the igraph tutorial.
* Information about community detection methods can be found on the [louvain github](https://github.com/vtraag/louvain-igraph).
* If you don't have a graph file available but you still want to try out the program, load one of the pickle files in the tests/test_files folder. These files represent very simple graphs. The unsigned file has no "sign" attribute and cannot be used for signed community detection.
