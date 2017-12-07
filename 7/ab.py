from collections import Counter
from functools import reduce

def find_root(adj_list):
    visited = []
    for node, props in adj_list.items():
        visited.extend(props[1])
    root = set(adj_list.keys()) ^ set(visited)
    return root.pop()

def find_unbalanced(weights, delta):
    counter = Counter(weights)
    unique = counter.most_common()[-1:]
    return unique[0][0]

def find_weight(adj_list, root):
    if not adj_list[root][1]:
        return adj_list[root][0]

    child_weights = []
    for child in adj_list[root][1]:
        child_weights.append(find_weight(adj_list, child))

    child_weight = set(child_weights)
    if len(child_weight) != 1:
        delta = child_weight.pop() - child_weight.pop()
        unbalanced_node = find_unbalanced(child_weights, delta)
        unbalanced_root = child_weights.index(unbalanced_node)
        print("{}".format(adj_list[adj_list[root][1][unbalanced_root]][0]-delta))
        return adj_list[root][0] + reduce(lambda x, y : x + y, child_weights)
    else:
        child_weight = reduce(lambda x, y : x + y, child_weights)
        root_weight = adj_list[root][0] + child_weight
        return root_weight

with open("./input.txt") as f:
    adj_list = {}
    nodes = [line.strip().split() for line in f]

    for node in nodes:
        props = []
        props.append(int(node[1].strip('()')))
        neighbors = []
        try:
            for i in range(3, len(node)+1):
                neighbors.append(node[i].strip(','))
        except IndexError:
            pass
        props.append(neighbors)
        adj_list[node[0]] = props

    root = find_root(adj_list)
    print("a: {}".format(root))
    print("b: {}".format(find_weight(adj_list, root)))
