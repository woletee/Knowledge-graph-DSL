#I didnot addd modifications to this extractor function 
def extractor(KG, adj, target_xnode):
    node_info = {}
    node_info["type"] = target_xnode.type
    node_info["properties"] = set()

    if isinstance(target_xnode, Gnode):
        node_info["definition"] = "Gnode"
        return node_info
    else :
        node_info["definition"] = target_xnode.condition

    # edge_list = KG[1]
    edge_dict = {}
    # print("node type : ", type(target_xnode))

    # print("preparing edge list... ")
    # result, _ = print_adj(KG)
    index = KG[0].index(target_xnode)
    for i, n in enumerate(KG[0]):
        if n.output == 1:
            break
    index2 = i
    for edge in adj[index:index2]:
        if edge[0] == 0:
            continue
        # print(edge[1])
        for tag in edge[1:]:
            # print("tag : ", tag)
            edge_dict[tag[0]] = edge[0]
    # print("\rfinish edge list")

    max_size = 0
    min_size = 900
    unique = 1
    for node in KG[0]:
        if node.type == "Onode" and node.condition == target_xnode.condition and node.input == 1:
            if node.color == target_xnode.color and node != target_xnode:
                unique = 0
            max_size = max(max_size, get_number_of_nodes(node))
            min_size = min(max_size, get_number_of_nodes(node))
    if max_size <= get_number_of_nodes(target_xnode):
        node_info["properties"].add("max_size")
    if min_size >= get_number_of_nodes(target_xnode):
        node_info["properties"].add("min_size")
    if unique == 1:
        node_info["properties"].add("unique_color")

    if "is_ring" in edge_dict.keys():
        node_info["properties"].add("ring_shape")
    if "is_rectangle" in edge_dict.keys():
        node_info["properties"].add("rectangle_shape")
    if "is_square" in edge_dict.keys():
        node_info["properties"].add("square_shape")
    if "is_symmetric" in edge_dict.keys():
        node_info["properties"].add("symmetric")

    node_info["edge_list"] = edge_dict
    return node_info

