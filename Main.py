

def analysis(str):
    dict_ = {}
    for i in str:
        dict_[i] = [dict_[i][0]+1] if i in dict_ else [1]
    return dict_


def get_min(dict_):
    min_ = [None, None]
    val_ = [None, None]
    fst = 0
    for i in dict_:
        if min_[fst]:
            if min_[fst] > dict_[i][0]:
                min_[fst] = dict_[i][0]
                val_[fst] = i
                fst = 0 if fst else 1
        else:
            min_[fst] = dict_[i][0]
            val_[fst] = i
            fst = 0 if fst else 1
    return val_



def create_codes(tree_):
    print(tree_)
    codes = {}
    def get_code(d, code):
        bit = 0
        for i in d:
            if "node" in i:
                for j in d[i][1]:
                    get_code(d[i][1], (code+bit))
            else:
                codes[i] = int(str(code)[1:])
    get_code(tree_, 0)
    return codes

def main():
    symbol = analysis(input()) # symbol: [num]
    #bin_tree = {} # symbol: [num, [douther_1, douther_2]]

    all_nodes = dict(symbol)
    nd_num = 0
    while len(all_nodes) > 1:
        min_ = get_min(all_nodes)
        node_val = (all_nodes[min_[0]][0] + all_nodes[min_[1]][0])
        d1 = {min_[0]:all_nodes[min_[0]]} # dought node 1
        d2 = {min_[1]:all_nodes[min_[1]]} # dought node 2
        all_nodes[f"node{nd_num}"] = [node_val, [d1, d2]]
        del all_nodes[min_[0]]
        del all_nodes[min_[1]]
        nd_num += 1
    print(create_codes(all_nodes))

if __name__ == "__main__":
    main()


{'node4': [21, [{'node2': [9, [{'node0': [3, [{'1': [1]}, {'2': [2]}]]}, {'6': [6]}]]}, {'node3': [12, [{'5': [5]}, {'node1': [7, [{'3': [3]}, {'4': [4]}]]}]]}]]}
