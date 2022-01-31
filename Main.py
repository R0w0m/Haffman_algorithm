

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
            if min_[0] >= dict_[i][0]:
                min_[0] = dict_[i][0]
                val_[0] = i
        else:
            min_[0] = dict_[i][0]
            val_[0] = i


    for i in dict_:
        if not i == val_[0]:
            if min_[1]:
                if min_[1] >= dict_[i][0]:
                    min_[1] = dict_[i][0]
                    val_[1] = i
            else:
                min_[1] = dict_[i][0]
                val_[1] = i

    '''
    for i in dict_:
        if not min_[0]:
            if not min_[1]:
                min_[1] = dict_[i]
                val_[1] = i
                continue
            min_[0] = dict_[i]
            val_[0] = i
        else:
            if min_[1] >= dict_[i]:
                min_[1] = dict_[i]
                val_[1] = i
                continue
            if min_[0] >= dict_[i]:
                min_[0] = dict_[i]
                val_[0] = i
    '''
    return val_



def create_codes(tree_):
    codes = {}
    def get_code(d, code):
        for i in d:
            if "node" in i:
                    get_code(d[i][1][0], (code+"0"))
                    get_code(d[i][1][1], (code+"1"))
            else:
                codes[i] = code
    get_code(tree_, "")
    return codes


def encode_str(str_, codes):
    return "".join([codes[i] for i in str_])


def main():
    text_line = input()
    symbol = analysis(text_line) # symbol: [num]
    #bin_tree = {} # symbol: [num, [douther_1, douther_2]]

    all_nodes = dict(symbol)
    nd_num = 0
    while len(all_nodes) > 1:
        min_ = get_min(all_nodes)
        node_val = (all_nodes[min_[0]][0] + all_nodes[min_[1]][0])
        d1 = {min_[0]:all_nodes[min_[0]]} # daughter node 1
        d2 = {min_[1]:all_nodes[min_[1]]} # daughter node 2
        all_nodes[f"node{nd_num}"] = [node_val, [d1, d2]]
        del all_nodes[min_[0]]
        del all_nodes[min_[1]]
        nd_num += 1
    codes = create_codes(all_nodes)
    print(all_nodes, end = "\n\n")
    print("\n".join(f"{i}  {codes[i]}" for i in codes))
    print(encode_str(text_line, codes))

if __name__ == "__main__":
    main()


'''
{'node6': [11, [
    {'node4': [4, [
        {'node2': [2, [
            {'r': [1]},
            {'d': [1]}]]},
        {'node1': [2, [
            {' ': [1]},
            {'w': [1]}]]}]]},
    {'node5': [7, [
        {'l': [3]},
        {'node3': [4, [
            {'node0': [2, [
                {'h': [1]},
                {'e': [1]}]]},
            {'o': [2]}]]}]]}]]}]

{'node2': [85, [
    {'node0': [2, [
        {'q': [1]},
        {'w': [1]}]]},
    {'node1': [83, [
        {'e': [1]},
        {'r': [82]}]]}]]}
'''
