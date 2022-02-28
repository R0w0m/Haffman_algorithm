



def analysis(str):
    dict_ = {}
    for i in str:
        dict_[i] = [dict_[i][0]+1] if i in dict_ else [1]
    return dict_




def get_min(dict_):
    min_ = [None, None]
    val_ = [None, None]
    for i in dict_:
        if min_[0]:
            min_[0] = dict_[i][0]
            val_[0] = i
        else:
            if  min_[0] > dict_[i][0]
            min_[1] = min_[0]
            min_[0] = dict_[i][0]
            val_[1] = val_[0]
            val_[0] = i
'''    fst = 0

    for i in dict_:
        if min_[fst]:
            if min_[fst] > dict_[i][0]:
                min_[fst] = dict_[i][0]
                val_[fst] = i
                fst = 0 if fst else 1
        else:
            min_[fst] = dict_[i][0]
            val_[fst] = i
            fst = 0 if fst else 1'''
    return val_

def make_codes(tree):
    codes={}
    for i in tree:
        tree[i][2] = 

def main():
    symbol = analysis(input()) # symbol: [num]
    bin_tree = {} # symbol: [num, [douther_1, douther_2]]

    all_nodes_symb = dict(symbol)
    nd_num = 0
    while len(all_nodes_symb) > 1:
        min_ = get_min(all_nodes_symb)
        print(min_[0], min_[1])
        all_nodes_symb[f"node{nd_num}"] = [(all_nodes_symb[min_[0]][0] + all_nodes_symb[min_[0]][0]), [{min_[0]:all_nodes_symb[min_[0]]}, {min_[1]:all_nodes_symb[min_[1]]}]]
        print(min_[0], min_[1])
        del all_nodes_symb[min_[0]]
        del all_nodes_symb[min_[1]]
        nd_num += 1
    print(all_nodes_symb)

if __name__ == "__main__":
    main()
