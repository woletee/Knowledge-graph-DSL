from matplotlib import colors    ### 까만 노드 인력척력 djqt는 버전 + grid_to_graph_woblack 함수 추가 + 1.414 주석처리 + np array 로 변경
import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.cluster import DBSCAN # conda install -c conda scikit-learn
import pandas as pd # conda install pandas

cmap = colors.ListedColormap(
        [
            '#000000', # 0 검은색
            '#0074D9', # 1 파란색
            '#FF4136', # 2 빨간색
            '#2ECC40', # 3 초록색
            '#FFDC00', # 4 노란색
            '#AAAAAA', # 5 회색
            '#F012BE', # 6 핑크색
            '#FF851B', # 7 주황색
            '#7FDBFF', # 8 하늘색
            '#870C25', # 9 적갈색
            '#505050', # 10 검은색_select
            '#30A4F9', # 11 파란색_select
            #'#FF4136', 
            '#FF7166', # 12 빨간색_select
            '#5EFC70', # 13 초록색_select
            '#FFFC30', # 14 노란색_select
            '#DADADA', # 15 회색_select
            '#F042EE', # 16 핑크색_select
            '#FFB54B', # 17 주황색_select
            '#AFFBFF', # 18 하늘색_select
            '#B73C55'  # 19 적갈색_select
        ])
    #norm = colors.Normalize(vmin=0, vmax=9)
norm = colors.Normalize(vmin=0, vmax=19)
def get_color(color) : ## not a DSL
    if color == 0:
        color = '#000000', # 0 검은색
    if color == 1:
        color = '#0074D9', # 1 파란색
    if color == 2:
        color = '#FF4136', # 2 빨간색
    if color == 3:
        color = '#2ECC40', # 3 초록색
    if color == 4:
        color = '#FFDC00', # 4 노란색
    if color == 5:
        color = '#AAAAAA', # 5 회색
    if color == 6:
        color = '#F012BE', # 6 핑크색
    if color == 7:
        color = '#FF851B', # 7 주황색
    if color == 8:
        color = '#7FDBFF', # 8 하늘색
    if color == 9:
        color = '#870C25', # 9 적갈색
    return color  

class Pnode :
    def __init__(self, grid, i, j):
        self.color = grid[i][j]
        self.number = self.node_number(len(grid[0]), i, j)
        self.visual_coord = [3 * j, 3 * (len(grid) - i - 1)]  ## coordinate for visualize
        self.coordinate = [j,i]         ## coordinate from the grid
    def node_number (self, col, i, j): ## start from 0 to (col * row -1) # may not needed
        temp = i * (col) + j
        return temp
    def __str__(self):
        return f"Pnode : {self.color, self.coordinate}"

class Onode:
    def __init__(self, obj):
        Pnode_list = []
        color_set = set()
        for Pnode in obj:
            Pnode_list.append(Pnode)
            color_set.add(Pnode.color)
        self.Pnode_list = Pnode_list
        self.color = color_set            ##questionalbe   
        self.coordinate = [0,0]                          ##questionalbe -> need bbox function first and type will be {(int, int), (int, int) ...}
    def __str__(self):
        pnodes = []
        for pnode in self.Pnode_list:
            pnodes.append(pnode.__str__())
        return f"Onode : {self.color, pnodes}"
    
class Gnode:
    def __init__(self, node_list): # node_list should contain all the Pnode and Onode from the grid
        self.Node_list = node_list
        color_s = set()
        for n in node_list:
            if isinstance(n, Pnode):
                color_s.add(n.color)
        self.color = color_s
        self.coordinate = [0,0]         ## questionable # do we need coornidate for Gnode?
    def __str__(self):
        return f"Gnode : {self.color, self.Node_list}"

class Vnode:
    def __init__(self, Gnode1, Gnode2): # node_list should contain all the Pnode and Onode from the grid
        self.Node_list = [Gnode1, Gnode2]
    def __str__(self):
        return f"Vnode : {self.Node_list}"

    
class Edge:
    def __init__(self, tag, node1, node2 = None):
        if node2 == None :
            self.node_set = {node1}
        else :
            self.node_set = {node1, node2}
        self.tag = tag       
    def __str__(self):
        n_set = []
        for n in self.node_set:
            n_set.append(n.__str__())
        return f"{n_set, self.tag}"    

def Grid_to_Img(grid): ## function for visualize the image, this function is not a DSL
    plt.axis("off")
    plt.imshow(grid, cmap = cmap, norm = norm)

def Make_NodeList (grid):     ## this function now generate Pnode list from grid
    node_list = []
    if type(grid[0]) == list :
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp_node = Pnode(grid, i, j)
                temp_node.color = grid[i][j]
                node_list.append(temp_node)
    # else :
    #     for sub_g in grid:
    #         node_list.append(Onode(sub_g))
    return node_list

def Concat_node_list (node_list1, node_list2):
    return node_list1 + node_list2

def Make_Onode (node_list, color_same, dist_dsl, edge_list):

    def edge_list_to_graph(edges):
        graph = {}
        for edge in edges:
            node1, node2 = edge.node_set
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)
        return graph
    
    if color_same == True:
        same_color, _ = get_to_is(get_color)
    else :
        same_color = lambda x1, x2 : True
        
    dist_1, _ = get_to_is(dist_dsl, 1)
    same_color_and_dist1 = lambda x1, x2: True if (same_color(x1,x2) == True and dist_1(x1,x2) == True) else False
    s_d_edge_list, _ = Make_edge_list(node_list, same_color_and_dist1)
    graph = edge_list_to_graph(s_d_edge_list)

    for node in node_list:
        if node not in graph.keys():
            graph[node] = []
    
    def cluster_graph(graph):
        clusters = []
        visited = set()

        def dfs(node, cluster):
            visited.add(node)
            cluster.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, cluster)

        for node in graph:
            if node not in visited:
                new_cluster = set()
                dfs(node, new_cluster)
                clusters.append(new_cluster)
                
        return clusters

    clusters = cluster_graph(graph)

    Onode_list = []
    tag = "get_onode"
    for obj in clusters:
        onode = Onode(obj)
        Onode_list.append(onode)
        for pnode in obj:
            e = Edge(tag, pnode, onode)
            edge_list.append(e)



    return node_list + Onode_list, edge_list 

def Make_Gnode (node_list, edge_list):
    gnode = Gnode(node_list)
    gnode_list = []
    tag = "get_gnode"
    for node in node_list:
        e = Edge(tag, gnode, node)
        edge_list.append(e)
    gnode_list.append(gnode)
    return node_list + gnode_list, edge_list

def Make_Vnode (node_list, edge_list):
    gnode_list = []
    for n in node_list:
        if isinstance(n, Gnode):
            gnode_list.append(n)
    assert len(gnode_list) == 2
    vnode = [Vnode(gnode_list[0], gnode_list[1])]
    tag = "get_vnode"
    e1 = Edge(tag, vnode[0], gnode_list[0])
    e2 = Edge(tag, vnode[0], gnode_list[1])
    edge_list.append(e1)
    edge_list.append(e2)
    return node_list + vnode, edge_list

def create_edge_list ():
    return []

def create_edge (get_dsl, node1, node2 = None, target = None): ## version 1 : edge_type is get_dsl
    is_dsl, tag = get_to_is(get_dsl, target)
    if node2 != None and target == None: ## node1, node2, no target
        if is_dsl(node1,node2) == True :
            edge = Edge(tag, node1, node2)
            return edge
    elif node2 != None and target != None: ## node1, node2, target
        if is_dsl(node1, node2) == target :
            edge = Edge(tag, node1, node2)
            return edge
    elif node2 == None and target != None: ## node1, target, 지금 get_to_is 함수의 출력으로는 불가능한 형태
        if is_dsl(node1, node2) == target :
            edge = Edge(tag, node1, node2)
            return edge
    elif node2 == None and target == None: ## is there any this templete get_dsl?
        if is_dsl(node1) == True :
            edge = Edge(tag, node1)
            return edge
    else:
        return
    
def Make_edge_list (node_list, dsl, target = None) :
    edge_list = create_edge_list()
    try :
        if isinstance (dsl(node_list[0]), bool) == True: ## dsl is is_dsl with only one param
            print("dsl is returning bool type with 1 param")
            tag = dsl.__name__
            for n1 in node_list:
                if dsl(n1) == True :
                    e = Edge(tag, n1)
                    edge_list.append(e)
            return edge_list, tag
        else :
            pass
    except :
        pass
    try :
        if isinstance (dsl(node_list[0], node_list[0]), bool) == True : ## dsl is is_dsl with two param
            print("dsl is returning bool type with 2 param")
            tag = dsl.__name__
            for n1 in node_list:
                for n2 in node_list:
                    if dsl(n1, n2) == True and n1 != n2 :
                        e = Edge(tag, n1, n2)
                        edge_list.append(e)
            return edge_list, tag
    except: 
        pass
    ## dsl is get_dsl
    print("dsl is get_dsl")
    for n1 in node_list:
        for n2 in node_list:
            e = create_edge(dsl, n1, n2, target)
            if e != None and n1 != n2:
                edge_list.append(e)
    return edge_list, edge_list[-1].tag

def Concat_edge_list (edge_list1, edge_list2):
    return edge_list1 + edge_list2

def get_to_is (get_f, target = None): ## is_square 같은 함수는 get 함수와의 관계를 정의하기가 어렵다
    param_num = get_f.__code__.co_argcount
    tag = get_f.__name__
    if param_num == 1:
        if target == None :
            is_dsl = lambda x1, x2: True if get_f(x1) == get_f(x2) else False
            tag = (tag, None)    ## questionalbe -> to make tag consistant, we need None as secound ele of tuple
        else :
            print("we have an excpetion here: get_DSl takes only one param but has non-None target value")
    elif param_num == 2:
        if target != None:
            is_dsl = lambda x1, x2: True if get_f(x1, x2) == target else False
            tag = (tag, target)
        else :
            print("we have an excpetion here: get_DSl takes two params but has None target value")
    return is_dsl, tag

def visualize(node_list, edge_list, tag):
    x = []
    y = []
    colors = []
    num_nodes = len(node_list)
    for ele in (node_list):
        x.append(ele.visual_coord[0])
        y.append(ele.visual_coord[1])
        colors.append(ele.color)
    for i in range(len(node_list)):
        plt.text(x[i] - 0.1, y[i]- 0.1, node_list[i].number , size = 15, color = 'white')

    for i in range(num_nodes) :
        for j in range(i, num_nodes) :
            for edge in edge_list:
                if edge.node_set == {node_list[i], node_list[j]} and edge.tag == tag:
                    plt.plot([x[i], x[j]], [y[i], y[j]], color = 'black', linewidth = 3)
    plt.axis('off')
    plt.axis('equal')
    plt.scatter(x, y, s = 500, c = colors, cmap = cmap, norm = norm)
    plt.show()


def get_manhattan_dist (node1,node2) : 
    x = abs(node1.coordinate[0] - node2.coordinate[0])
    y = abs(node1.coordinate[1] - node2.coordinate[1])
    dist = x + y
    return dist
    
def get_polar_dist (node1, node2) :
    x = abs(node1.coordinate[0] - node2.coordinate[0])
    y = abs(node1.coordinate[1] - node2.coordinate[1])
    return x if x > y else y

def get_color (node) :
    return node.color 
