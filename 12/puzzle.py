import re

def explore(graph, start, visited=[]):
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.append(neighbor)
            explore(graph, neighbor, visited)
    return visited

def connected_components(graph):
    count = 0
    programs = set(graph)
    while programs:
        program = next(iter(programs))
        programs = programs - set(explore(graph, program, []))
        count += 1
    return count
    
with open('./input.txt') as f:
    graph = {}
    for line in f:
        program, *neighbors = re.findall(r'\w+', line)
        graph[program] = neighbors

    print('1: {}'.format(len(explore(graph, '0', []))))
    print('2: {}'.format(connected_components(graph)))
