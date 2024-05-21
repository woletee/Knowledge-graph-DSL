def speci_tester(s, n_info):
    for tag in s[0]:
        if tag[0] == "definition":
            if tag[1] != n_info["definition"] :   
                return False
        else :
            if tag[1] not in n_info["properties"] : 
                return False
    return True
def Solution_generaterrs(task):
    KG = Make_KG(task)
    pair_1 = KG[0]
    for n in KG[0][0]:
        if isinstance(n, Gnode) and n.output == 1:
            target = (get_height(n), get_width(n), number_of_colorsett(n))   ###added the number_of_colorsett to get the target colors
    
    node_solver_h = set()
    node_solver_w = set()
    node_solver_color = set()
    
    for n in pair_1[0]:   
        if isinstance(n, Onode) or isinstance(n, Gnode):
            if n.output == 1:
                continue
            # ans_h = solver_function(n, target[0])
            # if ans_h:
            #     for a in ans_h:
            #         node_solver_h.add((n, a))
                    
            # ans_w = solver_function(n, target[1])
            # if ans_w:
            #     for a in ans_w:
            #         node_solver_w.add((n, a))
            
            ans_color = color_solver_function(n, target[2])
            if ans_color:
                for a in ans_color:
                    node_solver_color.add((n, a))
    
    solver_h = set()
    solver_w = set()
    solver_color = set()
    # for s in node_solver_h:
    #     print("type : ",s[0].type , "func : ", s[1][1])
    #     if isinstance(s[0], Gnode):
    #         print(s[1][0](s[0]))
    # print("#############################################")
    adj,_ = print_adj(KG[0])
    print("solver without spicifer : ",len(node_solver_h) , len(node_solver_w), len(node_solver_color))

    # print("generating solver for h")
    # for i, s_h in enumerate(node_solver_h):
    #     progress = (i + 1) / len(node_solver_h) * 100
    #     bar_width = int(progress)
    #     print('\r [%-*s] %.1f%%' % (100, '=' * bar_width, progress), end='')
    #     temp = specifer(KG[0], adj, s_h[0])    
    #     if temp:
    #         temp = tuple(temp)
    #     else:
    #         continue
    #     solver_h.add((temp, s_h[1]))
    # print("\ngenerating solver for w")
    # for i, s_w in enumerate(node_solver_w):
    #     progress = (i + 1) / len(node_solver_w) * 100
    #     bar_width = int(progress)
    #     print('\r [%-*s] %.1f%%' % (100, '=' * bar_width, progress), end='')
    #     temp = specifer(KG[0],adj, s_w[0])    
    #     if temp:
    #         temp = tuple(temp)
    #     else:
    #         continue
    #     solver_w.add((temp, s_w[1]))
    print("\ngenerating solver for c")
    for i, s_color in enumerate(node_solver_color):
        progress = (i + 1) / len(node_solver_color) * 100
        bar_width = int(progress)
        print('\r [%-*s] %.1f%%' % (100, '=' * bar_width, progress), end='')
        temp = specifer(KG[0],adj, s_color[0])
        if temp:
            temp = tuple(temp)
        else:
            continue
        solver_color.add((temp, s_color[1]))
    
    print("\nsolver num:", len(solver_h), len(solver_w), len(solver_color)) 
    for i in range(1, len(KG)):
        adj, _ = print_adj(KG[i])
        candi_node = []
        candi_node_info = []
        for n in KG[i][0]:
            if isinstance(n, Gnode) and n.output == 1:
                target_i = (get_height(n), get_width(n), number_of_colorsett(n))    ####addedd the function for getting the number of color set 
            if (n.type == "Gnode" or n.type == "Onode") and n.input == 1:
                candi_node_info.append(extractor(KG[i], adj, n))
                candi_node.append(n)
                
        new_solver_h = set()
        new_solver_w = set()
        new_solver_color = set()
        
        # for k, s in enumerate(solver_h):
        #     for j, n_info in enumerate(candi_node_info):
        #         if speci_tester(s, n_info) == False:
        #             continue
        #         if s[1][0](candi_node[j]) == target_i[0]:
        #             new_solver_h.add(s)
        #             break
        # solver_h = new_solver_h
        # for k, s in enumerate(solver_w):
        #     for j, n_info in enumerate(candi_node_info):
        #         if speci_tester(s, n_info) == False:
        #             continue
        #         if s[1][0](candi_node[j]) == target_i[1]:
        #             new_solver_w.add(s)
        #             break
        # solver_w = new_solver_w
        
        for k, s in enumerate(solver_color):
            for j, n_info in enumerate(candi_node_info):
                if speci_tester(s, n_info) == False:
                    continue
                if s[1][0](candi_node[j]) == target_i[2]:
                    new_solver_color.add(s)
                    break 
        solver_color = new_solver_color   #### for Color 

        print("after ",i+1,"th pair solver num:", len(solver_h), len(solver_w), len(solver_color))
    print("finish finding possible solvers")
    return solver_h, solver_w, solver_color
