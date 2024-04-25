# Knowledge Graph Construction for ARC Tasks

This repository contains Python code for constructing knowledge graphs from ARC (Abstraction and Reasoning Corpus) task grids. The project utilizes graph-based data structures to analyze and visualize relationships within ARC tasks, facilitating a deeper understanding of spatial and relational patterns.

## Features

- **Node Representation**: Utilize `Pnode`, `Onode`, `Gnode`, and `Vnode` classes to represent different layers of abstraction within ARC tasks.
- **Graph Construction**: Build and manipulate graph structures from task data.
- **Visualization**: Dynamically visualize knowledge graphs with color-coded nodes and edges.

# DSL structure 

This repository is dedicated to constructing and analyzing knowledge graphs from the Abstraction and Reasoning Corpus (ARC) tasks using a suite of domain-specific language (DSL) tools. These tools are organized across three primary layers of operation: **P-layer**, **Onode layer**, and **Gnode layer**, each offering unique functionalities tailored to different aspects of knowledge graph manipulation and analysis. Currently DSLs basically focus on the **grid Size** and **Color!**

### P-layer DSLs
The **P-layer** operates at the most granular level, dealing directly with individual nodes (Pnodes). This layer includes functions for basic node properties and metrics, such as:
- `get_color_of_node`: Fetch the color attribute of a node.
- `get_neighbours`: Determine adjacent nodes based on grid position.
- `get_manhattan_dist`, `get_polar_distance`: Calculate distances between nodes to support spatial reasoning.

### Onode Layer DSLs
The **Onode layer** abstracts collections of Pnodes into higher-level objects (Onodes), facilitating operations on node clusters:
- `get_onode_color`: Retrieve the collective color set of an Onode.
- `get_onode_width`, `get_onode_height`: Compute dimensions of node clusters.
- `get_Onode_dimension`: Fetch comprehensive dimensional data of Onodes.

### Gnode Layer DSLs
The **Gnode layer** encompasses higher-order structures and offers tools for global graph properties and operations:
- `get_dominant_color`: Identify the most frequent color in a node collection.
- `get_width`, `get_height`: Determine the overall dimensions of graph structures.
- `get_number_of_nodes`: Count nodes within a given structure for scaling analyses.

## Dependencies
Ensure you have the following Python packages installed:

- **matplotlib**:
- **numpy**:
- **scikit-learn**:
- **pandas**:

## Contributing

- **Contributions are welcome! Please fork the project, make your changes, and submit a pull request**:
