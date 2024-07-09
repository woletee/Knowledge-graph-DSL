def Solution_generaterrs(task):
    KG = Make_KG(task)
    pair_1 = KG[0]
    for n in KG[0][0]:
        if isinstance(n, Gnode) and n.output == 1:
            target = (get_height(n), get_width(n), number_of_colorsett(n), get_pattern(n.Node_list))
    
    node_solver_pattern = set()
    
    for n in pair_1[0]:   
        if isinstance(n, Onode) or isinstance(n, Gnode):
            if n.output == 1:
                continue

            ans_pattern = pattern_solver_function(n, target[3])
            if ans_pattern:
                for a in ans_pattern:
                    node_solver_pattern.add((n, a))
    
    solver_pattern = set()
    
    print("generating solver for pattern")
    for i, s_pattern in enumerate(node_solver_pattern):
        progress = (i + 1) / len(node_solver_pattern) * 100
        bar_width = int(progress)
        print('\r [%-*s] %.1f%%' % (100, '=' * bar_width, progress), end='')
        temp = specifer(KG[0], adj, s_pattern[0])
        if temp:
            temp = tuple(temp)
        else:
            continue
        solver_pattern.add((temp, s_pattern[1]))
    
    print("\nsolver num:", len(solver_pattern))
    for i in range(1, len(KG)):
        adj, _ = print_adj(KG[i])
        candi_node = []
        candi_node_info = []
        for n in KG[i][0]:
            if isinstance(n, Gnode) and n.output == 1:
                target_i = (get_height(n), get_width(n), number_of_colorsett(n), get_pattern(n.Node_list))
            if (n.type == "Gnode" or n.type == "Onode") and n.input == 1:
                candi_node_info.append(extractor(KG[i], adj, n))
                candi_node.append(n)
                
        new_solver_pattern = set()
        
        for k, s in enumerate(solver_pattern):
            for j, n_info in enumerate(candi_node_info):
                if speci_tester(s, n_info) == False:
                    continue
                if s[1][0](candi_node[j]) == target_i[3]:
                    new_solver_pattern.add(s)
                    break
        solver_pattern = new_solver_pattern

        print("after ", i+1,"th pair solver num:", len(solver_pattern))
    print("finish finding possible solvers")
    return solver_pattern
