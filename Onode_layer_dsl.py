#O-node Layer DSLs 
def get_onode_color(onode):
    return onode.color  # returns the set of colors the Onode contains 
def get_onode_width(onode):
    x_coords = [pnode.coordinate[0] for pnode in onode.Pnode_list]
    if x_coords:  
        width = max(x_coords) - min(x_coords)
    else:
        width = 0  # No width if there are no nodes
    return width
def get_onode_height(onode):
    y_coords = [pnode.coordinate[1] for pnode in onode.Pnode_list]
    if y_coords:  
        height = max(y_coords) - min(y_coords)
    else:
        height = 0  # No height if there are no nodes
    return height
def get_Onode_dimension(onode):
    width = get_onode_width(onode)
    height = get_onode_height(onode)
    return (width, height)
def get_width_diff(onode1, onode2):
  width1 = get_onode_width(onode1)
  width2 = get_onode_width(onode2)
  return abs(width1 - width2)
def get_height_diff(onode1, onode2):
  height1 = get_onode_height(onode1)
  height2 = get_onode_height(onode2)
  return abs(height1 - height2)
def get_dimension_diff(onode1, onode2):
    # Get dimensions of both Onodes
    dimensions1 = get_Onode_dimension(onode1)
    dimensions2 = get_Onode_dimension(onode2)
    # Calculate differences in width and height
    width_diff = abs(dimensions1[0] - dimensions2[0])
    height_diff = abs(dimensions1[1] - dimensions2[1])
    return (width_diff, height_diff)
def get_color_difference_set(onode1, onode2):
    colors1 = onode1.color
    colors2 = onode2.color
    color_diff = (colors1 - colors2).union(colors2 - colors1)
    return color_diff
def get_component(onode):
    return onode.Pnode_list
##def get_bounding_box(Pnode_list, Onode)
