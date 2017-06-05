Introduction
============

* Enables straightforward community detection using a GUI.
* Uses the [louvain package](https://github.com/vtraag/louvain-igraph) to determine communities.

Prerequisites
=============

* [Python 2.7.13](https://www.python.org/downloads/) - later Python 2.7 versions will likely also work, but this is the last Python version tested.
* [python-igraph](http://igraph.org/python/)
* [Pycairo](http://igraph.org/python/doc/tutorial/install.html#installing-igraph)
* [louvain](https://github.com/vtraag/louvain-igraph)

Using the GUI
=============

* Open the GUI by running the file open_gui.py in the top-level folder using Python 2.7.

Notes
=====
* Plots are loaded using the igraph load method, which attempts to automatically detect the graph type based on the file extension. Some working file types are .paj, .pickle, .gml, .graphml, and .graphmlz. Information about supported file types available on the ["igraph and the outside world"](http://igraph.org/python/doc/tutorial/tutorial.html#igraph-and-the-outside-world) section of the igraph tutorial.
* Plots can be saved as .png, .svg, .pdf, or .ps image files. 
* If attempting to save a plot, the file extension may need to be manually specified on certain operating systems. For example, when saving a plot, save it as "plot.png" instead of as "plot", even if the type "PNG (\*.png)" is already selected in the file browser.
* Information about the plot layout algorithms listed in the "Plot Graph" window may be found on the ["layouts and plotting"](http://igraph.org/python/doc/tutorial/tutorial.html#layouts-and-plotting) section of the igraph tutorial.
* Information about community detection methods can be found on the [louvain github](https://github.com/vtraag/louvain-igraph).
