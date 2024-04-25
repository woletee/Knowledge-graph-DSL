G-node layer DSLs
def get_dominant_color(node_list):
    color_counts = {}
    for node in node_list: color_counts[node.color] = color_counts.get(node.color, 0) + 1
    return max(color_counts, key=color_counts.get)  
def get_background_color_removed(node_list):
    dominant_color = get_dominant_color(node_list)  # Use existing function to find dominant color
    return [node for node in node_list if node.color != dominant_color]  # Filter out nodes with the dominant color
def get_least_common_color(node_list):
    color_counts = {}
    for node in node_list:
        color = get_color_of_node(node)  # Fetch the color using the provided helper function
        color_counts[color] = color_counts.get(color, 0) + 1
    min_count = min(color_counts.values())
    return [color for color, count in color_counts.items() if count == min_count]
def get_width(node_list):
    "DSL for getting the width of a node-list"
    width = max(node.coordinate[0] for node in node_list) + 1
    return width
def get_height(node_list):
    "DSL for getting the height of a node-list"
    height = max(node.coordinate[1] for node in node_list) + 1
    return height
def get_dimension(node_list):
    # Get both the width and height of the grid from the node_list
    width = get_width(node_list)
    height = get_height(node_list)
    return (width, height)
def get_number_of_nodes(node_list):    #this is equivalent with getting the size of the node_list 
    # Returns the number of nodes in the node_list
    return len(node_list)
def get_center_nodes(node_list):
    width, height = get_width(node_list), get_height(node_list)
    center_x, center_y = width // 2, height // 2
    return [node for node in node_list if node.coordinate == [center_x, center_y]]
def get_margin(node_list):
    margin_nodes = []
    for node in node_list:
        x, y = get_coordinate(node)
        if x == 0 or y == 0 or x == get_width(node_list) - 1 or y == get_height(node_list) - 1:
            margin_nodes.append(node)
    return margin_nodes
def get_non_margin(node_list):
    return [node for node in node_list if node not in get_margin(node_list)]
def get_corner(node_list):
    return [node for node in node_list if all(get_coordinate(node)[i] in {0, size - 1} 
    for i, size in zip([0, 1], (get_width(node_list), get_height(node_list))))]
def get_specific(node_list, target_colors):
    return [node for node in node_list if node.color in target_colors]
  #returns list of nodes that are neighbour to the specific nod
def get_height_difference(node_list1, node_list2):   #returns the height difference of two grids
    height1 = get_height(node_list1)
    height2 = get_height(node_list2)
    return abs(height1 - height2)
def get_width_difference(node_list1, node_list2):  #returns the width difference of two grids
    width1 = get_width(node_list1)
    width2 = get_width(node_list2)
    return abs(width1 - width2)
def get_max_height(node_list1, node_list2):
    return max(get_height(node_list1), get_height(node_list2))    #max height of two grids 
def get_max_width(node_list1, node_list2):
    return max(get_width(node_list1), get_width(node_list2))   #max width of two grids
