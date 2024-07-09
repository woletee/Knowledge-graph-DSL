def get_pattern(node_list):
    pattern = []
    for node in node_list:
        pattern.append((node.coordinate, node.color))
    return pattern

def match_pattern(node_list, pattern):
    for (coord, color) in pattern:
        for node in node_list:
            if node.coordinate == coord and node.color != color:
                return False
    return True

def transform_pattern(node_list, transformation):
    for node in node_list:
        node.color = transformation(node.color)
    return node_list
