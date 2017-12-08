from collections import Counter
from functools import reduce

def find_roots(dag):
    # all nodes not visited are roots
    visited = []
    for node, props in dag.items():
        visited.extend(props['children'])
    roots = set(dag.keys()) ^ set(visited)
    return roots

def make_dag(nodes):
    dag = {}
    for node in nodes:
        props = {}
        props['weight'] = int(node[1].strip('()'))
        children = []
        try:
            for i in range(3, len(node)+1):
                children.append(node[i].strip(','))
        except IndexError:
            pass
        props['children'] = children
        dag[node[0]] = props

    return dag

def reverse_dag(dag):
    # populate reverse dag with nodes & weights
    rev_dag = {}
    for node, props in dag.items():
        rev_props = {}
        rev_props['weight'] = props['weight']
        rev_props['children'] = []
        rev_dag[node] = rev_props

    # reverse children
    for node, props in dag.items():
        for child in props['children']:
            rev_dag[child]['children'].append(node)

    return rev_dag

def find_weight(dag, root, total_weights):
    if not dag[root]['children']:
        return dag[root]['weight']

    if root in total_weights:
        return total_weights[root]

    child_weights = []
    for child in dag[root]['children']:
        child_weights.append(find_weight(dag, child, total_weights))

    child_weight = reduce(lambda x, y : x + y, child_weights)
    return dag[root]['weight'] + child_weight

def find_bad_weight(root_weights):
    weights = dict(Counter(root_weights).most_common())
    return list(weights.keys()).pop()

def a(dag):
    roots = find_roots(dag)
    return roots.pop()

def b(dag):
    total_weights = {}
    rev_dag = reverse_dag(dag)

    while rev_dag:
        # strip roots from rev_dag
        strip_roots = find_roots(rev_dag)
        for root in strip_roots:
            del rev_dag[root]

        # roots of rev_dag are now an inner layer from dag leaves
        # iterate through these to find unbalanced nodes
        roots = list(find_roots(rev_dag))
        for root in roots:
            children_weights = []
            for child in dag[root]['children']:
                total_weights[child] = find_weight(dag, child, total_weights)
                children_weights.append(total_weights[child])

            unique_weights = set(children_weights)
            if len(unique_weights) != 1:
                # find bad_weight and lookup unbalanced root weight
                delta = unique_weights.pop() - unique_weights.pop()
                bad_weight = find_bad_weight(children_weights)
                bad_node = list(total_weights.keys())[list(total_weights.values()).index(bad_weight)]
                return dag[bad_node]['weight'] - delta

with open("./input.txt") as f:
    dag = {}
    nodes = [line.strip().split() for line in f]
    dag = make_dag(nodes)
    rev_dag = reverse_dag(dag)
    print("a: {}".format(a(dag)))
    print("b: {}".format(b(dag)))
