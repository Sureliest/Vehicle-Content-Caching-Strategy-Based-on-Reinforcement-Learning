import networkx as nx

G = nx.Graph()
G.add_edge(0, 1, weight=1)
G.add_edge(0, 2, weight=1)
G.add_edge(0, 3, weight=3)
G.add_edge(1, 4, weight=4)
G.add_edge(1, 5, weight=4)
G.add_edge(2, 5, weight=4)
G.add_edge(0, 6, weight=4)
G.add_edge(3, 6, weight=4)
G.add_edge(4, 7, weight=4)
G.add_edge(4, 8, weight=4)
G.add_edge(5, 8, weight=4)
G.add_edge(5, 6, weight=4)
G.add_edge(6, 9, weight=4)

D = []
for i in G.node:
    D.append(i)
F = []
degree = []
for i in range(G.number_of_nodes()):
    degree.append(G.degree[i])

while len(list(set(D) - set(F))) != 0:
    min = 9999
    for i in set(D) - set(F):
        if degree[i] < min:
            u = i
            min = degree[i]
    uu = []
    uu.append(u)
    g = G.subgraph(set(D)-set(uu))
    n = len(list(nx.connected_components(g)))
    if n != 1:
        F = set(F) | set(uu)
    else:
        D = set(D) - set(uu)
        for s in set(D) & set(list(nx.neighbors(G, u))):
            degree[s] = degree[s] - 1
        if len(list(set(list(nx.neighbors(G, u))) & set(F))) == 0:
            max = 0
            for i in list(nx.neighbors(G, u)):
                if degree[i] > max:
                    w = i
                    max = degree[i]
            ww = []
            ww.append(w)
            F = set(F) | set(ww)
    print(D)
    print(F)
    print(set(D)-set(F))
    print('\n')
print(D)



sub = G.subgraph(D)
s = 0
print(1)
visited = []
un = []
for i in sub.node:
    if i != s:
        un.append(i)

visited.append(s)

print(visited)
print(un)
next_hop = [[] for i in range(G.number_of_nodes())]

print(sub)


def dfs(sub, s, visited, un, next_hop):
    if len(un) == 0:
        return
    for i in sub._adj[s]:
        if visited.count(i) == 0:
            next_hop[s].append(i)
            visited.append(i)
            if un.count(i) != 0:
                un.remove(i)
            dfs(sub, i, visited, un, next_hop)
    return


dfs(sub, 0, visited, un,next_hop)

un = []
visited = []
for i in D:
    visited.append(i)

for i in G.node:
    if visited.count(i) == 0:
        un.append(i)

for i in G.node:
    for next in G.adj[i]:
        if visited.count(next) == 0:
            next_hop[i].append(next)
            visited.append(next)
            un.remove(next)

print(next_hop)