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
* [tqdm](https://pypi.python.org/pypi/tqdm#latest-pypi-stable-release)

Using the GUI
=============

* Open the GUI by running the file gui.py in the src folder using Python 2.7.

CSV file formatting if loading graph from CSV
=============================================

* The .csv file should have data labels in the first row.
* Two labels must exist: 'starting node', and 'ending node'.
* Other labels will be used to create to key-value pairs for edges, for example 'weight' will assign a value to the 'weight' attribute for an edge.
* One important label is 'sign': this label must be present to create signed graphs.
* The second row and below should contain data, if it exists, for individual edges.
* See the example_graph.csv file in lib/examples/csv for a simple example of a csv file representing a signed graph
