def pattern_solver_function(Xnode, target_pattern):
    solver = set()
    current_pattern = get_pattern(Xnode.Pnode_list)
    if current_pattern == target_pattern:
        temp = lambda x: get_pattern(x.Pnode_list)
        tag = ('pattern_exact_match',)
        solver.add((temp, tag))
    else:
        temp = lambda x: target_pattern
        tag = ('pattern_transformed',)
        solver.add((temp, tag))
    return solver
