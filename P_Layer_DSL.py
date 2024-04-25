#P-layer DSLs 
def get_color_of_node(node):
    return node.color
def get_vertical_groups(node1, node2):
    # Check if both nodes are on the same vertical line
    return node1.coordinate[0] == node2.coordinate[0]  
def get_neighbours(node, node_list):
    row, col = node.coordinate
    neighbours = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    return [n for n in node_list if n.coordinate in neighbours] 
def get_polar_distance(node1, node2):  
    x1, y1 = node1.coordinate
    x2, y2 = node2.coordinate
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return int(round(distance))
def get_manhattan_dist (node1,node2) :     #Visualized 
    x = abs(node1.coordinate[0] - node2.coordinate[0])
    y = abs(node1.coordinate[1] - node2.coordinate[1])
    dist = x + y
    return dist
def get_horizontal_groups(node1, node2):
    # Check if both nodes are on the same horizontal line
    return node1.coordinate[1] == node2.coordinate[1]
def get_coordinate(node):
    return node.coordinate
 
