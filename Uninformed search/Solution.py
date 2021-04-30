import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue


def read_fn():
    G = nx.Graph()
    edgeList = pd.read_csv('aedge_list.csv')
    c = 0
    for i in edgeList["from"]:
        G.add_weighted_edges_from([(
            i, edgeList["to"][c], edgeList["weight"][c])])
        c += 1
    return G


answer = []
cost = 0

colo = []
options = {
    'node_size': 300,
    'with_labels': True,
    'font_weight': 'bold',
    'node_color': colo,
    'with_labels': True
}


def print_fn(s, e, G):

    global answer
    color_map = {}
    n = len(G)

    for node in G:
        color_map[node] = 'red'

    for d in answer:
        color_map[d] = 'yellow'

    color_map[s] = 'green'
    color_map[e] = 'blue'

    for key, val in color_map.items():
        colo.append(val)
    nx.draw(G, **options)
    plt.show()


def BFS(s, e, G):

    global cost, answer
    vis = dict()
    for node in G:
        vis[node] = False

    queue = []
    flag = 0
    open_l = Queue()
    closed_l = Queue()
    queue.append(s)
    open_l.put(s)
    vis[s] = True

    print("{:<15} {:<15}".format('Open', 'Closed'))
    print("{:<15} {:<15}".format(
        ''.join(list(open_l.queue)), ''.join(list(closed_l.queue))))

    while queue:
        s = queue.pop(0)
        answer.append(s)
        closed_l.put(s)

        if (s == e):
            break

        for i in G[s]:
            if vis[i] is False:
                queue.append(i)
                vis[i] = True
                open_l.put(i)
                cost += G[s][i]['weight']
                if (i == e):
                    flag = 1
                    break

        open_l.get()
        print("{:<15} {:<15}".format(
            ''.join(list(open_l.queue)), ''.join(list(closed_l.queue))))

        if (flag == 1):
            break


def DFSUtil(v, e, G, visited):

    global cost, answer
    flag = 0
    visited.add(v)
    answer.append(v)
    if(v == e):
        return 1

    for neighbour in G[v]:
        if neighbour not in visited:
            print(v, neighbour, G[v][neighbour]['weight'])
            cost += G[v][neighbour]['weight']
            if(DFSUtil(neighbour, e, G, visited) == 1):
                flag = 1
                break

    return flag


def DFS(s, e, G):

    visited = set()
    DFSUtil(s, e, G, visited)


def UCS(start, end, G):

    global cost, answer
    goal = []
    goal.append(end)

    ans = []
    queue = []

    for i in range(len(goal)):
        ans.append(10**8)

    queue.append([0, start])

    visited = {}
    count = 0

    while (len(queue) > 0):

        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] *= -1

        if (p[1] in goal):

            index = goal.index(p[1])
            if (ans[index] == 10**8):
                count += 1

            if (ans[index] > p[0]):
                ans[index] = p[0]

            del queue[-1]
            queue = sorted(queue)
            if (count == len(goal)):
                cost = ans[0]
                return

        if (p[1] not in visited):
            for i, k in (G[p[1]].items()):
                queue.append(
                    [(p[0] + k['weight']) * -1, i])
                print(queue)
        visited[p[1]] = 1

    cost = ans[0]


G = read_fn()
UCS('A', 'M', G)
#BFS('A', 'M', G)
#DFS('A', 'M', G)
print("path->", answer, "cost ->", cost)
print_fn('A', 'M', G)
