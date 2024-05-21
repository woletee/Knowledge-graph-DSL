import copy
get_int = [xnode_h, xnode_w, number_of_colorsett, node_size, onode_count1, onode_count2, onode_count3, onode_count4]
def number_of_colorsett(Xnode):
    if isinstance(Xnode, Pnode) or isinstance(Xnode, Vnode):
        return None
    return set(Xnode.color)  # Returning the set of colors instead of its length

def identity_transformation(value, target):  #adding some value t
    if value == target:
        temp = lambda x: number_of_colorsett(x)
        tag = (number_of_colorsett.__name__, 'identity')
        return (temp, tag)
    return None

def multiplicative_transformation(value, target):
    if target % value == 0:
        factor = target // value
        temp = lambda x, f=factor: number_of_colorsett(x) * f
        tag = (number_of_colorsett.__name__, 'multiplicative', factor)
        return (temp, tag)
    return None

def additive_transformation(value, target):
    difference = target - value
    temp = lambda x, d=difference: number_of_colorsett(x) + d
    tag = (number_of_colorsett.__name__, 'additive', difference)
    return (temp, tag)

###used another solver function called color_solver_function for the color set predictor 
#this color_solver_function make use of the functions defined above to determine the transformations(relationships) between the target and the predicted 

def color_solver_function(Xnode, target_set):
    """Create solvers that match the color set of Xnode to the target set."""
    solver = set()
    colors = number_of_colorsett(Xnode)
    if colors is None:
        return solver
    least_common_color = get_least_common_color(Xnode)
    if get_least_common_color(Xnode) in target_set:
      temp = lambda x: set([0]).union([get_least_common_color(x)])
      tag = ("least common" 'superset match')
      solver.add((temp, tag))

    if colors.issubset(target_set):
      temp = lambda x: number_of_colorsett(x).union(colors - target_set)
      tag = (number_of_colorsett.__name__, 'subset match')
      solver.add((temp, tag))
    if colors.issuperset(target_set):
      temp = lambda x: set([get_dominant_color(x)])
      tag = (number_of_colorsett.__name__, 'dominiant ')
      solver.add((temp, tag))
    if colors.issuperset(target_set):
      temp = lambda x: number_of_colorsett(x) - set([get_dominant_color(x)])
      tag = (number_of_colorsett.__name__, 'superset match')
      solver.add((temp, tag))
    if colors != target_set:
       temp = lambda x: target_set
       tag = (number_of_colorsett.__name__, 'transformed')
       solver.add((temp, tag))
    if colors == target_set:
        temp = lambda x: number_of_colorsett(x)
        tag = (number_of_colorsett.__name__, 'exact match')
        solver.add((temp, tag))
    if colors.issuperset( target_set):
        temp = lambda x: colors
        tag = (number_of_colorsett.__name__, 'exact match')
        solver.add((temp, tag))
    
    # Checking if the colors are a subset of the target set

    return solver
#No modifications done for this Solver_function
def solver_function(Xnode, target):
    solver = set()
    
    v1 = xnode_h(Xnode)
    if not isinstance(v1, int):
        pass
    else :
        answer1 = linear(v1, target)
        if answer1 != None:
            # temp1 = lambda x: ((xnode_h(x) * answer1[0] + answer1[1] if not xnode_h(x) == None else 0) , print ("lambda : ",temp1  ,"candi(x) :",xnode_h(x),"candi: ", xnode_h.__name__, "answer[0] :", answer1[0], "answer[1] ", answer1[1]))
            temp1 = lambda x: ((xnode_h(x) * answer1[0] + answer1[1] if not xnode_h(x) == None else 0))
            tag1 = (xnode_h.__name__, answer1[0], answer1[1])
            solver.add((temp1,tag1))

    v2 = xnode_w(Xnode)
    if not isinstance(v2, int):
        pass
    else :
        answer2 = linear(v2, target)
        if answer2 != None:
            # temp2 = lambda x: ((xnode_w(x) * answer2[0] + answer2[1] if not xnode_w(x) == None else 0) , print ("lambda : ",temp2  ,"candi(x) :",xnode_w(x),"candi: ", xnode_w.__name__, "answer[0] :", answer2[0], "answer[1] ", answer2[1]))
            temp2 = lambda x: ((xnode_w(x) * answer2[0] + answer2[1] if not xnode_w(x) == None else 0))
            tag2 = (xnode_w.__name__, answer2[0], answer2[1])
            solver.add((temp2,tag2))

    v3 = number_of_colorset(Xnode)
    if not isinstance(v3, int):
        pass
    else :
        answer3 = linear(v3, target)
        if answer3 != None:
            # temp3 = lambda x: ((number_of_colorset(x) * answer3[0] + answer3[1] if not number_of_colorset(x) == None else 0) , print ("lambda : ",temp1  ,"candi(x) :",number_of_colorset(x),"candi: ", number_of_colorset.__name__, "answer[0] :", answer3[0], "answer[1] ", answer3[1]))
            temp3 = lambda x: ((number_of_colorset(x) * answer3[0] + answer3[1] if not number_of_colorset(x) == None else 0))
            tag3 = (number_of_colorset.__name__, answer3[0], answer3[1])
            solver.add((temp3,tag3))

    v4 = node_size(Xnode)
    if not isinstance(v4, int):
        pass
    else :
        answer4 = linear(v4, target)
        if answer4 != None:
            # temp4 = lambda x: ((node_size(x) * answer4[0] + answer4[1] if not node_size(x) == None else 0) , print ("lambda : ",temp4  ,"candi(x) :",node_size(x),"candi: ", node_size.__name__, "answer[0] :", answer4[0], "answer[1] ", answer4[1]))
            temp4 = lambda x: ((node_size(x) * answer4[0] + answer4[1] if not node_size(x) == None else 0))
            tag4 = (node_size.__name__, answer4[0], answer4[1])
            solver.add((temp4,tag4))

    v5 = onode_count1(Xnode)
    if not isinstance(v5, int):
        pass
    else :
        answer5 = linear(v5, target)
        if answer5 != None:
            # temp5 = lambda x: ((onode_count1(x) * answer5[0] + answer5[1] if not onode_count1(x) == None else 0) , print ("lambda : ",temp5  ,"candi(x) :",onode_count1(x),"candi: ", onode_count1.__name__, "answer[0] :", answer5[0], "answer[1] ", answer5[1]))
            temp5 = lambda x: ((onode_count1(x) * answer5[0] + answer5[1] if not onode_count1(x) == None else 0))
            tag5 = (onode_count1.__name__, answer5[0], answer5[1])
            solver.add((temp5,tag5))

    v6 = onode_count2(Xnode)
    if not isinstance(v6, int):
        pass
    else :
        answer6 = linear(v6, target)
        if answer6 != None:
            # temp6 = lambda x: ((onode_count2(x) * answer6[0] + answer6[1] if not onode_count2(x) == None else 0) , print ("lambda : ",temp6  ,"candi(x) :",onode_count2(x),"candi: ", onode_count2.__name__, "answer[0] :", answer6[0], "answer[1] ", answer6[1]))
            temp6 = lambda x: ((onode_count2(x) * answer6[0] + answer6[1] if not onode_count2(x) == None else 0))
            tag6 = (onode_count2.__name__, answer6[0], answer6[1])
            solver.add((temp6,tag6))

    v7 = onode_count3(Xnode)
    if not isinstance(v7, int):
        pass
    else :
        answer7 = linear(v7, target)
        if answer7 != None:
            # temp7 = lambda x: ((onode_count3(x) * answer7[0] + answer7[1] if not onode_count3(x) == None else 0) , print ("lambda : ",temp7  ,"candi(x) :",onode_count3(x),"candi: ", onode_count3.__name__, "answer[0] :", answer7[0], "answer[1] ", answer7[1]))
            temp7 = lambda x: ((onode_count3(x) * answer7[0] + answer7[1] if not onode_count3(x) == None else 0))
            tag7 = (onode_count3.__name__, answer7[0], answer7[1])
            solver.add((temp7,tag7))

    v8 = onode_count4(Xnode)
    if not isinstance(v8, int):
        pass
    else :
        answer8 = linear(v8, target)
        if answer8 != None:
            # temp8 = lambda x: ((onode_count4(x) * answer8[0] + answer8[1] if not onode_count4(x) == None else 0) , print ("lambda : ",temp8  ,"candi(x) :",onode_count4(x),"candi: ", onode_count4.__name__, "answer[0] :", answer8[0], "answer[1] ", answer8[1]))
            temp8 = lambda x: ((onode_count4(x) * answer8[0] + answer8[1] if not onode_count4(x) == None else 0))
            tag8 = (onode_count4.__name__, answer8[0], answer8[1])
            solver.add((temp8,tag8))

    return solver

    
