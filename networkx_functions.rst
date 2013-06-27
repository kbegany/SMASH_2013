============================
Available Networkx Functions
============================


---------------
Basic Functions
---------------

average_shortest_path_length(G)::

  Returns the average shortest path length.

average_clustering(G)::

  Compute the average clustering coefficient for the graph G.
  For unweighted graphs the clustering coefficient of each node  is
  the fraction of possible triangles that exist.

clustering(G)::

  Computes the clustering coefficient for nodes.
  For unweighted graphs the clustering coefficient of each node  is the fraction
  of possible triangles that exist.

degree(G)::

  Returns the degree of a single node or of a nbunch of nodes.  If
  nbunch is ommitted, then returns the degrees of all nodes.

degree_histogram(G)::

  Returns a list of the frequency (i.e. number of occurances) of each
  degree value.  The degree values are the index in the list.

density(G)::

  Returns the density of a graph.


------------------
Advanced Functions
------------------

betweenness_centrality(G)::

  Compute the shortest-path betweenness centrality for nodes.
  Betweenness centrality of a node  is the sum of the fraction of
  all-pairs shortest paths that pass through :

closeness_centrality(G)::

  Computes the closeness centrality for nodes.
  Closeness centrality at a node is 1/average distance to all other
  nodes.

degree_assortativity(G)::

  Computes the degree assortativity of graph.
  Assortativity measures the similarity of connections in the graph
  with respect to the node degree.


degree_centrality(G)::

  Computes the degree centrality for nodes.
  The degree centrality for a node v is the fraction of nodes it is
  connected to.

transitivity(G)::

  Computes the graph transitivity, the fraction of all possible triangles
  present in G.
  Possible triangles are identified by the number of “triads” (two
  edges with a shared vertex).



