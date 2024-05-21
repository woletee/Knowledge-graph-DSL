from itertools import combinations
#there is no any modifications done to this specifier function 
def specifer(KG, adj,target_xnode):  ## 다시 짜야할 것 같다. -> 람다함수 말고 그냥 유일하게 가지고 있는 특성들을 리스트로 반환하는 함수
    # adj, _ = print_adj(KG)
    node_info = extractor(KG, adj, target_xnode)
    speic = []
    if node_info["type"] == "Gnode":
        speic.append(("definition", "Gnode"))
        return tuple(speic)
    
    candi_node_list = []
    for n in KG[0]:
        if n.input  == 1 and (n.type == "Onode" or n.type == "Gnode") :
            candi_node_list.append(extractor(KG, adj, n))
    
    obj_def = node_info["definition"]
    speic.append(("definition", obj_def))
    
    for property in node_info["properties"]:
        speic.append(("properties", property))


    all_combinations = []
    for r in range(1, len(speic) + 1):
        all_combinations.extend(combinations(speic, r))

    # print("properties of target_node :", speic)
    for i, combo in enumerate(all_combinations):
        # print("combo :", combo)
        t_node = []
        for candi_info in candi_node_list:
            # print("candi_info :", candi_info)
            match = 1
            for c in combo :
                # print(c[0], c[1])
                if c[0] == "definition":
                    if c[1] != candi_info[c[0]] :   
                        match = 0    
                else :
                    if c[1] not in candi_info[c[0]]:
                        match = 0  
            if match == 1:
                t_node.append(n)
                # print("추가됨")
        # print("len of t_node :", len(t_node))
        if len(t_node) == 1:
            return combo
        else :
            continue
    return None
